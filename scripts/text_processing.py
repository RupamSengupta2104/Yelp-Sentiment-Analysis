import pandas as pd
import re
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')

# Load cleaned file
df = pd.read_csv('data/yelp_cleaned.csv')

# Text Processing Function
def clean_text(text):
    text = str(text).lower()  # Ensure it's string and lowercased
    text = re.sub(r'[^a-z\s]', '', text)  # Keep only letters and spaces
    words = text.split()  # Simple split instead of nltk.word_tokenize

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Apply processing
df['cleaned_text'] = df['text'].apply(clean_text)

# Save processed file
df.to_csv('data/yelp_processed.csv', index=False)

print("✅ Text processing complete! Saved as yelp_processed.csv")
