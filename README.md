# Using OpenSAFELY to analyse QOF indicators

## Abstract

The goal of this repository is to help a researcher build on the OpenSAFELY [research-template](https://github.com/opensafely/research-template) to investigate montly changes in Quality and Outcomes Framework ([QOF](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof)) indicators.

This repo contains resources, discussion, and issues surrounding the use of OpenSAFELY to assess the impact of the pandemic on routine care through the assessment of the Quality and Outcomes Framework ([QOF](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof)).

## Motivation

A couple of us are working on QOF indicators .
There are 25 clinical areas (e.g., Asthma, Hypertension) with 68 indicators, some with complex rules.
A .zip folder with all rules can be found [here](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/quality-and-outcome-framework-qof-business-rules/qof-business-rules-v46.0-2021-2022-baseline-release). 

We thought that organising our QOF developments (while still learning the general case) using a single GitHub repo (not a GitHub template) with (1) shared utility functions, (2) documentation on starting from the research template, and  (3) ongoing discussions would help to:

- Collect and discuss general issues with QOF (project specific issues will live in their respective repo)
- Guide decision making towards which aspects could potentially become reusable actions, go into a shared library, or are project specific and need to be guided by detailed documentation

## QOF Rule Complexity

This table describes potential "complexity" metrics for the QOF indicators, see code on the [doc_parsing](https://github.com/opensafely/qof-utilities/tree/doc_parsing) branch.
> :warning: **IN PROGRESS, NUMBERS NOT FINAL** includes register as an indicator for all clinical areas but excludes the Vaccination "Cohorts"
	
| Clinical Area                           |   Indicators |   Rule Count |   Line Count |
|:----------------------------------------|-------------:|-------------:|-------------:|
| Diabetes_v46.0.docx                     |            9 |           99 |          172 |
| Mental_health_v46.2.docx                |            7 |           59 |           82 |
| HF_v46.0.docx                           |            5 |           49 |           32 |
| Asthma_v46.0.docx                       |            4 |           46 |          114 |
| Smoking_v46.0.docx                      |            4 |           33 |          101 |
| Stroke_v46.0.docx                       |            4 |           32 |          101 |
| CHD_v46.0.docx                          |            4 |           31 |           89 |
| Vaccination and Immunisation_v46.0.docx |            4 |           16 |           36 |
| COPD_v46.0.docx                         |            3 |           23 |           35 |
| Cancer_v46.1.docx                       |            3 |           22 |           23 |
| Hypertension_v46.0.docx                 |            3 |           21 |           44 |
| Atrial_Fibrillation_v46.0.docx          |            3 |           20 |           35 |
| Cervical_Screening_v46.0.docx           |            3 |           19 |           22 |
| Non-diabetic_Hyperglycaemia_v46.0.docx  |            2 |           13 |           28 |
| Depression_v46.0.docx                   |            2 |           11 |           13 |
| Dementia_v46.0.docx                     |            2 |            9 |           15 |
| Rheumatoid_Arthritis_v46.0.docx         |            2 |            7 |            9 |
| Blood_Pressure_v46.0.docx               |            1 |            5 |            5 |
| CKD_v46.0.docx                          |            1 |            2 |            5 |
| Epilepsy_v46.0.docx                     |            1 |            2 |            4 |
| PAD_v46.0.docx                          |            1 |            1 |            1 |
| Palliative_Care_v46.0.docx              |            1 |            1 |            2 |
| Obesity_v46.0.docx                      |            1 |            1 |            3 |
| Learning_Disability_v46.0.docx          |            1 |            1 |            1 |
| Osteoporosis_v46.0.docx                 |            1 |            1 |            7 |

## Whats in this repo?

- Code
  - Word `.docx` parsing
  - Jupyter example notebook with placeholders
  - Analysis and plotting code
- [Discussions](https://github.com/opensafely/qof-utilities/discussions)
- [Issues](https://github.com/opensafely/qof-utilities/issues)
- [Wiki](https://github.com/opensafely/qof-utilities/wiki)
  - Workflow (from research template to qof research project)
  - QOF specific code snippets for study definitions

Multiple sets of common variables (register, demographics)
