import pandas as pd

def modify_csv(input_file, output_file, num_rows_to_keep):
    df = pd.read_csv(input_file)
    df = df.head(num_rows_to_keep)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = r'D:\Documents\Reviews.csv'
    output_file = "Training Data.csv"

    modify_csv(input_file, output_file, num_rows_to_keep)