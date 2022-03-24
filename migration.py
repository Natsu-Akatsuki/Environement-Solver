import pysed
import glob


def api_replace(src_dir, reg, pattern_file):
    match_files = glob.glob(src_dir + reg, recursive=True)
    with open(pattern_file, "r") as sources:
        replaces = sources.readlines()[1:]
    for file in match_files:
        for replace in replaces:
            replace = replace.strip().split()
            pysed.replace(replace[0], replace[1], file)


if __name__ == '__main__':
    src_dir = ""

    pattern_file = "replace/opencv_replace.txt"
    api_replace(src_dir, "**/*.cpp", pattern_file)

    pattern_file = "replace/opencv_replace.txt"
    api_replace(src_dir, "**/*.cc", pattern_file)

    pattern_file = "replace/CMakeLists_replace.txt"
    api_replace(src_dir, "**/CMakeLists.txt", pattern_file)
