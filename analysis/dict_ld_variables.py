
# Define common variables needed across indicators here
# See https://docs.opensafely.org/study-def-tricks/

import pandas as pd
from config import start_date, end_date
from cohortextractor import patients
from codelists_ld import (
    ld_codes,
    )

# Define dictionary of variables needed for learning disability register:
ld_reg_variables = dict(
    ld=patients.with_these_clinical_events(
        ld_codes,
        on_or_before="last_day_of_month(index_date)",
        returning="binary_flag",
        find_last_match_in_period=True,
        include_date_of_match=True,
        date_format="YYYY-MM-DD",
        return_expectations={
            "incidence": 0.01,
        },
    ),
    # Define learning disability register
    # TODO: Check section 3.2.4 Clinical data extraction criteria
    ld_reg=patients.satisfying(
        """
        # Learning disability register: Patients with a learning disability
        ld
        """
    ),
)
