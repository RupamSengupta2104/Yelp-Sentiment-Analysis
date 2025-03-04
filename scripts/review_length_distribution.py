import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'data/yelp.csv'
df = pd.read_csv(file_path)

# Add a column for review length (number of words per review)
df['review_length'] = df['text'].apply(lambda x: len(x.split()))

# Plot the distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['review_length'], bins=50, kde=True, color='skyblue')

# Plot labels
plt.title('Distribution of Review Length (Word Count)')
plt.xlabel('Number of Words in Review')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Save the plot
plt.savefig('images/review_length_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
