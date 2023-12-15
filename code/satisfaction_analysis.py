from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from data_preprocess import text_cleaner
import joblib
import os
import numpy as np

current_path = os.path.dirname(__file__)
models_path = os.path.join(current_path, '../machine_learning/models/')
vectorizer = joblib.load(models_path + "tfidf_vectorizer.joblib")
svm_classifier = joblib.load(models_path + "SVM_classifier.joblib")


def predict_sentiment(user_input):
    clean_input = text_cleaner(user_input)

    input_vectorized = vectorizer.transform([clean_input])
    main_prediction = svm_classifier.predict(input_vectorized)

    # Calculate decision scores for each class
    decision_scores = svm_classifier.decision_function(input_vectorized)

    # Calculate confidence levels using softmax
    confidence_levels = np.exp(decision_scores) / np.sum(np.exp(decision_scores), axis=1, keepdims=True)

    # Convert confidence levels to percentages and round to whole numbers
    confidence_percentages = (confidence_levels * 100).round().astype(int).tolist()

    return main_prediction[0], confidence_percentages[0]


'''' Example usage
user_input = "I didn't like the movie but I enjoyed the popcorn"
predicted_sentiment, (negative_confidence, neutral_confidence, positive_confidence) = predict_sentiment(user_input)

print("Predicted Sentiment:", predicted_sentiment)
print("Negative Confidence (%):", negative_confidence)
print("Neutral Confidence (%):", neutral_confidence)
print("Positive Confidence (%):", positive_confidence)
'''
