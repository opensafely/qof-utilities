# Using OpenSAFELY to analyse QOF indicators

## Motivation

The goal of this repository is to help a researcher build on the OpenSAFELY [research-template](https://github.com/opensafely/research-template) to investigate montly changes in Quality and Outcomes Framework ([QOF](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof)) registers.
This repo contains resources (reusable code) and more deatiled discussions around how to use and build on the code provided in this repository.

## Content

This repo currently contains all resources for the following QOF registers:

- Asthma (AST_REG): 
  - Codelists: [analysis/codelists_ast.py](analysis/codelists_ast.py)
  - Variable definitions: [analysis/dict_ast_variables.py](analysis/dict_ast_variables.py)
  - Study definition and measures: [analysis/study_definition_ast_reg.py](analysis/study_definition_ast_reg.py)
- Learning disability (LD_REG):
  - Codelists: [analysis/codelists_ls.py](analysis/codelists_ls.py)
  - Variable definitions: [analysis/dict_ls_variables.py](analysis/dict_ls_variables.py)
  - Study definition and measures: [analysis/study_definition_ls_reg.py](analysis/study_definition_ls_reg.py)
- Hypertension (HYP_REG):
  - Codelists: [analysis/codelists_hyp.py](analysis/codelists_hyp.py)
  - Variable definitions: [analysis/dict_hyp_variables.py](analysis/dict_hyp_variables.py)
  - Study definition and measures: [analysis/study_definition_hyp_reg.py](analysis/study_definition_hyp_reg.py)
- Palliative Care (PC_REG):
  - Codelists: [analysis/codelists_pc.py](analysis/codelists_pc.py)
  - Variable definitions: [analysis/dict_pc_variables.py](analysis/dict_pc_variables.py)
  - Study definition and measures: [analysis/study_definition_pc_reg.py](analysis/study_definition_pc_reg.py)
- Diabetes (DM_REG):
  - Codelists: [analysis/codelists_dm.py](analysis/codelists_dm.py)
  - Variable definitions: [analysis/dict_dm_variables.py](analysis/dict_dm_variables.py)
  - Study definition and measures: [analysis/study_definition_dm_reg.py](analysis/study_definition_dm_reg.py)
- Stroke / TIA (STIA_REG):
  - Codelists: [analysis/codelists_stia.py](analysis/codelists_stia.py)
  - Variable definitions: [analysis/dict_stia_variables.py](analysis/dict_stia_variables.py)
  - Study definition and measures: [analysis/study_definition_stia_reg.py](analysis/study_definition_stia_reg.py)


## Repository structure 

The following list describes the general structure of this repository:

### Specific files for each register

- All codelists specified in the QOF busieness rules are added to [codelists/codelists.txt](codelists/codelists.txt). 
  The codelists can be found on OpenCodelists under [NHSD Primary Care Domain Refsets](https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/).
  Note that the *codelists.txt* file in this repository specifies the codelists for all the registers implemented here. 
- The codelists needed for a specific QOF register (e.g., hypertension) are loaded in [analysis/codelists_hyp.py](analysis/codelists_hyp.py)
- The variables specified in the business rules are available in shared variable dictionaries specific to each QOF register (e.g., shared variables for implementing the hypertension register are available here: [analysis/dict_hyp_variables.py](analysis/dict_hyp_variables.py))
- The logic of the QOF business rules is also composed inside the shared variable dictionary (e.g., variable `hyp_reg` in [analysis/dict_hyp_variables.py](analysis/dict_hyp_variables.py))
- The study definition for each register makes use of the variables defined in the shared dictionaries and defines the the population list size in the `population` variable (e.g., 6 or older for asthma, see [analysis/study_definition_ast_reg.py](analysis/study_definition_ast_reg.py)).

### Shared files across all registers

- Codelists used for breakdowns of the QOF registers (e.g., ethnicity, learning disability) are loaded in [analysis/codelists_demographic.py](analysis/codelists_demographic.py)
- Variables with demographic information (e.g., age, ethnicity) or other variables (e.g., registration status) that are the same across all registers are defined in [analysis/dict_demographic_variables.py](analysis/dict_demographic_variables.py)
- Ethnicity is extracted in a separate study definition [analysis/study_definition_ethnicity.py](analysis/study_definition_ethnicity.py) and joined later with each QOF register
- Commonly used dates (e.g., '*Payment Period Start Date*') are defined in [analysis/config.py](analysis/config.py)

## Use case

New QOF studies should start by using the [OpenSAFELY research template](https://github.com/opensafely/research-template).
The steps outlined blow describe the general workflow:

1. Use the [OpenSAFELY research template](https://github.com/opensafely/research-template) to start your own QOF project
2. Copy all register specific and shared files into your study. For example to use the Asthma register in your study you would need to add:
     - indicator specific files: (i) [analysis/codelists_ast.py](analysis/codelists_ast.py), (ii) [analysis/dict_ast_variables.py](analysis/dict_ast_variables.py), and (iii) [analysis/study_definition_ast_reg.py](analysis/study_definition_ast_reg.py) as well as
     - shared files: (i) [analysis/codelists_demographic.py](analysis/codelists_demographic.py), (ii) [analysis/dict_demographic_variables.py](analysis/dict_demographic_variables.py),() [analysis/study_definition_ethnicity.py](analysis/study_definition_ethnicity.py) and joined later with each QOF register
- Commonly used dates (e.g., '*Payment Period Start Date*') are defined in [analysis/config.py](analysis/config.py)

1. actions 

# About the OpenSAFELY framework

Developers and epidemiologists interested in the framework should review [the OpenSAFELY documentation](https://docs.opensafely.org)
The OpenSAFELY framework is a Trusted Research Environment (TRE) for electronic
health records research in the NHS, with a focus on public accountability and
research quality.
Read more at [OpenSAFELY.org](https://opensafely.org).

# Licences
As standard, research projects have a MIT license. 
