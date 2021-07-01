# coding=utf-8

import requests
import threading


def get_status(url):
    r = requests.get(url, allow_redirects=False)
    return r.status_code


def start():
    f = open('./dic/sensitive.txt')
    url = []
    lines = f.readlines()
    for text in lines:
        text = text.rstrip('\n')
        #print(text)
        url.append('https://www.youkilearning.top'+'/'+text)
    print(url)
    f.close()
    for i in url:
        print(i)
        status = get_status(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        r = requests.get(i, headers=headers)
        html = r.text
        if status == 200 and '403 Forbidden' and 'Forbidden' not in html:
            print("Exist：敏感信息 "+i)
        #else:
            #print("Not Exist")

def main():
    t = threading.Thread(target=start)
    t.start()


if __name__ == "__main__":
    main()