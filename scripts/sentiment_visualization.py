import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sentiment data
df = pd.read_csv('data/yelp_with_sentiment.csv')

# Set plot style
sns.set_style("whitegrid")

# Plot sentiment distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='sentiment', data=df, palette='pastel')

# Add title and labels
plt.title('Sentiment Distribution in Yelp Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Count')

# Save the plot
plt.savefig('images/sentiment_distribution.png', bbox_inches='tight', dpi=300)
plt.show()

print("Sentiment distribution plot saved as 'images/sentiment_distribution.png'")
