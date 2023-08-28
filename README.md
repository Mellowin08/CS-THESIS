# Customer Satisfaction Analysis System

This is a decision support system for analyzing customer satisfaction in online shopping platforms using machine learning algorithm Support Vector Machine.
It includes a web application for user interaction and sentiment analysis of product reviews.

## Getting Started

Follow these instructions to set up and run the system locally.

### Prerequisites

- Python 3.11.4
  - Required Python libraries (listed in `requirements.txt`)

### Installation
1. Clone the Repository `gh repo clone Mellowin08/CS-THESIS`
2. Install the required dependencies
```bash
pip install -r requirements.txt
```

### Dataset
See Data Source section for the details of the dataset used in this project.

This project used a dataset that has a combination of non-digital product reviews (maximum of 100,000 rows for each category). If you want it, you can access it here: [amazon_reviews.csv](https://drive.google.com/file/d/1RfLyvBELQZ9aAbayx3O_iK5k23td5jjt/). 

Additionally, a Colab notebook has been provided, allowing you to customize your dataset combination. You can access it here: [Custom Dataset Selection.ipynb](https://colab.research.google.com/drive/1UxbcRmVtLWTrf50aL3YOTFiiMT2glOfC?usp=sharing).

After obtaining the dataset file, please put it on /CS-THESIS/data/raw_data/

## Data Source

The dataset used in this project was obtained from the [Amazon Review Data (2018)](https://nijianmo.github.io/amazon/index.html#subsets) generously provided by Jianmo Ni, UCSD.

- Dataset Name: Amazon Review Data (2018)
- Source: [https://nijianmo.github.io/amazon/index.html#subsets](https://nijianmo.github.io/amazon/index.html#subsets)
- Citation:
  "Justifying recommendations using distantly-labeled reviews and fined-grained aspects"
  Jianmo Ni, Jiacheng Li, Julian McAuley
  Empirical Methods in Natural Language Processing (EMNLP), 2019
  [PDF](http://cseweb.ucsd.edu/~jmcauley/pdfs/emnlp19a.pdf)
