#!/usr/bin/env python3

import os


def chk_path(path):
    """[Checking path exists]

    Args:
        path ([str]): [path to files]

    Returns:
        [bool]: [be or not to be]
    """

    chkd = []

    if os.path.exists(os.path.split(path)[0]):
        chkd.append(1)
    else:
        print(
            'Directory "{}" doesn\'t exist'.format(os.path.split(path)[0])
        )

        os.mkdir(os.path.split(path)[0])

        chkd.append(0)

    if os.path.exists(path):
        chkd.append(1)
    else:
        print(
            'File "{}" doesn\'t exist'.format(path)
        )

        with open(path, mode='w', encoding='utf-8') as fw:
            fw.close()

        chkd.append(0)

    if sum(chkd) <= 1:
        return False
    else:
        return True
