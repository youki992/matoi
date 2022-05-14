import re,random
import sys
from lib.core import Download

sys.path.append("..")
import lib.core.Download
def sqlcheck(url):
    """
    if(not url.find("?")):
        return False
    """
    if(url.find("?")):
        result = re.findall(".*\?(.*)=.*",url)
        original_url = re.findall("^http://.*?(?=\?id=)", url)
        for x in result:
            id = x
        for x in original_url:
            original_url = x
    Downloader = Download.Downloader()
    #print("开始SQL检测")
    TESTS = (" AND %d=%d", " OR NOT (%d=%d)")
    DBMS_ERRORS = {# regular expressions used for DBMS recognition based on error message response
    "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
    "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
    "Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
    "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
    "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
    "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
    "SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
    "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
}
    _content = Downloader.get(url)
    #print(_content)
    for (dbms, regex) in ((dbms, regex) for dbms in DBMS_ERRORS for regex in DBMS_ERRORS[dbms]):
        #print("开始SQL检测1")
        if(re.search(regex,_content)):
            #print("开始SQL检测2")
            return True
    content = {}
    for test_payload in TESTS:
        #print("开始SQL检测3")
        RANDINT = random.randint(1, 2)
        _url = original_url + '?' + id + '=' + test_payload%(RANDINT,RANDINT)
        content["true"] = Downloader.get(_url)
        _url = original_url + '?' + id + '=' + test_payload%(RANDINT,RANDINT+1)
        content["false"] = Downloader.get(_url)
        for (dbms, regex) in ((dbms, regex) for dbms in DBMS_ERRORS for regex in DBMS_ERRORS[dbms]):
            # print("开始SQL检测1")
            if (re.search(regex, content["true"])):
                # print("开始SQL检测2")
                return True
            if (re.search(regex, content["false"])):
                # print("开始SQL检测2")
                return True