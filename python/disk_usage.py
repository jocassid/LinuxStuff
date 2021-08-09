#!/usr/bin/env python3

from pathlib import Path
from subprocess import PIPE, Popen, run


def system_summary():

    ignore_dirs = {
        'boot', 'cdrom', 'dev',
        'media', 'mnt', 'proc',
    }

    cannot_read_count = 0

    for child in Path('/').iterdir():
        if child.name in ignore_dirs:
            continue
        if not child.is_dir():
            continue
        print(repr(child.absolute()))
        popen = Popen(
            [
                'du',
                # '--max-depth=1',
                str(child.absolute())
            ],
            stdout=PIPE,
            stderr=PIPE,
            encoding='utf8',
        )
        while True:
            line = popen.stdout.readline()
            if line:
                print("stdout", repr(line))
                pieces = line.split()
                print('pieces', pieces)
            line = popen.stderr.readline()
            if line:
                if line.startswith('du: cannot read directory'):
                    cannot_read_count += 1
                print("stderr", repr(line))
            if popen.poll():
                break

        break

    print("")








if __name__ == '__main__':
    system_summary()