import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
import nltk

from nltk.corpus import stopwords
stopword=set(stopwords.words('english'))
stemmer = nltk.SnowballStemmer("english")

data=pd.read_csv("hate_speech_cleaned.csv")
# print(data.head())

# import re

# def clean (text):
#  text = str(text).lower()
#  text = re.sub('[.?]', '', text)
#  text = re.sub('https?://\S+|www.\S+', '', text)
#  text = re.sub('<.?>+', '', text)
#  text = re.sub(r'[^\w\s]','',text)
#  text = re.sub('\n', '', text)
#  text = re.sub('\w\d\w', '', text)
#  text = [word for word in text.split(' ') if word not in stopword]
#  text=" ".join(text)
#  text = [stemmer. stem(word) for word in text. split(' ')]
#  text=" ".join(text)
#  return text
# data["text"] = data["text"].apply(clean)


x=np.array(data["text"])
y=np.array(data["labels"])

cv=CountVectorizer()
X = cv.fit_transform(x)
X_train,X_text,y_train,y_test = train_test_split(X,y,test_size=0.33)
model= DecisionTreeClassifier()
model.fit(X_train,y_train)
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(cv, file)
y_pred=model.predict(X_text)
from sklearn.metrics import accuracy_score
print(f"The accuracy score: {accuracy_score(y_test,y_pred)}")
# while True:
#     i=input('Enter the text to be detected: ')
#     i = cv.transform([i]).toarray()
#     print(model.predict(i))