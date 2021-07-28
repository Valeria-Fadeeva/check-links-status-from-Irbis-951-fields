#!/usr/bin/env python3


def create_file(filename):
    try:
        fw = open(filename, mode='w', encoding='utf-8')
        fw.write('')
        fw.close()
        return True
    except OSError as e:
        print(e)
        exit()
