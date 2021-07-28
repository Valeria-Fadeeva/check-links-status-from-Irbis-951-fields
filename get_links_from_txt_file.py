#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, 'modules')
import vf_fso


i = 0
link_cnt = 0
mfn = 0
link_list = []

filename_db = 'db/books.txt'
filename_result = 'links/links.txt'

fdb_chkd = vf_fso.chk_path(filename_db)
fr_chkd = vf_fso.chk_path(filename_result)

if fdb_chkd == False or fr_chkd == False:
    print('Exit since files do not exist')
    exit()

with open(filename_db, mode='r', encoding='utf-8') as fr:
    for line in fr:
        i += 1
        
        if line.startswith('*****'):
            mfn += 1
        
        if line.startswith('#951'):
            elements = line.split('^')
            for j in elements:
                if j.startswith('I'):
                    res = j
                    if len(res) > 7:
                        link_cnt += 1
                        link_list.append(res[1:].strip())
    fr.close()

link_list.sort()

text = ''
for link in link_list:
    text += link + '\n'
    
with open(filename_result, mode='w+', encoding='utf-8') as fw_plus:
    fw_plus.write(text)
    fw_plus.close()
    
print('MFN', mfn)
print('Link count', link_cnt)
print('Created', filename_result)
