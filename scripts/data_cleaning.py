# Step 1 - Import Libraries
import pandas as pd

# Step 2 - Load the Dataset
df = pd.read_csv('data/yelp.csv')

# Step 3 - Quick Check of Data
print("First 5 rows of data:")
print(df.head())

print("\nSummary Information of Dataset:")
print(df.info())

# Step 4 - Decide What to Keep
# We are only interested in 'text' (review text) and 'stars' (rating)
df = df[['text', 'stars']]

# Explanation (for understanding):
# - 'text' = actual customer review
# - 'stars' = customer rating (1 to 5 stars) — this helps us label good vs bad reviews later.

# Step 5 - Check for Missing Data
print("\nMissing Values Check:")
print(df.isnull().sum())

# Step 6 - Save Cleaned Data
df.to_csv('data/yelp_cleaned.csv', index=False)

print("\n✅ Data Cleaning Done! Cleaned file saved as 'data/yelp_cleaned.csv'")
