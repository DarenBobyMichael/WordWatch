import pickle

def hatespeech(text):
    from sklearn.feature_extraction.text import CountVectorizer
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    with open('vectorizer.pkl', 'rb') as file:
        cv = pickle.load(file)

        i=text
        i = cv.transform([i]).toarray()
        if loaded_model.predict(i)[0] == 1:
            return 1
        else:
            return 0