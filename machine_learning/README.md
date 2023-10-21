# Model Training
See Data Source section in the main README.md for the details of the dataset used in this project.

This project used a dataset that has a combination of non-digital product reviews (maximum of 100,000 rows for each category). If you want it, you can access it here: [amazon_reviews.csv](https://drive.google.com/file/d/1RfLyvBELQZ9aAbayx3O_iK5k23td5jjt/).

Additionally, a Colab notebook has been provided, allowing you to customize your dataset combination. You can access it here: [Custom Dataset Selection.ipynb](https://colab.research.google.com/drive/1UxbcRmVtLWTrf50aL3YOTFiiMT2glOfC?usp=sharing).

After obtaining the dataset file, please put it on `/CS-THESIS/data/raw_data/` and begin using the ipnyb notebooks. Start with 1 to Prepare the dataset and use 2 to Train the Model.

After generating the joblib files, it will be saved in `machine_learning/models/test_model`. please move it one level up to `models/` so that the Web app can read it.
