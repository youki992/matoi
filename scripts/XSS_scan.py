import optparse
from selenium import webdriver
import threading

def check_xss(url):
    driver = webdriver.Chrome()
    with open("./scripts/dic/xsspayload.txt",encoding="utf-8") as file:
        payloads = file.readlines()
        for payload in payloads:
            payload = payload.strip()
            try:
                driver.get(url + payload)
                message = driver.switch_to.alert.text
                if message is not None:
                    print("[+]url:"+url+",payload is:" + payload)
            except:
                pass