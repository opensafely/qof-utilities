from cohortextractor import codelist_from_csv

######################################
## DIABETES
######################################

# Cluster name: DM_COD
# Description: Diabetes diagnosis codes
# SNOMED CT:
dm_cod = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dm_cod.csv",
    system="snomed",
    column="code",
)

# Cluster name: DMRES_COD
# Description: Diabetes resolve codes
# SNOMED CT:
dmres_cod = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dmres_cod.csv",
    system="snomed",
    column="code",
)