import unittest
from satisfaction_analysis import predict_sentiment

class TestPredictReviews(unittest.TestCase):
    def test_positive_review_prediction(self):
        input_review = "This product exceeded my expectations! Great value."
        predicted_satisfaction = predict_sentiment(input_review)
        self.assertEqual(predicted_satisfaction[0], "Positive")

    def test_negative_review_prediction(self):
        input_review1 = "Very disappointed with the quality. It broke after a few days."
        predicted_satisfaction1 = predict_sentiment([input_review1])
        self.assertEqual(predicted_satisfaction1[0], "Negative")

        input_review2 = "I tried it out yesterday, it's always broken. The glass breaks easily and the package is not secure enough."
        predicted_satisfaction2 = predict_sentiment([input_review2])
        self.assertEqual(predicted_satisfaction2[0], "Negative")

    def test_neutral_review_prediction(self):
        input_review = "The product is okay, but it could be better."
        predicted_satisfaction = predict_sentiment(input_review)
        self.assertEqual(predicted_satisfaction[0], "Neutral")

    def test_special_characters_review(self):
        input_review = "This product is great! I love it! :). The texture is soft and it feels very comfortable in my skin :D"
        predicted_satisfaction = predict_sentiment(input_review)
        self.assertEqual(predicted_satisfaction[0], "Positive")

#Test for Errors
    def test_error_input(self):
        input_review = None
        with self.assertRaises(TypeError):
            predicted_satisfaction = predict_sentiment(input_review)

if __name__ == '__main__':
    unittest.main()
    #Just run python -m unittest analysis_test.py

