import pandas as pd

# Load the data
file_path = 'data/yelp.csv'  # Make sure file is already in 'data' folder
df = pd.read_csv(file_path)

# Basic Data Info
print("Data Overview:\n")
print(df.info())

# 1. Total number of reviews
print("\nTotal Reviews in Dataset:", len(df))

# 2. Sample 5 random reviews
print("\nRandom 5 Reviews:")
print(df['text'].sample(5).values)

# 3. Unique star ratings and their counts
print("\nUnique Ratings (Stars):")
print(df['stars'].value_counts())

# 4. Average rating across all reviews
print("\nAverage Rating Across All Reviews:", df['stars'].mean())

# 5. Sample 3 positive (5-star) reviews
print("\nExamples of 5-Star Reviews:")
print(df[df['stars'] == 5]['text'].sample(3).values)

# 6. Sample 3 negative (1-star) reviews
print("\nExamples of 1-Star Reviews:")
print(df[df['stars'] == 1]['text'].sample(3).values)
