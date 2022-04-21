
# Define common variables needed across indicators here
# See https://docs.opensafely.org/study-def-tricks/

import pandas as pd
from config import start_date, end_date
from cohortextractor import patients
from codelists_pc import (
    palcare_codes,
    palcareni_codes,
    )

# Define dictionary of variables needed for Palliative Care register:
pc_reg_variables = dict(
    # Date of the most recent palliative care code in the patient’s record
    # between 1 April 2008 and the achievement date (inclusive).
    pal_care=patients.with_these_clinical_events(
        palcare_codes,
        between=["2008-04-01", "last_day_of_month(index_date)"],
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # Date of the first code for palliative care no longer indicated in the
    # patient’s record following their latest palliative care code and up to
    # and including the achievement date.
    pal_care_ni=patients.with_these_clinical_events(
        palcareni_codes,
        on_or_before="last_day_of_month(index_date)",
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # Define Palliative Care register
    # TODO: Check section 3.2.4 Clinical data extraction criteria
    pal_care_reg=patients.satisfying(
        """
        # Palliative Care register:
        # Patients who have been identified as requiring palliative care
        (pal_care AND (NOT pal_care_ni)) OR
        (
            (pal_care AND pal_care_ni) AND
            (pal_care_ni_date <= pal_care_date)
        )

        """
    ),
)
