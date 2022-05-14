from flask import Flask, request
import requests
import datetime
import logging
import re

#预警推送，使用xray时再运行
app = Flask(__name__)

def push_wechat_group(content):
    hook='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=94a38c1e-0896-4a44-8441-8f399b9e8ed0'
    resp = requests.post(
        hook,
        json={"msgtype": "markdown",
        "markdown": {"content": content}})
    if resp.json()["errno"] != 0:
        raise ValueError("push wechat group failed, %s" % resp.text)

@app.route('/webhook', methods=['POST'])
def xray_webhook():
    vuln = request.json
    print(vuln)
    #print(vuln["data"])
    #print(vuln["target"]["url"])
    content = """## xray 发现了新漏洞

url: {url}

插件: {plugin}

漏洞类型: {vuln_class}

请及时查看和处理
""".format(url=vuln["data"]["target"]["url"], plugin=vuln["data"]["plugin"],
           vuln_class=vuln["type"] or "Default",
           )
    try:
        push_wechat_group(content)
    except Exception as e:
        logging.exception(e)
    return 'ok'


if __name__ == '__main__':
    app.run()