from cohortextractor import StudyDefinition, patients, Measure

import json
import pandas as pd

from config import start_date, end_date
from codelists_dm import dm_cod, dmres_cod

from dict_dm_variables import dm_reg_variables
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

        # Define GMS registration status
        gms_reg_status AND

        # Diabetes list type age restriction
        dm_list_type_age
        """,
    ),
    # Include demographic variables
    **demographic_variables,
    # Include diabetes variables
    **dm_reg_variables,
    )

# Create default measures
measures = [
    Measure(
        id="dm_reg_population_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["population"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_reg_practice_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["practice"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_reg_age_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["age_band"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_reg_sex_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["sex"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_reg_imd_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["imd"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_reg_region_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["region"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_reg_ethnicity_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["ethnicity"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_reg_learning_disability_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["learning_disability"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_reg_care_home_rate",
        numerator="diabetes_reg",
        denominator="population",
        group_by=["care_home"],
        small_number_suppression=True,
    ),
]
