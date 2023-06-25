import pickle
from sklearn.feature_extraction.text import CountVectorizer
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    cv = pickle.load(file)

while True:
    i=input('Enter the text to be detected: ')
    i = cv.transform([i]).toarray()
    print(loaded_model.predict(i))