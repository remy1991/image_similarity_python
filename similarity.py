from PIL import Image
import csv, time, sys, git, argparse, imagehash

def check_for_updates():
    repo = git.Repo(search_parent_directories=True)
    if repo.head.ref.object.hexsha != repo.head.object.hexsha:
        return 'There is a new update. Please perform "git pull" first'

def image_similiarity_score(image_a, image_b):
    hash1 = imagehash.average_hash(Image.open(image_a))
    hash2 = imagehash.average_hash(Image.open(image_b))
    return (hash1-hash2)

if __name__ == "__main__":
    check_for_updates()
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-csv', required=True, dest='input_csv')
    parser.add_argument('--output-csv', dest='output_csv')
    args = parser.parse_args()
    input_csv_path, output_csv_path = args.input_csv, args.output_csv
    if output_csv_path:
        output_csv_file = open(output_csv_path, mode='w')
        csv_writer = csv.writer(output_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['image1','image2','similar','elapsed'])
    print('image1,image2,similar,elapsed')
    with open(input_csv_path) as csv_file:
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
                    if output_csv_path:
                        csv_writer.writerow([row[0],row[1],similarity/100,elapsed_time])
                    print('{0},{1},{2},{3}'.format(row[0],row[1],similarity/100,elapsed_time))
                    # line_count += 1
                except:
                    if output_csv_path:
                        csv_writer.writerow([row[0],row[1]])
                    print('{0},{1}'.format(row[0],row[1]))