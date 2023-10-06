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
# palitan nyo lang ip address dito na nakassign sa pc nyo para maacess sa mobile or tablets
# then type nyo sa web browser nyo sa phone/table ex. "192.168.1.15:5000"
    app.run(debug=True, host='192.168.1.15', port=5000)
