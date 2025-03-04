import pandas as pd

# Load Data
file_path = 'data/yelp.csv'
df = pd.read_csv(file_path)

# Check first few rows to confirm date column name
print(df.head())

# Assuming date column is named 'date' (update if different)
df['date'] = pd.to_datetime(df['date'])

# Find Min and Max Dates
start_date = df['date'].min().strftime('%Y-%m-%d')
end_date = df['date'].max().strftime('%Y-%m-%d')

print(f"Date Range Covered: {start_date} to {end_date}")
