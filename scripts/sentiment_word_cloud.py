import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Load the data
df = pd.read_csv('data/yelp_with_sentiment.csv')

# Define function to create and save word cloud
def generate_wordcloud(sentiment):
    text = " ".join(df[df['sentiment'] == sentiment]['cleaned_text'].dropna())
    
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        stopwords=STOPWORDS,
        colormap='viridis',
        max_words=100
    ).generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud - {sentiment} Reviews')
    
    # Save to images folder
    plot_path = f'images/wordcloud_{sentiment}.png'
    plt.savefig(plot_path, dpi=300)
    print(f'Saved word cloud: {plot_path}')
    plt.show()

# Generate word clouds for Positive and Negative only
generate_wordcloud('Positive')
generate_wordcloud('Negative')
