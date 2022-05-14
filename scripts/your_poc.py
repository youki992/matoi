import requests
import time

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "PHPSESSID=hsbsup4h4duhlmqcrbt37j5u11"
}
headerss = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
payload = {}
dnslog = 'chobits.hsl35u.ceye.io'

def get_check():
    print('*'*10+'请输入poc名称、poc与返回包特征'+'*'*10)
    name = str(input())
    poc = str(input())
    show = str(input())
    for i in payload.keys():
        if i == name:
            print(name + ' poc名称重复')
            exit(0)
    payload[name] = poc
    print('*'*10+'是否启用ceye(dnslog)进行第三方检测回显'+'*'*10)
    print('*' * 5 + 'y/n' + '*' * 5)
    answer = str(input())
    print('*' * 10 + '请输入URL' + '*' * 10)
    url = str(input())
    switch = {'y': ceye,
              'n': norm,
              }
    switch.get(answer)(name,url,show)

def post_check():
    print('*'*10+'请输入poc名称、poc(poc以:q结尾)与返回包特征'+'*'*10)
    name = str(input())
    data = []
    input_ch = ''
    while True:
        input_ch = input()
        if (input_ch == ':q'):  # :q 为停止符
            break
        else:
            data.append(input_ch + '\n')

    #### 测试部分 ####
    # print(data)
    with open('test.txt', 'w')as fw:
        for item in data:
            fw.writelines(item)

    with open('test.txt', 'r')as fr:
        read_data = fr.read()
        #print(read_data)
    show = str(input())
    for i in payload.keys():
        if i == name:
            print(name + ' poc名称重复')
            exit(0)
    payload[name] = read_data
    print('*'*10+'是否启用ceye(dnslog)进行第三方检测回显'+'*'*10)
    print('*' * 5 + 'y/n' + '*' * 5)
    answer = str(input())
    print('*' * 10 + '请输入URL' + '*' * 10)
    url = str(input())
    switch = {'y': ceye_post,
              'n': norm_post,
              }
    switch.get(answer)(name,url,show)

def ceye(name,url,show):
    try:
        requests.packages.urllib3.disable_warnings()
        sends = requests.get(url=url+payload[name], headers=headers, timeout=20, verify=False)
    except:
        print(url + '访问失败，请到检查配置ceye.io的API或检查网络')

    time.sleep(3)
    try:
        check_dnslog = requests.get(
                url="http://api.ceye.io/v1/records?token=180a5ca69564997af21e4f109007f595&type=dns&filter=",
                headers=headerss)
            # http://api.ceye.io/v1/records?token={token}&type={dns|http}&filter={filter}，详细使用请阅http://ceye.io/api
    except:
        print('API调用失败，重新执行')
    if check_dnslog.text.find(dnslog) >= 0:
        print('[+]' + url + ' is vul')
        print('[+]payload: ' + name + '&' + payload[name])
            # print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        print('[-]' + url + ' is not vul to payload:' + name)

def ceye_post(name,url,show):
    try:
        requests.packages.urllib3.disable_warnings()
        sends = requests.post(url=url, headers=headers, data=payload[name], timeout=20, verify=False)
    except:
        print(url + '访问失败，请检查配置ceye.io的API或检查网络')

    time.sleep(3)
    try:
        check_dnslog = requests.get(
                url="http://api.ceye.io/v1/records?token=180a5ca69564997af21e4f109007f595&type=dns&filter=",
                headers=headerss)
            # http://api.ceye.io/v1/records?token={token}&type={dns|http}&filter={filter}，详细使用请阅http://ceye.io/api
    except:
        print('API调用失败，重新执行')
    if check_dnslog.text.find(dnslog) >= 0:
        print('[+]' + url + ' is vul')
        print('[+]payload: ' + name + '&' + payload[name])
            # print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        print('[-]' + url + ' is not vul to payload:' + name)

def norm(name,url,show):
    try:
        #print(name)
        #print(url+payload[name])
        #print(show)
        requests.packages.urllib3.disable_warnings()
        sends = requests.get(url=url+payload[name], headers=headers, timeout=20, verify=False)
        #print('sends:' + sends.text)
    except:
        print(url + '访问失败，请检查URL或网络')

    time.sleep(3)
    try:
        if show in sends.text:
            print('[+]' + url + ' is vul')
            print('[+]payload: ' + name + '&' + payload[name])
        else:
            print('[-]' + url + ' is not vul to payload:' + name)
    except:
        print('访问失败，重新执行')

def norm_post(name,url,show):
    try:
        #print(name)
        #print(url+payload[name])
        #print(show)
        requests.packages.urllib3.disable_warnings()
        print('*'*10+'开始请求'+'*'*10)
        sends = requests.post(url=url, headers=headers, data=payload[name], timeout=20, verify=False)
        #print('sends:' + sends.text)
    except:
        print(url + '访问失败，请检查URL或网络')

    time.sleep(3)
    try:
        if show in sends.text:
            print('[+]' + url + ' is vul')
            print('[+]payload: ' + name + '&' + payload[name])
        else:
            print('sends:'+sends.text)
            print('[-]' + url + ' is not vul to payload:' + name)
    except:
        print('访问失败，重新执行')


def start():
    print('启用dnslog接收可能会有延迟，为了减少误报,根据实际情况修改headers。')
    print('------------------------------------开始检测------------------------------------')
    print('-'*10 + '请输入poc类型 get/post' + '-'*10)
    type = str(input())
    switch = {'get': get_check,
          'post': post_check,
            }
    switch.get(type)()
