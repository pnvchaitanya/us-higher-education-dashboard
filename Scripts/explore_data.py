import pandas as pd

with open(r'D:\higher_ed_dashboard\raw_data\Most-Recent-Cohorts-Institution.csv', encoding='latin-1') as d:
    df = pd.read_csv(d)

print("Shape of dataset:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)