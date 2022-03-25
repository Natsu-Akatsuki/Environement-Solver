import pysed
import glob
import argparse
from pathlib import Path


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="arg parser")

    parser.add_argument('--src', type=str, default=None, help='specify the config for evaluation')
    args = parser.parse_args()

    src_dir = str(Path(args.src).resolve())

    pattern_file = "replace/opencv_replace.txt"
    api_replace(src_dir, "**/*.cpp", pattern_file)

    pattern_file = "replace/opencv_replace.txt"
    api_replace(src_dir, "**/*.cc", pattern_file)

    pattern_file = "replace/CMakeLists_replace.txt"
    api_replace(src_dir, "**/CMakeLists.txt", pattern_file)

    pattern_file = "replace/ros_replace.txt"
    api_replace(src_dir, "**/*.cpp", pattern_file)