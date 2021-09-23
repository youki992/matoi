import os

def start(url):
    command = 'python TideFinger.py -u '+url
    #print(command)
    os.system(command)

#start('baidu.com')