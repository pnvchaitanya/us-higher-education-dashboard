import pandas as pd

df = pd.read_csv('D:/higher_ed_dashboard/cleaned_data/cleaned_institutions.csv')

dim_institution = df[[
'institution_id',
'institution_name',
'city',
'state',
'control',
'control_label',
'preddeg',
'preddeg_label'
]].copy()

dim_institution = dim_institution.drop_duplicates(subset='institution_id')

dim_location = df[[
'state'
]].drop_duplicates().copy()

dim_location['location_id'] = range(1, len(dim_location) + 1)

dim_location = dim_location[['location_id', 'state']]

# merge location into dim_institution
dim_institution = dim_institution.merge(dim_location, on='state', how='left')

dim_institution.to_csv('D:/higher_ed_dashboard/cleaned_data/dim_institution.csv', index=False)
print("dim_institution saved:", dim_institution.shape)

dim_location.to_csv('D:/higher_ed_dashboard/cleaned_data/dim_location.csv', index=False)
print("dim_location saved:", dim_location.shape)

# merge location into main df (THIS WAS MISSING)
df = df.merge(dim_location, on='state', how='left')

fact_institutions = df[[
'institution_id',
'location_id',
'enrollment',
'admission_rate',
'tuition_in_state',
'tuition_out_state',
'median_earnings_10yr',
'median_earnings_6yr',
'graduation_rate',
'median_debt',
'grad_median_debt',
'pct_pell_grant',
'pct_federal_loan',
'retention_rate',
'pct_female',
'pct_first_gen',
'poverty_rate',
'unemp_rate',
'pct_white',
'pct_black',
'pct_hispanic',
'pct_asian'
]].copy()

fact_institutions.to_csv('D:/higher_ed_dashboard/cleaned_data/fact_institutions.csv', index=False)
print("fact_institutions saved:", fact_institutions.shape)

print("\nAll files saved successfully in cleaned_data folder")
print("\nYour star schema tables are:")
print("1. dim_institution.csv - describes each school")
print("2. dim_location.csv - state level info")
print("3. fact_institutions.csv - all the numbers and metrics")