from cohortextractor import StudyDefinition, patients, Measure

import json
import pandas as pd

# Import dates and codelists
from config import start_date, end_date
from codelists_stia import stia_codes

# Import shared variable dictionaries
from dict_stia_variables import stia_reg_variables
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

        # Define stroke and TIA register
        stia_reg
        """,
    ),
    # Include Stroke and TIA and demographic variable dictionaries
    **stia_reg_variables,
    **demographic_variables,
)

# Create Stroke and TIA register (stia001) measures
measures = [
    Measure(
        id="stia001_population_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["population"],
        small_number_suppression=True,
    ),
    Measure(
        id="stia001_practice_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["practice"],
        small_number_suppression=True,
    ),
    Measure(
        id="stia001_age_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["age_band"],
        small_number_suppression=True,
    ),
    Measure(
        id="stia001_sex_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["sex"],
        small_number_suppression=True,
    ),
    Measure(
        id="stia001_imd_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["imd"],
        small_number_suppression=True,
    ),
    Measure(
        id="stia001_region_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["region"],
        small_number_suppression=True,
    ),
    Measure(
        id="stia001_ethnicity_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["ethnicity"],
        small_number_suppression=True,
    ),
    Measure(
        id="stia001_learning_disability_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["learning_disability"],
        small_number_suppression=True,
    ),
    Measure(
        id="stia001_care_home_rate",
        numerator="stia_reg",
        denominator="population",
        group_by=["care_home"],
        small_number_suppression=True,
    ),
]
