import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Load your cleaned data
df = pd.read_csv("cleaned_customer_data.csv")

# --- Step 1: Reverse One-Hot Encoded Columns --- #
def reverse_one_hot(df, prefix):
    cols = [col for col in df.columns if col.startswith(prefix + "_")]
    df[prefix] = df[cols].idxmax(axis=1).str.replace(prefix + "_", "")
    return df

df = reverse_one_hot(df, 'Education')
df = reverse_one_hot(df, 'Marital_Status')

# --- Step 2: Visualizations --- #

# Age Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.tight_layout()
plt.show()

# Income Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['Income'], bins=20, kde=True)
plt.title('Income Distribution')
plt.xlabel('Income')
plt.tight_layout()
plt.show()

# Education vs Total Spend
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x='Education', y='Total_Spend')
plt.title('Total Spend by Education Level')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Marital Status vs Total Spend
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x='Marital_Status', y='Total_Spend')
plt.title('Total Spend by Marital Status')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Number of Web Visits per Month
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='NumWebVisitsMonth')
plt.title('Monthly Web Visits Distribution')
plt.xlabel('Web Visits per Month')
plt.tight_layout()
plt.show()

# --- Step 3: Save Final Dataset (Optional) --- #
df.to_csv("final_customer_data.csv", index=False)


