import pandas as pd

# File path to dataset inside 'data' folder
file_path = 'data/yelp.csv'

# Load the data
df = pd.read_csv(file_path)

# Quick preview
print("First 5 Rows of Data:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nColumn Names:")
print(df.columns)

print("\nNumber of Rows & Columns:", df.shape)

print("\nSample Review Text:")
print(df['text'].sample(1).values[0])
