from cohortextractor import codelist_from_csv

# Cluster name: PALCARE_COD
# Description: Palliative care codes
# SNOMED CT: ^999009771000230104
palcare_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-palcare_cod.csv",
    system="snomed",
    column="code",
)
# Cluster name: PALCARENI_COD
# Description: Palliative care not clinically indicated codes
# SNOMED CT: ^999009931000230103
palcareni_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-palcareni_cod.csv",
    system="snomed",
    column="code",
)
