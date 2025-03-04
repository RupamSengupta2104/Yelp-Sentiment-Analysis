import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'data/yelp.csv'
df = pd.read_csv(file_path)

# Ensure date is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Assign sentiment
def assign_sentiment(stars):
    if stars >= 4:
        return 'Positive'
    elif stars == 3:
        return 'Neutral'
    else:
        return 'Negative'

df['sentiment'] = df['stars'].apply(assign_sentiment)

# Set date as index and resample to weekly
df.set_index('date', inplace=True)
weekly_sentiment = df.resample('W')['sentiment'].value_counts().unstack(fill_value=0)

# Calculate 4-week moving average for smoother trend
weekly_sentiment_ma = weekly_sentiment.rolling(window=4).mean()

# Plotting
plt.figure(figsize=(12, 6))
for sentiment in weekly_sentiment.columns:
    plt.plot(weekly_sentiment_ma.index, weekly_sentiment_ma[sentiment], label=sentiment)

plt.title('Weekly Sentiment Trend (4-Week Moving Average)')
plt.xlabel('Date')
plt.ylabel('Number of Reviews')
plt.legend()
plt.grid(True)

# Save plot to reports
plt.savefig('reports/sentiment_weekly_trend.png')
plt.show()

print("✅ Weekly trend plot saved to reports/sentiment_weekly_trend.png")
