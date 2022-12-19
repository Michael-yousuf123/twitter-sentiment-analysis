
# Twitter sentiment analysis for the Qatar 2022 FIFA World Cup
## Author

- [Michael Yousuf](https://github.com/Michael-yousuf123)

## Technologies Used
In order to understand the sentiments of twitter users, this project used a variety of Python packages. 
Here are a few examples.

![twitter](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

## Goal

The goal of this project was to use sentiment analysis on data collected from Twitter to ascertain the feelings of FIFA World Cup 2022 viewers. In order to understand the sentiments of twitter users, this project used a variety of Python packages. The following sections explain the project's general procedure.

## Steps of text Processing

The individual tweets have to be cleaned up in order to achieve the main objective. The captured tweets are first processed in Python using the "processed_tweet" method created in Python. Punctuation, links, emoticons, and stop words were all removed from the tweets using this user-defined function in a single pass. In addition, I applied an NLP principle called "Tokenization." It is a technique for removing superfluous parts of a sentence by breaking it up into smaller chunks called "tokens." "Lemmatization" is a further method worth mentioning. Words are being "reverted" to their "base" form through this process. The illustration below is straightforward.

## Word-Cloud 

I used the NLTK library's Parts of Speech tagging module to identify the player that had the most mentions during the Qatar 2022 FIFA World Cup. One may create a Word Cloud based on word frequency and overlay these words over any image by using the WordCloud library. The most popular terms stated in tweets are presented in strong and large characters on the world cup graphic, while the least popular words are shown in smaller letters.

![Alt text](static/wordcloud.png?raw=true "Title")

## License

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/michaelyousuf/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/mikaelyousuf)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@michaelabdi2)
[![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/mchlabdi)