#!/usr/bin/env python3

import sys
import requests
from time import sleep
sys.path.insert(0, 'modules')
import vf_fso

filename_links = 'links/links.txt'

fn = {
        'other': 'links/text_other.txt',
        '200': 'links/text_200.txt', 
        '403': 'links/text_403.txt'
    }

for f in fn:
    if vf_fso.create_file(fn[f]):
        print('created', fn[f])

with open(filename_links, mode='r', encoding='utf-8') as fr:
    fr_plus_200 = open(fn['200'], mode='r+', encoding='utf-8')
    fr_plus_403 = open(fn['403'], mode='r+', encoding='utf-8')
    fr_plus_other = open(fn['other'], mode='r+', encoding='utf-8')
    
    i = 0
    for line in fr:
        i += 1
        link =line.strip()
        r = requests.head(link)
        
        if r.status_code == 200:
            fr_plus_200.write(line)
            
        elif r.status_code == 403:
            fr_plus_403.write(line)
            
        else:
            fr_plus_other.write(line)
            
        print(i, r.status_code, link)
            
        sleep(0.01)
        
    fr.close()
    fr_plus_200.close()
    fr_plus_403.close()
    fr_plus_other.close()
