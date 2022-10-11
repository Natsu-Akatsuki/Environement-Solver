import argparse
import csv
import glob
from pathlib import Path

import pysed


def api_replace(src_dir, posix, regexes):
    match_files = glob.glob(src_dir + posix, recursive=True)
    for file in match_files:
        for regex in regexes:
            pysed.replace(regex[0], regex[1], file)


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="arg parser")
    # todo: add hint
    parser.add_argument("-c", "--cfg", nargs='+', help="specify the reg configs for replacing", required=True)

    csv_files = parser.parse_args()._get_kwargs()[0][1]

    for csv_file in csv_files:
        with open(csv_file) as f:
            csv_reader = list(csv.reader(f))

            search_dir = csv_reader[0][1]
            file_patterns = csv_reader[1][1:]
            for file_pattern in file_patterns:

                regex = csv_reader[3:]
                search_dir = str(Path(search_dir).resolve())
                api_replace(search_dir, file_pattern, regex)
