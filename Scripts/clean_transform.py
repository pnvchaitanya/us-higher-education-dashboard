import pandas as pd

# Load dataset
df = pd.read_csv(
    r'D:\higher_ed_dashboard\raw_data\Most-Recent-Cohorts-Institution.csv',
    encoding='latin-1',
    low_memory=False
)

# Select required columns
columns_we_need = [
    'UNITID', 'INSTNM', 'CITY', 'STABBR', 'CONTROL',
    'PREDDEG', 'UGDS', 'ADM_RATE', 'TUITIONFEE_IN',
    'TUITIONFEE_OUT', 'MD_EARN_WNE_P10', 'MD_EARN_WNE_P6',
    'C150_4', 'C150_L4', 'DEBT_MDN', 'GRAD_DEBT_MDN',
    'PCTPELL', 'PCTFLOAN', 'RET_FT4', 'FEMALE',
    'FIRST_GEN', 'POVERTY_RATE', 'UNEMP_RATE',
    'PCT_WHITE', 'PCT_BLACK', 'PCT_HISPANIC', 'PCT_ASIAN'
]

df = df[columns_we_need]

# Convert numeric columns
numeric_columns = [
    'UGDS', 'ADM_RATE', 'TUITIONFEE_IN', 'TUITIONFEE_OUT',
    'MD_EARN_WNE_P10', 'MD_EARN_WNE_P6', 'C150_4', 'C150_L4',
    'DEBT_MDN', 'GRAD_DEBT_MDN', 'PCTPELL', 'PCTFLOAN',
    'RET_FT4', 'FEMALE', 'FIRST_GEN', 'POVERTY_RATE',
    'UNEMP_RATE', 'PCT_WHITE', 'PCT_BLACK', 'PCT_HISPANIC', 'PCT_ASIAN'
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Create labels
df['CONTROL_LABEL'] = df['CONTROL'].map({
    1: 'Public',
    2: 'Private Nonprofit',
    3: 'Private For-Profit'
})

df['PREDDEG_LABEL'] = df['PREDDEG'].map({
    0: 'Not classified',
    1: 'Certificate',
    2: 'Associate',
    3: 'Bachelor',
    4: 'Graduate'
})

# Combine graduation rates
df['GRAD_RATE'] = df['C150_4'].combine_first(df['C150_L4'])

# Filter invalid data
df = df[df['PREDDEG'] != 0]
df = df[df['UGDS'] > 0]

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Rename columns (business-friendly names)
df = df.rename(columns={
    'unitid': 'institution_id',
    'instnm': 'institution_name',
    'stabbr': 'state',
    'ugds': 'enrollment',
    'adm_rate': 'admission_rate',
    'tuitionfee_in': 'tuition_in_state',
    'tuitionfee_out': 'tuition_out_state',
    'md_earn_wne_p10': 'median_earnings_10yr',
    'md_earn_wne_p6': 'median_earnings_6yr',
    'debt_mdn': 'median_debt',
    'grad_debt_mdn': 'grad_median_debt',
    'pctpell': 'pct_pell_grant',
    'pctfloan': 'pct_federal_loan',
    'ret_ft4': 'retention_rate',
    'female': 'pct_female',
    'first_gen': 'pct_first_gen',
    'pct_white': 'pct_white',
    'pct_black': 'pct_black',
    'pct_hispanic': 'pct_hispanic',
    'pct_asian': 'pct_asian',
    'grad_rate': 'graduation_rate'
})

# Drop original graduation columns (clean dataset)
df = df.drop(columns=['c150_4', 'c150_l4'])

# Remove rows with critical missing values
df = df.dropna(subset=[
    'graduation_rate',
    'tuition_in_state',
    'median_earnings_10yr',
    'grad_median_debt'
])

# Create ROI metric (important for BI)
df['roi'] = df['median_earnings_10yr'] / df['tuition_in_state']

# Final check
print(" Final Dataset Shape:", df.shape)
print("\n Sample Data:")
print(df.head(5))

print("\n Remaining Missing Values:")
print(df.isnull().sum())

# Save cleaned dataset
output_path = r'D:\higher_ed_dashboard\cleaned_data\cleaned_institutions.csv'
df.to_csv(output_path, index=False)

print(f"\n Cleaned file saved successfully at: {output_path}")