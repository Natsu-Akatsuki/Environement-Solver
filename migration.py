import argparse
import glob
from pathlib import Path
from easydict import EasyDict
import pysed
import yaml


def api_replace(src_dir, posix, regexes):
    match_files = glob.glob(src_dir + posix, recursive=True)
    for file in match_files:
        for regex in regexes:
            regex = regex.strip().split(maxsplit=1)
            pysed.replace(regex[0], regex[1], file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="arg parser")
    # todo: add hint
    parser.add_argument("--cfg", type=str, default=None, help="specify the reg config for replacing")
    args = parser.parse_args()

    cfg = args.cfg
    with open(cfg, 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    cfg = EasyDict(cfg)

    for i in range(len(cfg.FILE)):
        replace = cfg.FILE[i].REPLCAE
        dir = replace.DIR
        posix = replace.POSIX
        regex = replace.REGEX

        dir = str(Path(dir).resolve())
        api_replace(dir, posix, regex)
