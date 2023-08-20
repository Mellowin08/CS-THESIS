from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from data_preprocess import text_cleaner, stop_words
import joblib
import os

current_path = os.path.dirname(__file__)
models_path = os.path.join(current_path, '..', 'models/')
vectorizer = joblib.load(models_path+"tfidf_vectorizer.joblib")
svm_classifier = joblib.load(models_path+"SVM_classifier.joblib")

def predict_sentiment(user_input):
    if not user_input:
        raise TypeError("Input cannot be empty")


    user_input = text_cleaner(user_input)
    cleaned_words_vectorized = vectorizer.transform([user_input])
    result = svm_classifier.predict(cleaned_words_vectorized)
    return result[0]
