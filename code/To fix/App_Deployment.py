import joblib
import contractions
import re
import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

negative_words = {'no', 'not', "don't", "aren't", "couldn't", "didn't", "doesn't", "hadn't", "hasn't", "haven't", "isn't", "mightn't", "mustn't", "needn't", "shouldn't", "wasn't", "weren't", "won't", "wouldn't", "never", "neither", "nor", "none", "nobody", "nowhere", "nothing", "hardly", "scarcely"}
stop_words = set(stop_words)

stop_words -= negative_words
len_stop_words = len(stop_words)

model = joblib.load(r"Practice code\Review_Analyzer")


def text_cleaner(text):
    text = text.lower() 
    text = re.sub(r'<.*?>', ' ', text) 
    text = re.sub(r'http\S+', ' ', text)    
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    words = text.split()
    words = [contractions.fix(word) for word in words]
    cleaned_text = " ".join(word for word in words if word not in stop_words)
    return cleaned_text



def main():
    while True: 
        user_input = input("Enter your review here:")
        if user_input.lower() in ['quit', 'q']:
            break    
        user_input = text_cleaner(user_input)
        result = model.predict([user_input])
        print(result)

if __name__ == "__main__":
    main()