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

The analysis was performed using various techniques:

1. **Descriptive Statistics**: Basic descriptive statistics were calculated for the numerical columns in the DataFrame. This included measures such as mean, median, standard deviation, minimum, and maximum.

2. **Correlation Analysis**: The correlation between different numerical columns was calculated to identify any potential relationships.

3. **Text Analysis**: The text data was analyzed using natural language processing techniques. This included tokenization, stop word removal, and sentiment analysis.

## Findings

The analysis revealed several interesting findings:

1. **Accuracy**: The accuracy of the model is 0.7221, indicating that it correctly classified 72.21% of the instances.
2. **False Positive Rate**: The false positive rate of the model is 0.2414, meaning that it incorrectly classified 24.14% of the negative instances as positive.

3. **Confusion Matrix**: The confusion matrix shows that the model performed well in classifying instances with a sentiment score of 0 or 4, but struggled with instances labeled as 2.

## Interpretations

Based on the findings, several interpretations can be made:

1. **Regarding Performance Metrics**: The model's accuracy of 0.7221 indicates that it is performing reasonably well in classifying sentiment. However, there is room for improvement, especially in reducing the false positive rate

2. **Regarding Pretrained Model Performance**: The model's performance in classifying instances with a sentiment score of 0 or 4 suggests that it is effective in identifying strongly negative or positive sentiments. However, its performance in classifying instances with a sentiment score of 2 which is neutral may need further improvemnt.

3. **Evaluating the Confusion Matrix**: The confusion matrix provides a visual representation of the model's performance, showing the number of instances correctly and incorrectly classified for each sentiment score. This information can be used to evaluate the model's strengths and weaknesses and guide future improvements. 


These interpretations provide valuable info regarding big data like Twitter Sentiments and can be used to improve the model's performance.