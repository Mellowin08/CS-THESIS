from flask import Flask, render_template, request
# Import function
from satisfaction_analysis import predict_sentiment


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = request.form['review']

        # Get Prediction using imported function
        predicted_sentiment, (negative_confidence, neutral_confidence, positive_confidence) = predict_sentiment(user_input)

        return f"{predicted_sentiment},{negative_confidence},{neutral_confidence},{positive_confidence}"

if __name__ == '__main__':
    app.run(debug=True)
