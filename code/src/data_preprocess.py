import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


stop_words = set(stopwords.words('english'))
negative_words = {'no', 'not', "don't", "aren't", "couldn't", "didn't", "doesn't", "hadn't", "hasn't", "haven't", "isn't", "mightn't", "mustn't", "needn't", "shouldn't", "wasn't", "weren't", "won't", "wouldn't", "never", "neither", "nor", "none", "nobody", "nowhere", "nothing", "hardly", "scarcely"}
stop_words -= negative_words # Remove the Negative words


import contractions
import re

def text_cleaner(text):
    text = str(text).lower()                   # Convert to string and lowercase
    text = re.sub(r'<.*?>', ' ', text)         # Remove HTML tags
    text = re.sub(r'http\S+', ' ', text)       # Remove URLs using regular expression not covered by tags
    text = re.sub(r'[^A-Za-z0-9\s]', '', text) # Remove non-alphanumeric characters using regular expression
    words = text.split()                       # Splitting the text into individual words
    words = [contractions.fix(word) for word in words]  # Expand Contractions
    cleaned_text = " ".join(word for word in words if word not in stop_words) # Remove the stopwords from the text.
    return cleaned_text
