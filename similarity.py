from PIL import Image
import csv, time, git, sys, argparse, imagehash

def check_for_updates():
    repo = git.Repo(search_parent_directories=True)
    repo.remotes.origin.fetch()
    if len(list(repo.iter_commits('master..master@{u}'))) > 0:
        return 'There is a new update. Please perform "git pull" first'

def image_similiarity_score(image_a, image_b):
    hash1 = imagehash.average_hash(Image.open(image_a))
    hash2 = imagehash.average_hash(Image.open(image_b))
    return abs(hash1-hash2)

def main():
    if check_for_updates():
        print(check_for_updates())
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-csv', required=True, dest='input_csv')
    parser.add_argument('--output-csv', dest='output_csv')
    args = parser.parse_args()
    if args.output_csv:
        output_file = open(args.output_csv, mode='w')
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['image1','image2','similar','elapsed'])
    else:
        output_file = sys.stdout
        output_file.write('image1,image2,similar,elapsed\n')
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
                    if args.output_csv:
                        csv_writer.writerow([row[0],row[1],similarity/100,elapsed_time])
                    output_file.write('{0},{1},{2},{3}\n'.format(row[0],row[1],similarity/100,elapsed_time))
                    # line_count += 1
                except FileNotFoundError:
                    if args.output_csv:
                        csv_writer.writerow([row[0],row[1]])
                    output_file.write('{0},{1}\n'.format(row[0],row[1]))

if __name__ == "__main__":
    main()