from flask import Flask, render_template, request
# Import function
from satisfaction_analysis import predict_sentiment

app = Flask(__name__)


@app.route('/individual_review.html')
def individual_reviews():
   return render_template('individual_review.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = request.form['review']

        # Get Prediction using imported function
        predicted_sentiment, (negative_confidence, neutral_confidence, positive_confidence) = predict_sentiment(user_input)

        return f"{predicted_sentiment},{negative_confidence},{neutral_confidence},{positive_confidence}"

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/consolidated_reviews.html')
def consolidated_reviews():
    return render_template('consolidated_reviews.html')

if __name__ == '__main__':
    app.run(debug=True)
