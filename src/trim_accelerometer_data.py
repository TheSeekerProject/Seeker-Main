import argparse
import csv

def trim_accelerometer_data(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)
        next(csv_reader) # Skip header row
        for row in csv_reader:
            acceleration_data = row[-3:] # Extract acceleration data from last 3 columns
            csv_writer.writerow(acceleration_data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Trim accelerometer data from CSV file')
    parser.add_argument('input_file_path', help='Path to input CSV file')
    parser.add_argument('output_file_path', help='Path to output CSV file')
    args = parser.parse_args()
    trim_accelerometer_data(args.input_file_path, args.output_file_path)

