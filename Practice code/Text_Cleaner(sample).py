import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

REPLACE_BY_SPACE_RE = re.compile(r'[^\w\s]')

def text_cleaner(text):

    text = BeautifulSoup(text, "html.parser").get_text()
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = re.split(r'\s+', text.strip())
    cleaned_text = " ".join(word for word in text if word not in stop_words)
    return cleaned_text

def main():
    while True: 
        user_input = input("Enter a text to clean: ")
        if user_input.lower() in ['quit', 'q']:
            break    
        cleaned_text = text_cleaner(user_input)
        print(f"Cleaned text: {cleaned_text} \n")


if __name__ == "__main__":
    main()
