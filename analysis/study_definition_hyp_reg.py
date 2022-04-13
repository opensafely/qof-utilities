from cohortextractor import StudyDefinition, patients, Measure

import json
import pandas as pd

# Import dates and codelists
from config import start_date, end_date
from codelists_hyp import hyp_codes, hyp_res_codes

# Import shared variable dictionaries
from dict_hyp_variables import hyp_reg_variables
from dict_demographic_variables import demographic_variables

study = StudyDefinition(
    index_date=start_date,
    default_expectations={
        "date": {"earliest": start_date, "latest": end_date},
        "rate": "uniform",
        "incidence": 0.5,
    },
    population=patients.satisfying(
        """
        # Define general population parameters
        (NOT died) AND
        (sex = 'F' OR sex = 'M') AND
        (age_band != 'missing') AND

        # Define GMS registration status
        gms_reg_status AND

        # Define Hypertension register
        hyp_reg
        """,
    ),
    # Include hypertension and demographic variable dictionaries
    **hyp_reg_variables,
    **demographic_variables,
)

# Create hypertension register (hyp_reg) measures
measures = [
    Measure(
        id="hyp_reg_population_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["population"],
        small_number_suppression=True,
    ),
    Measure(
        id="hyp_reg_practice_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["practice"],
        small_number_suppression=True,
    ),
    Measure(
        id="hyp_reg_age_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["age_band"],
        small_number_suppression=True,
    ),
    Measure(
        id="hyp_reg_sex_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["sex"],
        small_number_suppression=True,
    ),
    Measure(
        id="hyp_reg_imd_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["imd"],
        small_number_suppression=True,
    ),
    Measure(
        id="hyp_reg_region_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["region"],
        small_number_suppression=True,
    ),
    Measure(
        id="hyp_reg_ethnicity_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["ethnicity"],
        small_number_suppression=True,
    ),
    Measure(
        id="hyp_reg_learning_disability_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["learning_disability"],
        small_number_suppression=True,
    ),
    Measure(
        id="hyp_reg_care_home_rate",
        numerator="hyp_reg",
        denominator="population",
        group_by=["care_home"],
        small_number_suppression=True,
    ),
]
