import unittest
from satisfaction_analysis import predict_sentiment

class TestPredictSentiment(unittest.TestCase):

    def test_positive_sentiments(self):
        positive_data = [
            ("Positive", "This product exceeded my expectations! Great value."),
            ("Positive", "My biggest concern buying these was that there would be a bunch of duds in the box. So far, they're all good. I'm a teacher and don't believe in giving kids a hard time if they show up to class without a pencil....even that one kid that shows up every day without the pencil you gave them yesterday. Anyhow, the pencils are good and at this unit price it makes it somewhat affordable to give that kid a pencil every day, even if I have to use my own money to buy them...."),
            ("Positive", "This product is great! I love it! :). The texture is soft and it feels very comfortable in my skin :D"),
        ]
        self._test_sentiment_predictions(positive_data)

    def test_negative_sentiments(self):
        negative_data = [
            ("Negative", "Very disappointed with the quality. It broke after a few days."),
            ("Negative", "I tried it out yesterday, it's always broken. The glass breaks easily, and the package is not secure enough."),
            ("Negative", "I wanted to give felting a try. First off the texture of the cotton isn't great. It felt uncomfortable to touch and It doesn't really stiffen when I poke it. You can tell that the materials used are very cheap compared to the ones you buy in a shop."),
        ]
        self._test_sentiment_predictions(negative_data)

    def test_neutral_sentiments(self):
        neutral_data = [
            ("Neutral", "The product is okay, but it could be better."),
            ("Neutral", "I recently bought a new mini pc for a good price and saw this for some more memory. I picked this both up for less than $500. Good price for an early birthday gift. I had just a bit of problems installing Windows on it. That was user error though. But when I finally got it to work...I couldn't get ANY network adapters, network drivers, and connections to work once I installed this. It has been 6 hours since I started.. No Exaggeration. I started it at 6:45 pm..it is now 12:20 am...I'm beyond frustrated. That's okay I'm sure it would have been great to be able to use this and finally do some gaming. I'll just stick to an external drive and keep the original SSD in the computer."),
        ]
        self._test_sentiment_predictions(neutral_data)

    def test_other_checks(self):
        other_checks = [
            # Emoji
            ("Positive", "This product is great! I love it! 😍. The texture is soft and it feels very comfortable in my skin 🤗"),
            # Special Characters
            ("Negative", "They didn't even bother packaging it properly. It arrived and there are spills everywhere! It leaked during shipment (49% percent of the product is left). There are no safety labels!! >:( "),
            # Capital Letters Only.
            ("Neutral", "IT WAS MEH. NOT THAT GOOD BUT NOT THAT BAD, THE TASTE COULD BE IMPROVED BUT IT'S ACTUALLY DOABLE."),
        ]
        self._test_sentiment_predictions(other_checks)

    def _test_sentiment_predictions(self, data):
        for expected_sentiment, review in data:
            with self.subTest(review=review):
                prediction = predict_sentiment(review)
                self.assertEqual(prediction[0], expected_sentiment)

if __name__ == '__main__':
    unittest.main()
