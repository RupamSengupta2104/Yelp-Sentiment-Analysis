import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('data/yelp.csv')

# Parse date correctly (assuming format in file is YYYY-MM-DD)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Function to assign sentiment based on stars
def assign_sentiment(stars):
    if stars >= 4:
        return 1  # Positive
    elif stars == 3:
        return 0  # Neutral
    else:
        return -1  # Negative

# Apply sentiment assignment
df['sentiment'] = df['stars'].apply(assign_sentiment)

# Set date as index for resampling
df.set_index('date', inplace=True)

# Weekly average sentiment + 4-week moving average
weekly_trend = df.resample('W')['sentiment'].mean()
weekly_trend_ma4 = weekly_trend.rolling(window=4).mean()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(weekly_trend, label='Weekly Average Sentiment', linestyle='--', color='gray')
plt.plot(weekly_trend_ma4, label='4-Week Moving Average Sentiment', color='blue')
plt.xlabel('Date')
plt.ylabel('Average Sentiment Score')
plt.title('Yelp Sentiment Trend Analysis (4-Week Moving Average)')
plt.legend()

# Save the plot in images folder
plt.savefig('images/sentiment_trend_plot.png', dpi=300)

# Optional - Show plot (can be removed if running in non-interactive mode)
plt.show()
