import csv

def modify_csv(input_file, output_file, rows_per_score=500):
    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.DictReader(csv_in)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csv_out, fieldnames)
        writer.writeheader()

        scores = {}
        for row in reader:
            score = row['Score']
            if score not in scores:
                scores[score] = 0

            if scores[score] < rows_per_score:
                writer.writerow(row)
                scores[score] += 1

            if sum(scores.values()) >= len(scores) * rows_per_score:
                break

if __name__ == "__main__":
    input_file = r"D:\Downloads\Reviews.csv"
    output_file = "Training Data.csv"
    modify_csv(input_file, output_file)