
# QOF registers in OpenSAFELY

The purpose of this repository is to provide code which replicates [QOF business rules](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof) for condition registers. This code is intended for researchers to copy and use in their own OpenSAFELY study repositories, and can be used for further analyses on monthly QOF trends and breakdowns by relevant variables. 

This repo also contains [wikis](https://github.com/opensafely/qof-utilities/wiki) with documentation about how we have implemented the QOF business rules. Please feel free to contribute to it, and the [discussion](https://github.com/opensafely/qof-utilities/discussions) and raise any [issues](https://github.com/opensafely/qof-utilities/issues) - this resource is in development and we welcome all contributions to help others use it.

We have designed this repo and the instructions below for people who are familiar with OpenSAFELY and who have completed the [OpenSAFELY Getting Started tutorial](https://docs.opensafely.org/getting-started/). 

## Contents of this repo

This repo currently contains resources for the creation of QOF registers for the following clinical domains in OpenSAFELY

- Asthma (AST_REG)

- Diabetes (DM_REG)

- Hypertension (HYP_REG)

- Learning disability (LD_REG)

- Palliative Care (PC_REG)

- Stroke / TIA (STIA_REG)

To create a QOF register in your own OpenSAFELY study you will need to copy from this repo both *specific files for that register* and *shared register files*. Details of both of these types of files can be found below. 

### Specific files needed for each register

Files specific to a register have a suffix denoting which register they relate to, for example, hypertension register files have the suffix _hyp_ or _hyp_reg_. We will use the hypertension register as an example below, for all other registers use the files with the relevant suffix.

- The *register specific codelist* python file needed for the QOF register (e.g., hypertension) is in the [analysis/codelists_hyp.py](analysis/codelists_hyp.py) file.

- The QOF business rules have been coded into individual variables (such as diagnosis of hypertension) and combined into a register variable (such diagnosis of unresolved hypertension) within a *register specific variable dictionary* (see [OpenSAFELY programming tricks](https://docs.opensafely.org/study-def-tricks/#sharing-common-study-definition-variables)). You can identify the final register variable in the dictionary as it is composed by combining the individual variables using the _patients.satisfying()_ function, and has the naming convention _[condition tag]_reg_. The variable dictionary for implementing the hypertension register are here [analysis/dict_hyp_variables.py](analysis/dict_hyp_variables.py)). 

- The *register specific study definition* makes use of the variables defined in the register specific variable dictionary and the demographic dictionary (see below). This file defines the population list size in the _population_ variable, and generates the measures using the register specific register variable. The register specific study definition file is here [analysis/study_definition_hyp_reg.py](analysis/study_definition_hyp_reg.py)).

### Shared files across all registers

- The *demographic and register specific codelist* text contains all codelists specified in the QOF business rules required for the conditions covered in this repo so far. The codelists can be found on OpenCodelists under [NHSD Primary Care Domain Refsets]([https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/](https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/)). The file containing all relevant codelists for QOF register studies on OpenSAFELY is here [codelists/codelists.txt](codelists/codelists.txt). 

For more information on the codelists used to define population and demographic variables, see the wiki article [‘Standard parameters and variables in QOF register studies’](https://github.com/opensafely/qof-utilities/wiki/Standard-parameters-and-variables-in-QOF-register-studies).

- The *demographic and population breakdown codelist* python file, used for breakdowns of the QOF registers (e.g., ethnicity. learning disability) is in the [analysis/codelists_demographic.py](analysis/codelists_demographic.py) file.

- The *demographic and population variable dictionary* contains variables relating to demographics (e.g., age, ethnicity), specific cohorts (e.g., care home status) and other variables (e.g.,GP practice registration status). These are the same across all, more information on the codelists used can be found [here.](https://github.com/opensafely/qof-utilities/wiki/Standard-parameters-and-variables-in-QOF-register-studies) The demographic and population variable dictionary file is here [analysis/dict_demographic_variables.py](analysis/dict_demographic_variables.py).

- Within OpenSAFELY studies ethnicity is usually extracted in a separate study definition and joined later with each QOF register. The *ethnicity study definition* can be found here [analysis/study_definition_ethnicity.py](analysis/study_definition_ethnicity.py).

- The *project.yaml file for all register registers* includes actions for all condition specific registers. To use this file, you will need to copy across to your study’s project.yaml file the actions relating to your specific condition register of interest. Actions relating to specific register have a suffix with the condition tag. The actions associated with all registers are in this file [project.yaml](project.yaml)

## Using this repo

To recreate the QOF register for one of the registers above follow the following steps:



1. Use the [OpenSAFELY research template](https://github.com/opensafely/research-template) to start your own OpenSAFELY QOF project and add it to the wiki list of repos using this code. 
2. Copy over the relevant register specific files

- The register specific codelist python file

- The register specific variable dictionary

- The register specific study definition



3. Copy over the shared files for all registers (excluding the _project.yaml_ file, this is covered in the step below)

- The demographic and register specific codelist text file

- The demographic and population breakdown codelist python file

- The demographic and population variable dictionary

- The ethnicity study definition 



4. Copy over only the actions relating to your register of interest, from the _project.yaml_ file into the _project.yaml_ file in your research repo. These consist of: 

_- generate_study_population_[XXX]_reg_

_- generate_study_population_ethnicity_



5. If relevant to your analysis, adjust the _config.py_ file and the _project.yaml_ file in your repo to cover the time period and level of return of interest. For analyses looking at trends in register prevalence before and during the pandemic we would recommend a start date of 1/03/2022 and the latest month as the end date. In the _project.yaml_ file, this will be written in the _generate_study_population_[XXX]_reg_ action (which creates the register) as ‘--index-date-range "2021-04-01 to 2022-03-01 by month" ‘.

## Register specific files

The following list shows the condition specific files required to create a QOF register

- Asthma (AST_REG)

  - Codelists: [analysis/codelists_ast.py](analysis/codelists_ast.py)

  - Variable definitions: [analysis/dict_ast_variables.py](analysis/dict_ast_variables.py)

  - Study definition and measures: [analysis/study_definition_ast_reg.py](analysis/study_definition_ast_reg.py)

- Learning disability (LD_REG)

  - Codelists: [analysis/codelists_ls.py](analysis/codelists_ls.py)

  - Variable definitions: [analysis/dict_ls_variables.py](analysis/dict_ls_variables.py)

  - Study definition and measures: [analysis/study_definition_ls_reg.py](analysis/study_definition_ls_reg.py)

- Hypertension (HYP_REG)

  - Codelists: [analysis/codelists_hyp.py](analysis/codelists_hyp.py)

  - Variable definitions: [analysis/dict_hyp_variables.py](analysis/dict_hyp_variables.py)

  - Study definition and measures: [analysis/study_definition_hyp_reg.py](analysis/study_definition_hyp_reg.py)

- Palliative Care (PC_REG)

  - Codelists: [analysis/codelists_pc.py](analysis/codelists_pc.py)

  - Variable definitions: [analysis/dict_pc_variables.py](analysis/dict_pc_variables.py)

  - Study definition and measures: [analysis/study_definition_pc_reg.py](analysis/study_definition_pc_reg.py)

- Diabetes (DM_REG)

  - Codelists: [analysis/codelists_dm.py](analysis/codelists_dm.py)

  - Variable definitions: [analysis/dict_dm_variables.py](analysis/dict_dm_variables.py)

  - Study definition and measures: [analysis/study_definition_dm_reg.py](analysis/study_definition_dm_reg.py)

- Stroke / TIA (STIA_REG)

  - Codelists: [analysis/codelists_stia.py](analysis/codelists_stia.py)

  - Variable definitions: [analysis/dict_stia_variables.py](analysis/dict_stia_variables.py)

  - Study definition and measures: [analysis/study_definition_stia_reg.py](analysis/study_definition_stia_reg.py)

## Worked example

The steps outlined below describe the workflow for one example register, asthma, on how to use the resources in this repository for your study:

1. Use the [OpenSAFELY research template](https://github.com/opensafely/research-template) to start your own QOF project and add it to the wiki list of repos using this code. 

2. Copy all asthma register specific

     - Asthma specific files:

        - [analysis/codelists_ast.py](analysis/codelists_ast.py)

        - [analysis/dict_ast_variables.py](analysis/dict_ast_variables.py)

        - [analysis/study_definition_ast_reg.py](analysis/study_definition_ast_reg.py)

3. Copy over the shared files (excluding _project.yaml_ actions)

     - Shared files:

        - [codelists/codelists.txt](codelists/codelists.txt)

        - [analysis/codelists_demographic.py](analysis/codelists_demographic.py)

        - [analysis/dict_demographic_variables.py](analysis/dict_demographic_variables.py)

        - [analysis/study_definition_ethnicity.py](analysis/study_definition_ethnicity.py)

3. Finally you need to specify the actions that are needed for the asthma register in the [project.yaml](project.yaml) for your project. 

   For example, asthma actions required to create the register:

     -  _generate_study_population_ast_reg_: to extract the study population for the asthma register

     -  _generate_study_population_ethnicity_: to extract ethnicity for the asthma register population (Note - this action is not register specific and is required for all registers)

     -  _join_ethnicity_ast_reg_: to join ethnicity to the asthma register

     -  _generate_measures_ast_reg_: to generate measures (percentage prevalence for the total population and breakdown by demographic variables)

# About the OpenSAFELY framework

Developers and epidemiologists interested in the framework should review [the OpenSAFELY documentation](https://docs.opensafely.org)

The OpenSAFELY framework is a Trusted Research Environment (TRE) for electronic

health records research in the NHS, with a focus on public accountability and

research quality.

Read more at [OpenSAFELY.org](https://opensafely.org).

# Licences

As standard, research projects have a MIT license. 
