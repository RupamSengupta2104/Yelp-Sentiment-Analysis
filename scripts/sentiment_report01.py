import pandas as pd

# Load data
file_path = 'data/yelp.csv'
df = pd.read_csv(file_path)

# Function to classify sentiment
def assign_sentiment(stars):
    if stars >= 4:
        return 'Positive'
    elif stars == 3:
        return 'Neutral'
    else:
        return 'Negative'

df['sentiment'] = df['stars'].apply(assign_sentiment)

# Summary Table Calculation
summary_table = df['sentiment'].value_counts().reset_index()
summary_table.columns = ['Sentiment', 'Count']
summary_table['Percentage'] = (summary_table['Count'] / summary_table['Count'].sum()) * 100

# Display and save summary table
print(summary_table)

summary_table.to_csv('reports/sentiment_summary.csv', index=False)
print("✅ Sentiment summary saved to reports/sentiment_summary.csv")
