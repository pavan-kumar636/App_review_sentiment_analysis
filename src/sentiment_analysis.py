import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('/content/linkedin-reviews.csv')
data.head()
data.info()
data.describe()
rating_counts = data['Rating'].value_counts().reset_index()
rating_counts
fig = px.bar(rating_counts, x='Rating', y='Count', title='Distribution of Ratings')
fig.show()
data['Review_len'] = data['Review'].apply(len)
data.head()
sns.histplot(data['Review_len'], bins = 50, kde = True)
plt.title('Distribution of Review Length')
plt.xlabel('Review Length')
plt.ylabel('Frequency')
plt.show()
from textblob import TextBlob
def review_Analysis(review):
  sentiment = TextBlob(review).sentiment
  if sentiment.polarity >0.1:
    return 'Positive'
  elif sentiment.polarity < -0.1:
    return 'Negative'
  else:
    return 'Neutral'

data['Sentiment'] = data['Review'].apply(review_Analysis)
data.head()
sentiment_counts = data['Sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Count']
sentiment_counts

fig = px.bar(sentiment_counts, x='Sentiment', y='Count', title = 'Sentiment Count')
fig.show()
sns.countplot(data = data, x='Rating', hue = 'Sentiment')
plt.title('Sentiment Count by Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.legend(title='Sentiment')
plt.show()
from wordcloud import WordCloud
def generate__word_cloud(sentiment):
  text = ' '.join(review for review in data[data['Sentiment']==sentiment]['Review'])
  wordcloud = WordCloud(width = 800, height = 400, background_color = 'White').generate(text)
  plt.figure(figsize=(10,5))
  plt.imshow(wordcloud, interpolation = 'bilinear')
  plt.axis('off')
  plt.title(f'Word Cloud for {sentiment} Reviews')
  plt.show()

for sentiment in data['Sentiment'].unique():
  generate__word_cloud(sentiment)
  



