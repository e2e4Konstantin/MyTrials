# https://realpython.com/command-line-interfaces-python-argparse/

import datetime
import argparse
from pathlib import Path




parser = argparse.ArgumentParser(prog="ls", description="List the content of a directory",  epilog="Thanks for using %(prog)s! :)", )

print(parser)

parser.add_argument("path")
parser.add_argument("-l", "--long", action="store_true")

parser.add_argument("site")


args = parser.parse_args()
print(args)

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)
#
# for entry in target_dir.iterdir():
#     print(entry.name)


def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name

for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))