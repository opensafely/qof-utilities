import argparse
import docx
from docx.document import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
from collections import defaultdict
import re
import pandas as pd
import pathlib


def parse_table(table, extra_trim=True):
    """
    Set the second row as the column headers
    Remove the first two rows and the last row
    Register header is one row higher
    """
    trim = 0
    if extra_trim:
        trim += 1
    if table is not None:
        new_table = table.copy()
        new_table.rename(columns=new_table.iloc[0 + trim], inplace=True)
        new_table = new_table[1 + trim :].reset_index(drop=True)
        new_table = new_table[:-1]
        return new_table
    else:
        return pd.DataFrame()


class Indicator:
    def __init__(
        self,
        indicator_table,
        denominator_table=None,
        numerator_table=None,
        extra_trim=True,
    ):
        self.indicator_id = indicator_table[0][1]
        self.description = indicator_table[1][1]
        self.numerator = parse_table(numerator_table, extra_trim)
        self.denominator = parse_table(denominator_table, extra_trim)
        self.rule_count = len(self.denominator.index) + len(self.numerator.index)
        self.line_count = self._line_count()

    def __str__(self):
        return self.indicator_id

    def __repr__(self):
        return "Indicator(indicator_id={}, rule_count={}, line_count={})".format(
            self.indicator_id, self.rule_count, self.line_count
        )

    # TODO: Check this is working as expected
    def _line_count(self):
        total = 0
        if not self.numerator.empty:
            total += sum(len(re.split("OR|AND", x)) for x in self.numerator["Rule"])
        if not self.denominator.empty:
            total += sum(len(re.split("OR|AND", x)) for x in self.denominator["Rule"])
        return total


# Redefine text property to include hyperlinks
Paragraph.text = property(lambda self: get_paragraph_text(self))


# https://github.com/python-openxml/python-docx/issues/40
def iter_block_items(parent):
    """
    Yield each paragraph and table child within *parent*, in document order.
    Each returned value is an instance of either Table or Paragraph.
    """
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


# https://github.com/python-openxml/python-docx/issues/85
def get_paragraph_text(paragraph):
    """
    Include hyperlink as text
    """

    def get_tag(element):
        return "%s:%s" % (
            element.prefix,
            re.match("{.*}(.*)", element.tag).group(1),
        )

    text = ""
    run_count = 0
    for child in paragraph._p:
        tag = get_tag(child)
        if tag == "w:r":
            text += paragraph.runs[run_count].text
            run_count += 1
        if tag == "w:hyperlink":
            for subchild in child:
                if get_tag(subchild) == "w:r":
                    text += subchild.text
    return text


# https://github.com/python-openxml/python-docx/issues/757
# TODO: Current issue python-docx parsing cell with form field (i.e. drop-down)
# The library skips the cell rather than leaving an empty string
# Fine if there is additional text in the cell; an issue if JUST the drop-down
# Current solution is to manually remove content control from each word doc
def build_table_dictionary(doc):
    """
    Create a dictionary of document tables by table header text
    Save any text that starts with an interger as a potential table header
    """
    table_lookup = defaultdict(list)
    for block in iter_block_items(doc):
        if isinstance(block, Table):
            df = [
                ["" for i in range(len(block.columns))] for j in range(len(block.rows))
            ]
            for i, row in enumerate(block.rows):
                for j, cell in enumerate(row.cells):
                    if cell.text:
                        df[i][j] = cell.text.strip()
            table_lookup[last_text].append(pd.DataFrame(df))
        else:
            # AF was prefixed with 3.2.4\tClinical data extraction criteria
            if "Heading" in block.style.name:
                last_text = re.sub(r"^[\d.-]+\s*", "", block.text.strip())
    return table_lookup


# TODO: not currently parsing "Cohorts" (Vaccination)
def get_register(table_lookup):
    """
    Older clinical areas had the register as a separate indicator
    But the actual rules are always defined in section 3
    To capture the register rules in complexity analysis always analyse
    """
    dataset_tables = table_lookup["Case registers"]
    for i in range(len(dataset_tables)):
        if "_REG" in dataset_tables[i][0][1]:
            return Indicator(dataset_tables[i], dataset_tables[i + 1], extra_trim=False)


def get_indicators(table_lookup):
    """
    Parse indicator tables "Indicator(s)", creating a dict of Indicator objects
    Grab tables in groups of three (indicator, numerator, denominator)
    If there is no third table, numerator and denominator may be combined
    """
    indicators = table_lookup["Indicator(s)"]
    indicator_dict = {}
    ind_iter = iter(range(len(indicators)))
    for i in ind_iter:
        first_indicator = indicators[i]
        if "maintains a register" in first_indicator[1][1]:
            # Skip a register indicator, handled elsewhere
            continue
        try:
            second_indicator = indicators[i + 1]
        except IndexError:
            continue
        # Grab the next two denominator and numerator tables
        try:
            third_indicator = indicators[i + 2]
            # Skip two iterations for the numerator and denominator
            next(ind_iter)
            next(ind_iter)
        except IndexError:
            # If there is no third indicator, then numerator and
            # denominator may be combined
            split = second_indicator[
                second_indicator[0] == "End of denominator rules"
            ].index[0]
            if split:
                third_indicator = second_indicator[split + 1 :]
                # TODO: find way to drop null rows
                third_indicator = third_indicator[2:]
                third_indicator.reset_index(drop=True)
                second_indicator = second_indicator[:split]
                # Skip one iteration for the combined table
                next(ind_iter)
        indicator_obj = Indicator(indicators[i], second_indicator, third_indicator)
        indicator_dict[indicator_obj.indicator_id] = indicator_obj
    return indicator_dict


def extract_one(doc_path):
    """
    Output csv for each indicator
    """
    doc = docx.Document(doc_path)
    table_lookup = build_table_dictionary(doc)
    indicators = get_indicators(table_lookup)
    variables = parse_table(
        table_lookup["Clinical data extraction criteria"][0], extra_trim=False
    )
    codelists = parse_table(table_lookup["Clinical code clusters"][0], extra_trim=False)
    import code

    code.interact(local=locals())
    return indicators


def summary_stats(docs_dir):
    counts = []
    for f in docs_dir.rglob("*.docx"):
        doc = docx.Document(f)
        table_lookup = build_table_dictionary(doc)
        register = get_register(table_lookup)
        indicators = get_indicators(table_lookup)
        variables = parse_table(
            table_lookup["Clinical data extraction criteria"][0], extra_trim=False
        )
        codelists = parse_table(
            table_lookup["Clinical code clusters"][0], extra_trim=False
        )
        if register:
            indicators[register.indicator_id] = register
        counts.append(
            [
                f.name,
                len(indicators),
                sum(x.rule_count for x in indicators.values()),
                sum(y.line_count for y in indicators.values()),
                len(variables),
                len(codelists),
            ]
        )
    df = (
        pd.DataFrame(
            counts,
            columns=[
                "Clinical Area",
                "Indicators",
                "Rules",
                "Lines",
                "Variables",
                "Code clusters",
            ],
        )
        .sort_values(["Indicators", "Rules"], ascending=(False, False))
        .reset_index(drop=True)
    )
    print(df.to_markdown(index=False))
    df.to_csv(f.parent / "counts.csv")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parse QOF documents")
    parser.add_argument(
        "doc_path",
        type=pathlib.Path,
        help="Path to QOF docs directory or single doc file",
    )

    args = parser.parse_args()
    if args.doc_path.is_dir():
        summary_stats(args.doc_path)
    else:
        extract_one(args.doc_path)
