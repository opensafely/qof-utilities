
# Define common variables needed across indicators here
# See https://docs.opensafely.org/study-def-tricks/

import pandas as pd
from config import start_date, end_date
from cohortextractor import patients
from codelists import (
    hyp_codes,
    hyp_res_codes,
)

# Define dictionary of variables needed for hypertension register:
# Patients with an unresolved diagnosis of hypertension
hyp_reg_variables = dict(
    # Define variables for hypertension (binary) and associated date
    # HYPLAT_DAT (hyp_lat_date): Date of the most recent hypertension
    # diagnosis up to and including the achievement date.
    hyp_lat=patients.with_these_clinical_events(
        on_or_before="last_day_of_month(index_date)",
        codelist=hyp_codes,
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
    ),
    # Note that this is the same variable description as:
    # HYP_DAT (hypertension_date): Date of the first hypertension
    # diagnosis up to and including the achievement date.
    hyp=patients.with_these_clinical_events(
        on_or_before="last_day_of_month(index_date)",
        codelist=hyp_codes,
        returning="binary_flag",
        find_first_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
    ),
    # Define variables for resolved hypertension (binary) and associated date
    # HYPRES_DAT: Date of the most recent hypertension resolved code recorded
    # after the most recent hypertension diagnosis and up to and including
    # the achievement date.
    hyp_res=patients.with_these_clinical_events(
        on_or_before="last_day_of_month(index_date)",
        codelist=hyp_res_codes,
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
    ),
    # Define hypertension register
    hyp_reg=patients.satisfying(
        """
        # Select patients from the specified population who have a diagnosis
        # of hypertension which has not been subsequently resolved.
        (hyp AND (NOT hyp_res)) OR
        (hyp_res <= hyp)
        """
    ),
)
