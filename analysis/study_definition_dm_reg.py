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

        # Diabetes list size age restriction
        age > 17
        """,
    ),
    # Include diabetes variables
    **dm_reg_variables,
    # Include demographic variables
    **demographic_variables,
)

# Create default measures
measures = [
    Measure(
        id="dm_population_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["population"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_practice_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["practice"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_age_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["age_band"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_sex_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["sex"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_imd_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["imd"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_region_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["region"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_ethnicity_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["ethnicity"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_learning_disability_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["learning_disability"],
        small_number_suppression=True,
    ),
    Measure(
        id="dm_care_home_rate",
        numerator="diabetes",
        denominator="population",
        group_by=["care_home"],
        small_number_suppression=True,
    ),
]