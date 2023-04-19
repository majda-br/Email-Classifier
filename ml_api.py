# -*- coding: utf-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer


app = FastAPI()


class model_input(BaseModel):
    email: str


# loading the saved model
email_classification_model = pickle.load(open("email_classification_model.sav", "rb"))
email_vectorizer_model = pickle.load(open("email_vectorizer.sav", "rb"))
stopWords = pickle.load(open("stopwords.sav", "rb"))


@app.post("/email_prediction")
def email_class_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    raw_input_data = input_dictionary["email"]
    preprocessed_input_data = []
    preprocessed_input_data.append(preprocessing_email(raw_input_data))

    preprocessed_input_data_embedding = email_vectorizer_model.transform(
        preprocessed_input_data
    )

    input_data_as_numpy_array = preprocessed_input_data_embedding.toarray()

    prediction = email_classification_model.predict(input_data_as_numpy_array)

    return prediction[0]


def preprocessing_email(email):
    # Unwanted list of words
    contex_words = [
        "subject",
        "best",
        "regards",
        "your name",
        "recipient",
        "dear",
        "please",
        "name",
        "thank",
        "email",
    ]

    # splits the sentences in words keeping alphabatic values only
    tokenizer = RegexpTokenizer(r"[a-zA-Z]+")
    words = tokenizer.tokenize(email)

    # instanciate the Stemmer
    ps = PorterStemmer()

    wordsFiltered = []
    for w in words:
        # lowercase words
        w = w.lower()
        # retrieve stopwords and context words
        if w not in stopWords and w not in contex_words:
            # Stemming of the filtred words
            wordsFiltered.append(ps.stem(w))

    return " ".join(wordsFiltered)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
