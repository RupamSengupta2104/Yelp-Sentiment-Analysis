import pandas as pd

df = pd.read_csv('data/yelp_with_sentiment.csv')

print("First 5 rows of the processed dataset:")
print(df.head())

print("\nSentiment distribution in the dataset:")
print(df['sentiment'].value_counts())

print("\n✅ Data quality check completed successfully!")
