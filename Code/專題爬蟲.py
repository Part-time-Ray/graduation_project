import requests
import re
import os
import glob
import json
print('hi')
floder_path = r'C:\Users\wangr\OneDrive\桌面\專題'
get = {}
for root, dirs, files in os.walk(floder_path):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='UTF-8') as f:
                    html = f.read()
            except:
                try:
                    with open(file_path, 'r', encoding='gbk') as f:
                        html = f.read()
                except:
                    try:
                        with open(file_path, 'r', encoding='big5') as f:
                            html = f.read()
                    except:
                        continue
            for text in re.findall(r'标签:.*?<a class="clink".*?>(.*?)</a>.*?摘要: (.*?)<', html, flags=re.DOTALL):
                text = list(text)
                text[1] = re.sub(r'&amp;nbsp;', '', text[1])
                text[1] = re.sub(r'\u200c', '', text[1])
                get[text[0]] = text[1]
print('Ivan', get['Ivan'], sep='\n\n')

    