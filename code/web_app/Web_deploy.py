from flask import Flask, render_template, request
# Import function
import sys
sys.path.append("..")
from satisfaction_analysis import predict_sentiment


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = request.form['review']

        # Get Prediction using imported function
        ans = predict_sentiment(user_input)

        if ans == 'Positive':
            return "Positive :)"
        elif ans == 'Negative':
            return "Negative :("
        elif ans == 'Neutral':
            return "Neutral :|"

if __name__ == '__main__':
    app.run(debug=True)
