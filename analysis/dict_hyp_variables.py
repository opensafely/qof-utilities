
# Define common variables needed across indicators here
# See https://docs.opensafely.org/study-def-tricks/

import pandas as pd
from config import start_date, end_date
from cohortextractor import patients
from codelists import (
    hyp_codes,
    hyp_res_codes,
    bp_sys_codes,
    bp_dia_codes,
    ht_max_codes,
    hyp_pca_pu_codes,
    hyp_pca_dec_codes,
    bp_dec_codes,
    hyp_invite_codes,
)

# Define unique list of hypertension codes to set expectations in dummy data
hyp_codes_path = "codelists/nhsd-primary-care-domain-refsets-hyp_cod.csv"
hyp_codes_df = pd.read_csv(hyp_codes_path)
hyp_codes_unique = hyp_codes_df["code"].unique()

# Define dictionary of variables needed for hypertension register:
# Patients with an unresolved diagnosis of hypertension
hyp_reg_variables = dict(
    registered=patients.registered_as_of(
        "last_day_of_month(index_date)",
        return_expectations={"incidence": 0.9},
    ),
    # Define variables for hypertension (binary) and associated date
    # HYPLAT_DAT (hypertension_date): Date of the most recent hypertension
    # diagnosis up to and including the achievement date.
    # Note that this is the same variable description as:
    # HYP_DAT (hypertension_date): Date of the first hypertension
    # diagnosis up to and including the achievement date.
    hypertension=patients.with_these_clinical_events(
        on_or_before="last_day_of_month(index_date)",
        codelist=hyp_codes,
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
    ),
    # Define variables for resolved hypertension (binary) and associated date
    # HYPRES_DAT: Date of the most recent hypertension resolved code recorded
    # after the most recent hypertension diagnosis and up to and including
    # the achievement date.
    hypertension_resolved=patients.with_these_clinical_events(
        on_or_before="last_day_of_month(index_date)",
        codelist=hyp_res_codes,
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
    ),
    # Define hypertension register
    # REG_DAT (hypertension_register_date): The most recent date that the
    # patient registered for GMS, where this registration occurred on or
    # before the achievement date
    hypertension_register=patients.satisfying(
        """
        # Select patients from the specified population who have a diagnosis
        # of hypertension which has not been subsequently resolved.
        (hypertension AND (NOT hypertension_resolved)) OR
        (hypertension_resolved_date <= hypertension_date)
        """
    ),
)
