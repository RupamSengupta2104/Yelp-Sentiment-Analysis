import pandas as pd

df = pd.read_csv('data/yelp_with_sentiment.csv')
print(df[['sentiment', 'cleaned_text']].head(30))
