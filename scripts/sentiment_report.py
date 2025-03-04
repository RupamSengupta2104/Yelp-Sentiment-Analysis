import pandas as pd
import matplotlib.pyplot as plt

# Load the data directly
file_path = 'data/yelp.csv'
df = pd.read_csv(file_path)

# Sentiment assignment logic based on stars
def assign_sentiment(stars):
    if stars >= 4:
        return 'positive'
    elif stars == 3:
        return 'neutral'
    else:
        return 'negative'

df['sentiment'] = df['stars'].apply(assign_sentiment)

# Calculate sentiment counts
sentiment_counts = df['sentiment'].value_counts()

# Save sentiment counts as CSV (basic table report)
sentiment_counts.to_csv('reports/sentiment_basic_report.csv')

# Plot sentiment distribution
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind='bar', color=['green', 'orange', 'red'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)

# Save the plot to reports folder
plt.savefig('reports/sentiment_distribution_plot.png')

print("Basic sentiment report and plot saved to 'reports' folder.")
