# Using OpenSAFELY to analyse QOF indicators

## Abstract

The goal of this repo is to help a research go from the Opensafely research template to Quality and Outcomes Framework ([QOF](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof)) results.

# QOF Rule Complexity

> This table describes the "complexity" of the QOF indicators, see code on the [doc_parsing](https://github.com/opensafely/qof-utilities/tree/doc_parsing) branch. Note that the "line count" is currently still :warning: **WORK IN PROGRESS** :warning:.
	
Clinical Area                           |   Indicators |   Rule Count |   Line Count |
|:----------------------------------------|-------------:|-------------:|-------------:|
| Diabetes_v46.0.docx                     |            9 |           97 |          169 |
| Mental_health_v46.2.docx                |            7 |           58 |           81 |
| HF_v46.0.docx                           |            5 |           48 |           30 |
| Asthma_v46.0.docx                       |            4 |           43 |          110 |
| Stroke_v46.0.docx                       |            4 |           31 |           99 |
| CHD_v46.0.docx                          |            4 |           30 |           88 |
| Vaccination and Immunisation_v46.0.docx |            4 |           16 |           36 |
| Smoking_v46.0.docx                      |            3 |           32 |           81 |
| Cancer_v46.1.docx                       |            3 |           21 |           22 |
| Hypertension_v46.0.docx                 |            3 |           20 |           42 |
| COPD_v46.0.docx                         |            3 |           19 |           26 |
| Atrial_Fibrillation_v46.0.docx          |            3 |           19 |           33 |
| Cervical_Screening_v46.0.docx           |            2 |           17 |           19 |
| Dementia_v46.0.docx                     |            2 |            8 |           14 |
| Rheumatoid_Arthritis_v46.0.docx         |            2 |            6 |            7 |
| Non-diabetic_Hyperglycaemia_v46.0.docx  |            1 |           10 |           23 |
| Depression_v46.0.docx                   |            1 |            9 |           10 |
| Blood_Pressure_v46.0.docx               |            1 |            5 |            5 |
| PAD_v46.0.docx                          |            1 |            0 |            0 |
| CKD_v46.0.docx                          |            1 |            0 |            0 |
| Palliative_Care_v46.0.docx              |            1 |            0 |            0 |
| Obesity_v46.0.docx                      |            1 |            0 |            0 |
| Learning_Disability_v46.0.docx          |            1 |            0 |            0 |
| Osteoporosis_v46.0.docx                 |            1 |            0 |            0 |
| Epilepsy_v46.0.docx                     |            1 |            0 |            0 |
| **Total**                               |           68 |              |              |

## Motivation

A couple of us are working on QOF indicators .
There are 25 clinical areas (e.g., Asthma, Hypertension) with 68 indicators, some with complex rules.
A .zip folder with all rules can be found [here](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/quality-and-outcome-framework-qof-business-rules/qof-business-rules-v46.0-2021-2022-baseline-release). 

We thought that organising our QOF developments (while still learning the general case) using a single GitHub repo (not a GitHub template) with (1) shared utility functions, (2) documentation on starting from the research template, and  (3) ongoing discussions would help to:

- Collect and discuss general issues with QOF (project specific issues will live in their respective repo)
- Guide decision making towards which aspects could potentially become reusable actions, go into a shared library, or are project specific and need to be guided by detailed documentation

## Aim

This repo contains resources, discussion, and issues surrounding the use of OpenSafely to assess the impact of the pandemic on routine care through the assessment of the Quality and Outcomes Framework ([QOF](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof)).

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
