from PIL import Image
from check_for_updates import check_for_updates
import csv, time, sys, argparse, imagehash

# Image similarity function to calculate score
def image_similiarity_score(image_a, image_b):
    hash1 = imagehash.average_hash(Image.open(image_a))
    hash2 = imagehash.average_hash(Image.open(image_b))
    return abs(hash1-hash2)

def main():
    print(check_for_updates())
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-csv', required=True, dest='input_csv', help='Absolute path for input csv file')
    parser.add_argument('--output-csv', dest='output_csv', help='Absolute path for output csv file')
    args = parser.parse_args()
    if args.output_csv:
        output_file = open(args.output_csv, mode='w')
    else:
        output_file = sys.stdout
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['image1','image2','similar','elapsed'])
    with open(args.input_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                try:
                    start_time = time.time()
                    similarity = image_similiarity_score(row[0],row[1])
                    elapsed_time = time.time() - start_time
                    csv_writer.writerow([row[0],row[1],similarity/100,elapsed_time])
                except (FileNotFoundError, IOError):
                    csv_writer.writerow([row[0],row[1],None,None])

if __name__ == "__main__":
    main()