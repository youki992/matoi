import os

def start(url_input):
    url = url_input
    command = 'python dirscan.py -u '+url
    print(command)
    os.system(command)