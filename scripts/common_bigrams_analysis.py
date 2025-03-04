import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import re
from nltk.corpus import stopwords
from nltk.util import ngrams
from wordcloud import WordCloud

# Load Data
df = pd.read_csv('data/yelp.csv')

# Basic Preprocessing
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word not in stop_words]
    return words

df['cleaned_tokens'] = df['text'].apply(clean_text)

# Generate Bigrams
all_bigrams = []
for tokens in df['cleaned_tokens']:
    bigrams = list(ngrams(tokens, 2))
    all_bigrams.extend(bigrams)

# Count Most Common Bigrams
bigram_counts = Counter(all_bigrams)
common_bigrams = bigram_counts.most_common(20)

# Visualization
bigram_df = pd.DataFrame(common_bigrams, columns=['Bigram', 'Count'])
bigram_df['Bigram'] = bigram_df['Bigram'].apply(lambda x: ' '.join(x))

plt.figure(figsize=(12,6))
sns.barplot(x='Count', y='Bigram', data=bigram_df, palette='viridis')
plt.title('Top 20 Most Common Bigrams in Reviews')
plt.xlabel('Count')
plt.ylabel('Bigram')
plt.tight_layout()
plt.savefig('images/common_bigrams.png')
plt.show()
