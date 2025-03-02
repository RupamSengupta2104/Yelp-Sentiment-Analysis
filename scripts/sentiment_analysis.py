import pandas as pd
import nltk
from nltk.corpus import opinion_lexicon

# Download lexicon if not already downloaded
nltk.download('opinion_lexicon')

# Load positive and negative words from nltk's opinion lexicon
positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())

# Load the processed data
df = pd.read_csv('data/yelp_processed.csv')

def get_sentiment(text):
    words = text.split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)

    if pos_count > neg_count:
        return 'Positive'
    elif neg_count > pos_count:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to each review
df['sentiment'] = df['cleaned_text'].apply(get_sentiment)

# Save to a new file
df.to_csv('data/yelp_with_sentiment.csv', index=False)

print("Sentiment analysis completed! File saved as 'data/yelp_with_sentiment.csv'")
