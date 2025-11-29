# Install jdk8
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
import os
# Set jdk environment path which enables you to run Pyspark in your Colab environment.
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
!update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

Confguring Kaggle dataset
!pip install -q opendatasets

import opendatasets as od
od.download('https://www.kaggle.com/datasets/kazanova/sentiment140')
!pip install -q findspark pyspark==3.3.0 nltk
#### for data manipulation and math operations ####
import pandas as pd
import numpy as np

#### for visualizations ####
# plotly
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns

#### NLP packages ####
# NLTK library
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import word_tokenize

#### other useful packages ####
import string
from collections import Counter
import re
from tqdm import tqdm


#### Pyspark packages ####
from pyspark.sql import functions as func
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

#### Evalutions ####
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# import findspark
# findspark.init()
# findspark.find()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Tweet").getOrCreate()
# spark.stop()
spark

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType
from pyspark.sql.functions import col, to_timestamp, expr
from pyspark.sql.functions import udf


# Load the data from HDFS
df =(spark.read
          .format('csv')
          .option('header', 'false')
          .load('sentiment140/training.1600000.processed.noemoticon.csv'))
# Show the DataFrame
df.show(truncate=False)
df.count(), len(df.columns) # Size / shape of dataset
# adding columns to dataset
from pyspark.sql.functions import col, to_timestamp, expr


df = (df.withColumnRenamed('_c0','target').withColumnRenamed('_c1','id').withColumnRenamed('_c2','tweet_date')\
  .withColumnRenamed('_c3','flag').withColumnRenamed('_c4','user').withColumnRenamed('_c5','text')
)
df = df.withColumn('tweet_date', expr('substring(tweet_date, 5, 27)'))
df = df.select(col('target').cast('int'),
                         col('id').cast('int'),
                         to_timestamp(col('tweet_date'),'MMM dd HH:mm:ss zzz yyyy').alias('date'),
                         col('flag').cast('string'),
                         col('user').cast('string'),
                         col('text').cast('string'),
                        )

df.show(truncate=False)
df.printSchema()
Preprocessing dataset
# missing values
df.select([func.count(func.when(func.isnan(c),c)).alias(c) for c in df.columns]).toPandas().head()

# check duplicates
duplicates = df.groupBy("text").count().where("`count` > 1")

# Show duplicates
duplicates.show()
df = df.dropna()
df.count(), len(df.columns) # Size / shape of dataset after dropping NA values
# drop duplicates
df = df.dropDuplicates(['text'])
df.groupBy("text").count().where("`count` > 1").show()
df.dtypes
# only work on text and target, to reduce baggage
drops= ("id","date","flag","user")
df = df.drop(*drops)
df.show(5, truncate = False)
# change column target from 4 to 1 and rename it to 'label'
df = df.withColumnRenamed('target', 'label')
df = df.withColumn('label', func.when(df.label == 4, 1).otherwise(df.label))
df.select('label').distinct().show()
Text Clean Cell **Minimized as it was done in previous part**
nltk.download('stopwords')
nltk.download('punkt')
stop_words = stopwords.words("english")
stemmer = SnowballStemmer("english")
text_cleaning_re = r"@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
spark.conf.set("spark.sql.execution.pythonUDF.arrow.enabled", "false")

# decorator for udf
@udf(returnType=StringType())
def preprocess(text, stem=False):
    # Remove link,user and special characters
    word_tokens = word_tokenize(text)
    # filtered_sentence = [w.lower() for w in word_tokens if not w.lower() in stop_words and w.isalpha()]
    filtered_sentence = []
    for word in word_tokens:
        word = re.sub(text_cleaning_re, ' ', word)
        if word not in stop_words:
            filtered_sentence.append(word)
        if stem == True:
            filtered_sentence.append(stemmer.stem(word))

    return " ".join(filtered_sentence)

# preprocess = udf(preprocess, StringType())
df = df.withColumn('text_cleaned',preprocess(df.text))
df.show(5, truncate = False)
# EDA and Visualizations
# distribution of sentiments
df.groupBy("label").count().show()
# convert df to train for pandas dataframe
train = df.toPandas()
class_group_counts = train.groupby('label').count()['text'].reset_index().sort_values(by='text',ascending=False)
class_group_counts.style.background_gradient(cmap='Blues')
# Bar Chart for Distribution of Data in accordance to Sentiment classes.

import plotly.graph_objs as go

# create the trace
trace = go.Bar(
    x = class_group_counts['label'],
    y = class_group_counts['text'],
    marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                 line=dict(color='rgb(0,0,0)',width=1.5)),
    text = class_group_counts['text'],
    )

data = [trace]
layout = go.Layout(barmode = "group",title='Sentiment Distribution')

fig = go.Figure(data = data, layout = layout)
fig.show()
# Pie Chart for Distribution of Data in accordance to Sentiment classes.


import plotly.graph_objs as go

# create the trace
trace = go.Pie(
    labels = class_group_counts.label,
    values = class_group_counts.text
)

data = [trace]
layout = go.Layout(title="Pie plot of the distribution of the categorical classes")

fig = go.Figure(data = data,layout=layout)
fig.show()
# Group by date and count the number of tweets per day
tweet_count_per_day = df.groupBy("date").count().orderBy("date")

# Convert Spark DataFrame to Pandas DataFrame for plotting
tweet_count_per_day_pd = tweet_count_per_day.toPandas()

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=tweet_count_per_day_pd, x='date', y='count')
plt.xlabel('Date')
plt.ylabel('Tweet Volume')
plt.title('Tweet Volume Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.grid(True)
plt.show()

# top 10 most frequent words in the dataset
from sklearn.feature_extraction.text import TfidfVectorizer
def get_top_n_words(corpus, n=None):
    vec = TfidfVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]

common_words = get_top_n_words(train['text'], 10)
df2 = pd.DataFrame(common_words, columns = ['text' , 'count'])
df2.groupby('text').sum()['count'].sort_values(ascending=False).plot(
    kind='bar', title='Top 10 words in text before removing stop words')

# User engagement metrics
# Average length of tweet
train['text_len'] = train['text'].apply(len)
train['text_len'].describe()

# visualisations firectly from spark dataframe: df

train= train.drop('text_len', axis=1)
# Average length of tweet
dfv = df.toPandas()
dfv['text_len'] = dfv['text'].apply(len)
dfv.plot(kind='hist', y='text_len', bins=20, title='Average length of tweet')
# Average word length
def avg_word(sentence):
    words = sentence.split()
    return (sum(len(word) for word in words)/len(words))

dfv['avg_word_len'] = dfv['text'].apply(avg_word)
dfv.plot(kind='hist', y='avg_word_len', bins=20, title='Average word length')
df = df.drop('text')
# Wordcloud
!pip install -q wordcloud

from wordcloud import WordCloud

pandas_df = df.toPandas()
pandas_df.head()
# Pos Sentiments Wordcloud
pandas_df['label'] = pandas_df['label'].astype(int)
pandas_df['text_cleaned'] = pandas_df['text_cleaned'].astype(str)
plt.figure(figsize = (20,16))
wc = WordCloud(max_words = 2000 , width = 1600 , height = 900).generate(" ".join(pandas_df[pandas_df["label"]==1.0].text_cleaned))
plt.imshow(wc , interpolation = 'bilinear')
## Neg Sentiments Wordcloud
plt.figure(figsize = (20,16))
wc = WordCloud(max_words = 2000 , width = 1600 , height = 900).generate(" ".join(pandas_df[pandas_df["label"]==0.0].text_cleaned))
plt.imshow(wc , interpolation = 'bilinear')
# Prepare data for modelling
## Tokenization, Stopwords removal, TF-IDF
df = df.withColumn("label", col("label").cast("int"))
tokenizer = Tokenizer(inputCol="text_cleaned", outputCol="words_toks")
words_toks = tokenizer.transform(df)
words_toks.show(5, truncate = False)
vectorizer = CountVectorizer(inputCol="words_toks", outputCol="raw_features")
model = vectorizer.fit(words_toks)
featurizedData = model.transform(words_toks)
featurizedData.show(5, truncate = False)
idf = IDF(inputCol="raw_features", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)
rescaledData.select ("label", "features").show(5, truncate = False)
df_scaled = rescaledData.select("label", "features")
seed = 42
train_df, test_df = df_scaled.randomSplit([0.7, 0.3], seed=seed)
train_df.count(), test_df.count()
train_df.show(5, truncate = False)
train_df.groupBy("label").count().show()
# Creating the model
lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=10)
model = lr.fit(train_df)
predictions = model.transform(test_df)
preds = predictions.toPandas()
preds.head()
# Model Evaluation
evaluator = BinaryClassificationEvaluator(labelCol='label',metricName='areaUnderROC')
areaUnderROC = evaluator.evaluate(predictions)
print(f"The testing areaUnderROC of our Logistic Regression model is: {areaUnderROC}")
y_true = preds['label'].astype('float')
y_pred = preds['prediction']
y_true.value_counts()
y_pred.value_counts()
print(classification_report(y_true, y_pred))
print(accuracy_score(y_true, y_pred))
sns.heatmap(confusion_matrix(y_true, y_pred), annot=True, fmt='g', cmap='Blues')
# Final Report
> By Ammar Ahmed 20L-0961
## Data Collection Methodology

The data was collected in a structured format using the PySpark framework. I downloaded the dataset from Kaggle using opendatasets and then loaded the data into a Spark DataFrame. The data was then cleaned and processed using PySpark only.

## Preprocessing Steps

The data preprocessing involved several steps:

1. **Column Renaming**: The dataframe was renamed using WithColumn and then data was altered to rename the columns to more appropriate names.

2. **Data Loading**: The data was loaded into a PySpark DataFrame using the defined schema and encoding.

3. **Data Cleaning**: The data was cleaned by removing unnecessary columns, handling missing values, and converting data types where necessary. For example, the "tweet_date" column was converted to a timestamp using the `to_timestamp` function.

4. **Feature Engineering**: New features were created from the existing data using PySpark's `expr` and `udf` functions. These features were added to the DataFrame as new columns.

## Analysis Techniques
We employed logistic regression for sentiment analysis due to its simplicity and effectiveness. Logistic regression is a binary classification algorithm that models the probability of an instance belonging to a particular class (positive or negative).

### Logistic Regression Basics
- Logistic regression uses a logistic function (sigmoid) to model the probability of the positive class:
  $$ P(y=1) = \frac{1}{1 + e^{-z}} $$
  where:
    - $z$ is the linear combination of features and their corresponding weights.
    - $e$ is the base of the natural logarithm.

### Model Training
- We split the dataset into training and validation sets.
- Trained the logistic regression model using the training data.
- Evaluated the model performance on the validation set.

## Findings
1. **Model Performance**:
   - Accuracy: Approximately 76%.
   - Precision and recall are balanced for both positive and negative classes.
   - F1-score indicates a good trade-off between precision and recall.

2. **Confusion Matrix**:
   - True Positives (TP): 180,858 (correctly predicted positive instances).
   - True Negatives (TN): 178,036 (correctly predicted negative instances).
   - False Positives (FP): 59,082 (incorrectly predicted as positive).
   - False Negatives (FN): 55,902 (incorrectly predicted as negative).

3. **Tweet Length Distribution**:
   - Average tweet length: Approximately 74 characters.
   - Minimum tweet length: 6 characters.
   - Maximum tweet length: 359 characters.

## Interpretations
- Our model performs reasonably well in distinguishing positive and negative sentiment.
- The most common words before removing stop words include 'to', 'the', 'my', 'you', 'it', 'and', 'is', 'for', 'in', and 'of'.
- Word clouds were useful for quickly identifying prevalent sentiments in a large text dataset.

## wordclouds
### positive wordcloud
- Words like “love,” “thank,” and “awesome” stand out prominently.
- The inclusion of terms like “good morning” suggests positivity related to greetings.
- The variety of positive words creates an uplifting and cheerful tone.
### negative wordcloud
- Words like “sad,” “wish,” "ugh," and “hate” are prevalent.
- The presence of terms like “miss” and “bad” indicates negative sentiments.
- The negative word cloud conveys a sense of disappointment and frustration.

## Conclusion
Our Twitter sentiment analysis provides valuable insights into public sentiment. The word clouds offer a visual representation of the most common words in positive and negative tweets, aiding in sentiment analysis and interpretation. By leveraging PySpark's capabilities, we can efficiently process large datasets and derive meaningful insights for decision-making. The model's performance metrics indicate its effectiveness in classifying tweets based on sentiment, enabling us to gauge public opinion and sentiment trends effectively.