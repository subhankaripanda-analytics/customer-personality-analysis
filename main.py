import pandas as pd

# Load the CSV file
df = pd.read_csv('.kaggle/marketing_campaign.csv')

# Sort by a specific column (example: Income in descending order)
df_sorted = df.sort_values(by='Income', ascending=False)

# Display the top rows in a clean table format
print(df_sorted.to_string(index=False))  # index=False makes it cleaner

