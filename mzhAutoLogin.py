# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 15:19:16 2015

@author: Administrator
"""

import os
import urllib2
import urllib
import cookielib
import cookielib
import Image
#from pytesser import * 
url='http://www.cqumzh.cn/bbs/logging.php?action=login&loginsubmit=true&userlogin=true'

#request.add_header('User-Agent', 'fake-client')
#
cookiejar=cookielib.CookieJar()
urlopener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
urllib2.install_opener(urlopener)
urlopener.addheaders.append(('Referer', 'http://www.cqumzh.cn/bbs/logging.php?action=login'))
urlopener.addheaders.append(('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'))
urlopener.addheaders.append(('Host', 'www.cqumzh.cn'))
urlopener.addheaders.append(('User-Agent', 'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1); Trident/5.0'))
urlopener.addheaders.append(('Connection', 'Keep-Alive'))
urlopener.addheaders.append(('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'))
request = urllib2.Request('http://www.cqumzh.cn/bbs/logging.php?action=login')
response = urlopener.open(request)
print response.read()
#urlopener.addheaders.append(('Accept-Encoding', 'gzip, deflate'))
print cookiejar
print 'XXX Login......'
imgurl=r'http://www.cqumzh.cn/bbs/seccode.php'
#print urlopener.open(imgurl).read()
outfile=open(r'./code.jpeg', 'wb')
ax=urlopener.open(urllib2.Request(imgurl)).read()
outfile.write(ax)
outfile.close()
authcode=raw_input('Please enter the authcode:')
print cookiejar

#设置cookie的值，因为post request head  需要 返回 cookie (不是cookies ，是将cookies的格式处理后的值)  
cookies = ''
 #这里要从
for index, cookie in enumerate(cookiejar):
   #print '[',index, ']';
   #print cookie.name;
   #pr(www.111cn.net)int cookie.value;
   #print "###########################"
   cookies = cookies+cookie.name+"="+cookie.value+";";
   print "###########################"
   cookie = cookies[:-1]
   print "cookies:",cookie
   
authcode=raw_input('Please enter the authcode:')
# Send login/password to the site and get the session cookie
#values={'login_id':username, 'opl':'op_login', 'login_passwd':password, 'login_check':authcode}
values2={'formhash':'be711575',
'referer':'http://www.cqumzh.cn/bbs/index.php?frameon=no',
'loginfield':'username',
'questionid':0,
'seccodeverify':authcode,
'verifyimgid':'432bb7cac8a262cdea28cb357545d50a',
'ghostcrc':'a0d05ed4d',
'directpg':	'http://localhost/index.php',
'username':	'用户名',
'loginmode'	:'invisible',
'password'	:'密码',
'cookietime':'0',
'questionid':	0,
'answer':''	,
'loginsubmit':	'true'
}

data=urllib.urlencode(values2)
strtemp=cookie+'; AbK_frameon=yes; AbK_onlineusernum=129; AJSTAT_ok_pages=2; AJSTAT_ok_times=1; bdshare_firstime=1426057940711';
print strtemp
mheaders={
'Host':	'www.cqumzh.cn',
'User-Agent':	'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
'Accept'	:'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language':	'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':	'gzip, deflate',
'Referer':	'http://www.cqumzh.cn/bbs/logging.php?action=login',
'Cookie':	strtemp,
'Content-Type':	'application/x-www-form-urlencoded',
'Content-Length'	:'356'
}
#print data
urlcontent=urlopener.open(urllib2.Request(url,data))#,mheaders
page=urlcontent.read()
print page
url2="http://www.cqumzh.cn/bbs/forumdisplay.php?fid=223"
urlcontent=urlopener.open(urllib2.Request(url2))#,mheaders
page=urlcontent.read()
print page
