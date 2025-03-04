import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import STOPWORDS

# Load the processed data with sentiment column
df = pd.read_csv('data/yelp_with_sentiment.csv')

# Check unique sentiments (just for safety check - can remove later)
print("Unique sentiment values:", df['sentiment'].unique())

# Function to get top words for a given sentiment
def get_top_words(sentiment, top_n=20):
    filtered_reviews = df[df['sentiment'] == sentiment]['cleaned_text'].dropna()
    all_words = " ".join(filtered_reviews).split()
    all_words = [word for word in all_words if word.lower() not in STOPWORDS]
    
    word_counts = Counter(all_words)
    return word_counts.most_common(top_n)

# Function to plot and save top words barplot
def plot_top_words(sentiment, skip_if_empty=True):
    common_words = get_top_words(sentiment)
    
    if skip_if_empty and len(common_words) == 0:
        print(f"No valid words found for sentiment: {sentiment}. Skipping plot.")
        return

    words, counts = zip(*common_words)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=list(words), y=list(counts), palette='viridis')
    plt.xticks(rotation=45)
    plt.title(f'Top {len(words)} Words in {sentiment.capitalize()} Reviews')
    plt.tight_layout()

    # Save the plot into images folder
    plot_path = f'images/top_words_{sentiment.lower()}.png'
    plt.savefig(plot_path, dpi=300)
    print(f'Saved plot to: {plot_path}')
    plt.show()

# Run analysis only for Positive and Negative (skip Neutral for now)
plot_top_words('Positive')
plot_top_words('Negative')
