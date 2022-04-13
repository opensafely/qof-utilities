from cohortextractor import codelist_from_csv

# Cluster name: LD_COD
# Description: Learning disability (LD) codes
# SNOMED CT: ^999002611000230109
ld_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-ld_cod.csv",
    system="snomed",
    column="code",
)
