# Import the necessary libraries
import spacy  # Import the spaCy library for natural language processing
from textblob import TextBlob  # Import the TextBlob library for sentiment analysis

# Load the spaCy model for English (small version)
nlp = spacy.load("en_core_web_sm")

# Define a function to analyze the sentiment of a given text using TextBlob
# Note: di ko ginamit sentiment analyzer natin kasi nakabuild in ang text cleaner which i need punctuatuion marks
def analyze_sentiment(text):
    analysis = TextBlob(text)  # Create a TextBlob object with the input text
    sentiment = analysis.sentiment.polarity  # Get the polarity score (sentiment score)
    if sentiment > 0:
        return 'Positive'  # Return 'Positive' if sentiment is positive
    elif sentiment < 0:
        return 'Negative'  # Return 'Negative' if sentiment is negative
    else:
        return 'Neutral'  # Return 'Neutral' if sentiment is close to zero

# Define a function to extract phrases from a text
def extract_phrases(text, min_length=2, max_length=6):
    doc = nlp(text)  # Process the input text with spaCy to create a Doc object
    phrases = []  # Initialize an empty list to store phrases
    current_phrase = []  # Initialize an empty list for the current phrase being extracted

    for token in doc:
        if token.is_alpha:  # Check if the token is alphabetic (a word)
            current_phrase.append(token.text)  # Add the word to the current phrase
        else:
            if min_length <= len(current_phrase) <= max_length:
                phrases.append(" ".join(current_phrase))  # If the phrase length is within the specified range, add it to the list
            current_phrase = []  # Reset the current phrase for the next sequence

    if min_length <= len(current_phrase) <= max_length:
        phrases.append(" ".join(current_phrase))  # Add the last phrase to the list if it meets the criteria

    return phrases  # Return the list of extracted phrases

# When using extract_phrases 
# Simple explanation if may nakita sya punctuation mark like dot or coma or etc hahatiin nya and consider main phrase...
# Sample date: "This is an example sentence. It contains multiple phrases."
# Output:
# "This is an example sentence"
# "It contains multiple phrases"




# Define a function to extract phrases using part-of-speech (POS) tagging
def extract_phrases_nopunc(text):
    highlighted_phrases = []  # Initialize an empty list to store highlighted phrases

    # Define the parts of speech (POS) that are typically part of phrases (Adjectives, Nouns, Adverbs)
    phrase_pos_tags = {"ADJ", "NOUN", "ADV"}

    # Process the input text with spaCy to create a Doc object
    doc = nlp(text)

    for i, token in enumerate(doc):
        if token.pos_ in phrase_pos_tags:  # Check if the token's POS is in the specified set
            phrase = token.text  # Initialize the phrase with the current token
            for j in range(1, 6):  # Look ahead to the next 5 tokens
                if i + j < len(doc):
                    next_token = doc[i + j]
                    if next_token.pos_ in phrase_pos_tags:  # If the next token's POS is in the set
                        phrase += " " + next_token.text  # Add the token to the current phrase
                    else:
                        break  # If the next token is not in the set, stop extending the phrase
                else:
                    break  # If reaching the end of the document, stop extending the phrase
            if 3 <= len(phrase.split()) <= 6:  # Check if the phrase contains 3 to 6 words
                highlighted_phrases.append(phrase)  # Add the phrase to the list of highlighted phrases

    return highlighted_phrases  # Return the list of highlighted phrases

# When using extract_phrases_nopunc
# Simple explanation if may nakita sya adjectives, nouns, or adverbs and have a length of 3 to 6 words consider as main phrase...
# Sample date: "adjectives, nouns, or adverbs and have a length of 3 to 6 words"
# Output:
# "quick brown fox jumps"
# "runs very fast"


# Accept user input for a review
user_input = input("Enter a review: ")

# Extract phrases using both methods and combine the results
user_phrases = extract_phrases(user_input) + extract_phrases_nopunc(user_input)

# Analyze the sentiment for all extracted phrases
for phrase in user_phrases:
    sentiment = analyze_sentiment(phrase)  # Analyze the sentiment of each extracted phrase
    print(f"Phrase: '{phrase}' - Sentiment: {sentiment}")  # Print the phrase and its sentiment
