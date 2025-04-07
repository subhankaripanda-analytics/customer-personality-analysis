import pandas as pd

# Load the dataset using tab separator
df = pd.read_csv('.kaggle/marketing_campaign.csv', sep='\t')
# Display basic info
print("Initial Data Overview:\n")
print(df.info())
print("\nFirst 5 rows:\n")
print(df.head())

 #Check for missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing 'Income' with median
df['Income'] = df['Income'].fillna(df['Income'].median())


# Drop duplicates
print("\nDuplicate rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Convert 'Dt_Customer' to datetime format
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True)

# Clean up column names (strip whitespaces)
df.columns = df.columns.str.strip()

# Confirm changes
print("\nCleaned Data Overview:\n")
print(df.info())
print("\nFirst 5 rows after cleaning:\n")
print(df.head())

# Identify categorical columns
categorical_cols = df.select_dtypes(include='object').columns
print("\nCategorical Columns:")
print(categorical_cols)

for col in categorical_cols:
    print(f"\nUnique values in '{col}':")
    print(df[col].unique())

df['Education'] = df['Education'].replace({'2n Cycle': 'Undergraduate'})

df['Marital_Status'] = df['Marital_Status'].replace({
    'Alone': 'Single',
    'Absurd': 'Single',
    'YOLO': 'Single'
})
print("\nCleaned unique values in 'Education':", df['Education'].unique())
print("Cleaned unique values in 'Marital_Status':", df['Marital_Status'].unique())

# Convert text columns to numbers (One-Hot Encoding)
df = pd.get_dummies(df, columns=['Education', 'Marital_Status'], drop_first=True)

# Show result
print("\nShape after encoding:", df.shape)
print("\nNew column names after encoding:")
print(df.columns)

#  Create new feature: Customer age
df['Age'] = 2025 - df['Year_Birth']

#  Create new feature: Total amount spent on products
df['Total_Spend'] = df[['MntWines', 'MntFruits', 'MntMeatProducts',
                        'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)

# Drop 'ID' and 'Year_Birth' since they're no longer needed
df.drop(['ID', 'Year_Birth'], axis=1, inplace=True)

#  Final preview
print("\nFinal cleaned data preview:")
print(df.head())
print("\nFinal shape:", df.shape)

df.to_csv("cleaned_customer_data.csv", index=False)




