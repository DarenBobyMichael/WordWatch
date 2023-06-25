import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import nltk
import re
from nltk.corpus import stopwords
stopword=set(stopwords.words('english'))
stemmer = nltk.SnowballStemmer("english")

data=pd.read_csv("hate_speech.csv")
# print(data.head())

data["labels"]=data["label"].map({'hate':"Hate Speech", 'nothate':"Not Hate Speech"})
data=data[["text","labels"]]
print(data)

import re

def clean (text):
 text = str(text).lower()
 text = re.sub('[.?]', '', text)
 text = re.sub('https?://\S+|www.\S+', '', text)
 text = re.sub('<.?>+', '', text)
 text = re.sub(r'[^\w\s]','',text)
 text = re.sub('\n', '', text)
 text = re.sub('\w\d\w', '', text)
 text = [word for word in text.split(' ') if word not in stopword]
 text=" ".join(text)
 text = [stemmer. stem(word) for word in text. split(' ')]
 text=" ".join(text)
 return text
data["clean_text"] = data["text"].apply(clean)
data.to_csv('hatespeech.csv', index=False)
