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


class Indicator:
    def __init__(
        self, indicator_table, denominator_table=None, numerator_table=None
    ):
        self.indicator_id = indicator_table[0][1]
        self.description = indicator_table[1][1]
        self.numerator = self._parse_indicator(numerator_table)
        self.denominator = self._parse_indicator(denominator_table)
        self.rule_count = len(self.denominator.index) + len(
            self.numerator.index
        )
        self.line_count = self._line_count()

    def _parse_indicator(self, table):
        """
        Set the second row as the column headers
        Remove the first two rows and the last row
        """
        if table is not None:
            new_table = table.copy()
            new_table.rename(columns=new_table.iloc[1], inplace=True)
            new_table = new_table[2:].reset_index(drop=True)
            new_table = new_table[:-1]
            return new_table
        else:
            return pd.DataFrame()

    # TODO: Check this is working as expected
    def _line_count(self):
        """ """
        if not self.numerator.empty:
            num_total = sum(
                len(re.split("OR|AND", x)) for x in self.numerator["Rule"]
            )
            denom_total = sum(
                len(re.split("OR|AND", x)) for x in self.denominator["Rule"]
            )
            return num_total + denom_total
        else:
            return 0


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
# TODO: Extra parsing to eliminate Numerator/Denominator rows?
# TODO: Current issue python-docx parsing cell with form field (i.e. drop-down)
# The library skips the cell rather than leaving an empty string
# It works fine if there is additional text in the cell
# Current solution is to manually remove content control from each word doc
def build_table_dictionary(doc):
    table_lookup = defaultdict(list)
    for block in iter_block_items(doc):
        if isinstance(block, Table):
            df = [
                ["" for i in range(len(block.columns))]
                for j in range(len(block.rows))
            ]
            for i, row in enumerate(block.rows):
                for j, cell in enumerate(row.cells):
                    if cell.text:
                        df[i][j] = cell.text.strip()
            table_lookup[last_text].append(pd.DataFrame(df))
        else:
            if re.match("(\d+)", block.text.strip()):
                last_text = block.text.strip()
    return table_lookup


def get_indicators(table_lookup):
    indicators = table_lookup["4. Outputs"]
    indicator_list = []
    for i in range(len(indicators)):
        if indicators[i][0][0] == "Indicator ID":
            if indicators[i + 1][0][0] == "Indicator ID":
                indicator_list.append(Indicator(indicators[i]))
            else:
                # Grab the next two denominator and numerator tables
                indicator_list.append(
                    Indicator(
                        indicators[i], indicators[i + 1], indicators[i + 2]
                    )
                )
                # Skip two iterations for the numerator and denominator
                i = i + 2
    return indicator_list


def run_one(docx_path, json_path):
    doc = docx.Document(docx_path)
    table_lookup = build_table_dictionary(doc)
    indicators = get_indicators(table_lookup)


def run():
    for f in pathlib.Path("converted").rglob("*.docx"):
        doc = docx.Document(f)
        table_lookup = build_table_dictionary(doc)
        indicators = get_indicators(table_lookup)
        print(
            f,
            len(indicators),
            sum(x.rule_count for x in indicators),
            sum(y.line_count for y in indicators),
        )


if __name__ == "__main__":
    # import sys
    # run_one(sys.argv[1], sys.argv[2])
    run()
