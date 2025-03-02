import os
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the images folder exists
os.makedirs('images', exist_ok=True)

# Load the processed dataset (with cleaned_text column already there)
file_path = 'data/yelp_processed.csv'
df = pd.read_csv(file_path)

# Combine all cleaned text into one big string (corpus)
all_words = " ".join(df['cleaned_text'])

# Split into individual words
word_list = all_words.split()

# Get frequency count of each word
word_freq = Counter(word_list)

# Get top 20 words
top_words = word_freq.most_common(20)

# Unpack for plotting
words, counts = zip(*top_words)

# Plot
plt.figure(figsize=(12, 6))

# Recommended way to avoid future seaborn warning
sns.barplot(x=list(words), y=list(counts), hue=list(words), legend=False, palette='viridis')

plt.xticks(rotation=45)
plt.title('Top 20 Most Common Words in Yelp Reviews')
plt.xlabel('Words')
plt.ylabel('Frequency')

# Save plot as image
plot_path = 'images/top_20_words_frequency.png'
plt.savefig(plot_path, bbox_inches='tight', dpi=300)

# Show plot
plt.show()

print(f"Plot saved successfully at: {plot_path}")
