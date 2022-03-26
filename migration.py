import argparse
import glob
from pathlib import Path

import pysed


def api_replace(src_dir, reg, pattern_file):
    match_files = glob.glob(src_dir + reg, recursive=True)
    with open(pattern_file, "r") as sources:
        replaces = sources.readlines()[1:]
    for file in match_files:
        for replace in replaces:
            replace = replace.strip().split(maxsplit=1)
            if replace[0][0] == "#":
                continue
            pysed.replace(replace[0], replace[1], file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="arg parser")
    # todo: add hint
    parser.add_argument("--src", type=str, default=None, help="specify the src dir for replacing")
    parser.add_argument("--reg", type=str, default=None, help="specify the reg file for replacing")
    args = parser.parse_args()

    src_dir = str(Path(args.src).resolve())
    pattern_file = str(Path(args.reg).resolve())

    # pattern_file = "replace/common/opencv.replace"
    # api_replace(src_dir, "/**/*.cpp", pattern_file)
    #
    # pattern_file = "replace/common/opencv.replace"
    # api_replace(src_dir, "/**/*.cc", pattern_file)
    #
    # pattern_file = "replace/common/CMakeLists.replace"
    # api_replace(src_dir, "/**/CMakeLists.txt", pattern_file)

    api_replace(src_dir, "/**/*.cpp", pattern_file)
