#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import urllib,urllib2,cookielib,socket  
# url = "http://www.nbtong.com.cn/tis-web/callservice.do?service=SmartBusService"
url = "http://119.15.136.4:28090/ubossInterface/mcallremoteservice.do?&jsonpcallback=jQuery172020148572290807276_1401665658506&PG_Data=%7B%22SERVICE_NAME%22%3A%22BusInfoService%22%2C%22method%22%3A%22getBusInfoCache%22%2C%22LINE_NAME%22%3A%2223%E8%B7%AF%22%7D&_=1401672304229"
i_headers = {
"Host": "www.nbtong.com.cn",\
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0",\
"Accept": "application/xml, text/xml, */*; q=0.01",\
"Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",\
"Accept-Encoding": "gzip, deflate",\
"DNT": "1",\
"Content-Type":"text/xml; charset=UTF-8",\
"X-Requested-With": "XMLHttpRequest",\
"Referer":"http://www.nbtong.com.cn/tis-web/citytrip/WirelessBus.jsp",\
"Connection":"keep-alive",\
"Pragma":"no-cache",\
"Cache-Control":"no-cache"}

# params =  '<?xml version="1.0" encoding="UTF-8"?><uboss><ServiceName>SmartBusService</ServiceName><Data><sSEARCHNAME>10路</sSEARCHNAME><smethod>queryStationByPath</smethod><suboss_referer_url>http://www.nbtong.com.cn/tis-web/citytrip/WirelessBus.jsp</suboss_referer_url></Data></uboss>'

req = urllib2.Request(url,  headers=i_headers)
req.get_method = lambda: 'GET'

try:  
    page = urllib2.urlopen(req)  
    out = page.read()
    print out
    # with open("out.xml", "w") as f:
        # f.write(out)
# like get  
#url_params = urllib.urlencode({"a":"1", "b":"2"})  
#final_url = url + "?" + url_params  
#print final_url  
#data = urllib2.urlopen(final_url).read()  
#print "Method:get ", len(data)  
except urllib2.HTTPError as e:  
    print "Error Code:", e.code  
except urllib2.URLError as e:  
    print "Error Reason:", e.reason  
