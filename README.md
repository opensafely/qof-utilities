# Using OpenSAFELY to analyse QOF indicators

## Motivation

The goal of this repository is to help a researcher build on the OpenSAFELY [research-template](https://github.com/opensafely/research-template) to investigate montly changes in Quality and Outcomes Framework ([QOF](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof)) registers.
This repo contains [resources](/), [discussion](https://github.com/opensafely/qof-utilities/discussions), and [issues](https://github.com/opensafely/qof-utilities/issues) surrounding the use of OpenSAFELY to assess the impact of the pandemic on routine care through the assessment of ([QOF](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof)).

New QOF studies should start by using the [OpenSAFELY research template](https://github.com/opensafely/research-template) and follow the general structure of this repository where possible, see ['Repository structure'](#repository-structure) section below.

## QOF business rules for registers

[The Quality and Outcomes Framework (QOF)](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof) outlines several indicators that focus hypertension (HYP) targets. 
This project aims to use OpenSAFELY to quantify the extent to which any of the relevant Hypertension QOF indicators ([v46](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/quality-and-outcome-framework-qof-business-rules/qof-business-rules-v46.0-2021-2022-baseline-release)) were disrupted during the pandemic but wont link our results to clinical outcomes.
A short description of the QOF Hypertension ([v46](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/quality-and-outcome-framework-qof-business-rules/qof-business-rules-v46.0-2021-2022-baseline-release)) register and each indicator is shown below:

* **HYP_REG**: Hypertension register: Patients with an unresolved diagnosis of hypertension.

## Repository structure 

The following list outlines the the general steps for implementing QOF in OpenSAFELY:

1. Add all codelists specified in the QOF busieness rules to [codelists/codelists.txt](codelists/codelists.txt). 
   The codelists can be found on OpenCodelists under [NHSD Primary Care Domain Refsets](https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/).
2. Define the variables specified in the business rules in shared variable dictionaries
3. Implement QOF registister logic in the study definition (see [here](#study-definitions))
4. Specify measures (e.g., total achievement and breakdowns) for each indicator (see [here](#measures))

### Codelists

* All codelists used in this project are available in the [codelists](codelists) folder.

### Variable dictionaries

Variables that are shared by multiple QOF indicators are specified in dictionaries (see [OpenSAFELY programming tricks](https://docs.opensafely.org/study-def-tricks/#sharing-common-study-definition-variables)):
* **Demographic variables**: [analysis/dict_demographic_variables.py](analysis/dict_demo_variables.py)
* Variables to define a QOF **register** (`xxx_reg_variables`): e.g., [analysis/dict_hyp_variables.py](analysis/dict_hyp_variables.py)

    Almost all business rules can be broken down into individual variables that follow this strucutre: 
    (1) a clinical codelist and a 
    (2) timeframe, so variable names are following this  structure: `<name_of_codelist>_<time_frame>`.

    TODO ADD EXAMPLE

  * Where the date of the variable will also be needed, we can make use of the `include_date_*` argument. 
    Depending on the variable description the additional arguments `find_first_match_in_period` or `find_last_match_in_period` need to be set to `True`.
    This will include the date associated with each event to the dataframe (see [OpenSAFELY variable reference](https://docs.opensafely.org/study-def-variables/)).
  * The variables defined in these dictionaries can then be loaded as needed in individual study defintions using `** name_of_variable_dictionary,`).
### Study definitions

* Each register (e.g., HYP_REG / HYP001) is specified in individual study definitions. 
  Within each study definition, we can compose variables from the dictionaries using the `patients.satisfying()` function to:
  1. Create a variable for each rule (e.g., ADD EXAMPLE), where variables for each rule number are named following this structure: `<indicator>_<register>_<rule_number>`.
  2. These rule variables can then again be composed to create the register variables (e.g., `hyp_reg`).

  Examples can be found here:
    * **HYP001**: [analysis/study_definition_hyp001.py](analysis/study_definition_hyp001.py)

* Commonly used dates (e.g., '*Payment Period Start Date*') are defined in [analysis/config.py](analysis/config.py)

### Actions

All actions are defined in the [project.yaml](project.yaml).

* Each register has the following actions:
  * `generate_study_population_xxx***`: Extract study population
  * `generate_measures_xxx***`: Generate measures using the `Measure()` framework (see [OpenSAFELY documentation](https://docs.opensafely.org/measures/))
  * `join_ethnicity_xxx`

# About the OpenSAFELY framework

Developers and epidemiologists interested in the framework should review [the OpenSAFELY documentation](https://docs.opensafely.org)
The OpenSAFELY framework is a Trusted Research Environment (TRE) for electronic
health records research in the NHS, with a focus on public accountability and
research quality.
Read more at [OpenSAFELY.org](https://opensafely.org).

# Licences
As standard, research projects have a MIT license. 
