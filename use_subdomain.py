import os

def start(url_input):
    url = url_input
    command = 'python subdomain.py -u '+url
    print(command)
    os.system(command)

#start('baidu.com')