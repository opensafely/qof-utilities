
# Define common variables needed across indicators here
# See https://docs.opensafely.org/study-def-tricks/

import pandas as pd
from config import start_date, end_date
from cohortextractor import patients
from codelists_dm import (
    dm_cod,
    dmres_cod,
)

# Define dictionary of variables needed for diabetes register:
# Patients with an unresolved diagnosis of diabetes
dm_reg_variables = dict(

    dm_diag=patients.with_these_clinical_events(
        on_or_before="last_day_of_month(index_date)",
        codelist=dm_cod,
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
    ),
    # Define variables for resolved diabetes (binary) and associated date
    # DMRES_DAT: Date of the most recent diabetes resolved code recorded
    # after the most recent diabetes diagnosis and up to and including
    # the achievement date.
    diabetes_resolved=patients.with_these_clinical_events(
        on_or_before="last_day_of_month(index_date)",
        codelist=dmres_cod,
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
    ),

    age_dm_reg=patients.age_as_of(
         "last_day_of_month(index_date) + 1 day",
         return_expectations={
             "rate": "universal",
             "int": {"distribution": "population_ages"},
         },
    ),

    # Define diabetes register
    diabetes=patients.satisfying(
        """
        # Select patients from the specified population who have a diagnosis
        # of diabetes which has not been subsequently resolved.
        (dm_diag AND NOT diabetes_resolved 
        AND age_dm_reg > 17) 
        
        OR
        
        (diabetes_resolved_date < dm_diag_date
        AND age_dm_reg > 17)
        """
    ),
)