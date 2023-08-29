# ESG Sentiment Analysis of the Annual Reports of publicly traded Automotive Manufacturers 
## Abstract
This project demonstrates the use of natural language processing methods in Python to perform a sentiment analysis on annual report (10-K) SEC filings of three automotive manufacturers, specifically focusing on the sentiment around the corporate ESG policies.

Model was built using Python 3.8.6.

## Motivation
In recent years environmental, social, and governance (ESG) investing, where investors account for corporate policies pertaining to those categories when making investments, has grown in popularity. Many fund managers have even created proprietary investment funds that specifically track ESG and sustainability metrics when performing allocation. I was interested to see whether one can use machine learning techniques, specifically natural language processing, to quantifiably measure sentiment pertaining to corporate ESG policies across a specific industry.

**Disclaimer**: The results of this model are experimental in nature and should not be confused as justification for investment decision-making. 

## About the Data Used
Data used for this model was derived from multiple sources, depending on the use and purpose. 

For training the model to recognize the difference between ESG related and non-ESG related text, multiple online articles were downloaded and converted to '*.txt" format. ESG articles were found using Google searches and filtering criteria corresponding to ESG-related terms. 

In order to train the model to recognize 'positive' and 'negative' sentiments, the Loughran-McDonald Master Dictionary with Sentiment Word Lists data set was used.

Testing was performed on the three FY-19 annual 10-K SEC filings for Fiat-Chrysler Automobiles (FCA), Ford Motor Company (F), and General Motors (GM).

## Methodology
For the purposes of this project, a supervised training model was employed. The implementation methodology can be broken down into the following key steps:

1. Build the positive and negative words dictionary.
2. Build the ESG dictionaries (one for each category: environmental, social, governance).
3. Read in the target text file.
4. Utilizing a three-sentence moving window identify all instances of environmental, social, and governance discussions.
5. Count the total number of words that are positive and negative. By subtracting the number of negative words from the number of positive words, derive the total "points" for the given ESG category. Given the varying quantity of ESG discussions per text file, we want to normalize the metric to a percentage that can be used for cross-file comparison.
6. For each file, derive the total ESG points by aggregating the total points for each ESG category. 

## Results
The resulting output of the model can be seen below. The output includes an itemized breakdown of the frequency of discussion, total net sentiment, and net sentiment as a fraction to the total frequency of discussion for each category and for each company. Looking at the total sentiment for each company we see that there is a generally negative sentiment across each company. However, of the three companies, Ford Motors has the least negative sentiment.

![image](https://github.com/wgemba/AnnualReport_NLP/assets/134420287/be1cb052-0a91-4e92-81ef-76e1eee19098)
