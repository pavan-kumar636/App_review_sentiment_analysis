# App Reviews Sentiment Analysis using Python
App Reviews Sentiment Analysis means evaluating and understanding the sentiments expressed in user reviews of mobile applications (apps).
It involves using data analysis techniques to determine whether the sentiments in these reviews are positive, negative, or neutral.
App Reviews Sentiment Analysis is a valuable tool for app developers and businesses to understand user feedback, prioritize feature updates, and maintain a positive user community.

Below is the process that i followed for the task of app reviews sentiment analysis:

The first step is to gather a dataset of app reviews.
Then, perform EDA by analyzing the length of the reviews and their ratings, etc.
Then, label the sentiment data using tools like Textblob or NLTK.
Understand the overall distribution of sentiments (positive, negative, neutral) in the dataset.
Explore the relationship between the sentiments and the ratings given.
Analyze the text of the reviews to identify common themes or words in different sentiment categories.

Dataset is LinkedIn reviews 
The dataset contains two columns: Review and Rating. The Review column consists of textual reviews, and the Rating column contains corresponding numerical ratings.

![Screenshot 2024-09-09 184819](https://github.com/user-attachments/assets/8879d335-0b80-41d5-8c9f-6ecbd9b1ea36)

![image](https://github.com/user-attachments/assets/39d6395c-d764-4f27-bdf4-0ad6b7118d54)

Here’s the distribution of ratings from the LinkedIn reviews dataset. As you can see, it gives a clear picture of how many reviews fall into each rating category (from 1 to 5).

![image](https://github.com/user-attachments/assets/b6ab0f30-85f5-4094-ac32-886fc7d22145)

The above histogram give the information about review length frequency

# Adding Sentiment Labels in the Data
the next step is to label the data with sentiments. We can use Textblob for this task. TextBlob provides a polarity score ranging from -1 (very negative) to 1 (very positive) for a given text. We can use this score to classify each review’s sentiment as positive, neutral, or negative. You can install it by executing the pip command mentioned below in your terminal or command prompt:  pip install textblob

![image](https://github.com/user-attachments/assets/4c581f77-4a23-4ad3-87fb-6b89b65dc5b3)

The dataset now includes sentiment labels for each review, classified as Positive, Negative, or Neutral based on the polarity score calculated by TextBlob.

# Analyzing App Reviews Sentiments
Now that our dataset is labelled, let’s perform app reviews sentiment analysis. We’ll begin by analyzing the distribution of sentiments across the dataset. It will give us a basic understanding of the general sentiment tendency in the reviews:

![image](https://github.com/user-attachments/assets/0e053d10-8913-43fd-9a41-4971fbcaebff)

So, we can see although the app has low ratings, still the reviewers don’t use many negative words in the reviews for the app.

Next, we’ll explore the relationship between the sentiments and the ratings. This analysis can help us understand whether there is a correlation between the sentiment of the text and the numerical rating. For this task, we can see how sentiments are distributed across different rating levels:

![image](https://github.com/user-attachments/assets/0bb4b7bd-e5bd-44c1-99c8-d3526ac213d3)

Now, let’s perform a text analysis to identify common words or themes within each sentiment category. It involves examining the most frequently occurring words in positive, negative, and neutral reviews using a word cloud:

![image](https://github.com/user-attachments/assets/d7d8494d-6072-4086-a83d-1b7acfd6433b)

![image](https://github.com/user-attachments/assets/1e91525b-2906-4057-b06c-dc0ffa3b041b)

![image](https://github.com/user-attachments/assets/9c72d0a2-1b50-4f55-a9fb-f48045fe0975)

# Summary
So, App Reviews Sentiment Analysis is a valuable tool for app developers and businesses to understand user feedback, prioritize feature updates, and maintain a positive user community. It involves using data analysis techniques to determine whether the sentiments in these reviews are positive, negative, or neutral.
