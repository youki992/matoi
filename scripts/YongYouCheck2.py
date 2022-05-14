import requests
from scripts import printColor

def YOCheck(ip):
    link=str(ip)+'/fs/'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}#伪装成浏览器访问
    r=requests.get(link,headers=headers)
    if 'username' and 'password' in r.text:
        pc = printColor.Colors()
        pc.print_red_text('用友NCCloud FS文件管理SQL注入: '+link)
        return 1
    else:
        print("用友NCCloud is not vuln!")
        #print(r.text)