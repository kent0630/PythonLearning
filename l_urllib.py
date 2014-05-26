#!/usr/bin/python
# encoding=utf-8
import os
import urllib, httplib  
url = "http://www.baidu.com"  
def use_urllib():  
    """
    urllib.urlopen(url[, data[, proxies]]) :
        url: 表示远程数据的路径
        data: 以post方式提交到url的数据
        proxies:用于设置代理

urlopen返回对象提供方法：
    -read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
    -info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
    -getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
    -geturl()：返回请求的url 
    """
  # httplib.HTTPConnection.debuglevel = 1   
    page = urllib.urlopen(url)  
    print "status:", page.getcode() #200请求成功,404  
    print "url:", page.geturl()  
    print "head_info:\n",  page.info()  
    print "Content len:", len(page.read())  

def urllib_other_functions():  
    """
    urllib.quote(string[, safe])：对字符串进行编码。参数safe指定了不需要编码的字符
    urllib.unquote(string) ：对字符串进行解码
    urllib.quote_plus(string [ , safe ] ) ：与urllib.quote类似，但这个方法用'+'来替换' '，而quote用'%20'来代替' '
    urllib.unquote_plus(string ) ：对字符串进行解码
    urllib.urlencode(query[, doseq])：将dict或者包含两个元素的元组列表转换成url参数。例如 字典{'name': 'wklken', 'pwd': '123'}将被转换为"name=wklken&pwd=123"
    urllib.pathname2url(path)：将本地路径转换成url路径
    urllib.url2pathname(path)：将url路径转换成本地路径
    """
    astr = urllib.quote('this is "K"')  
    print astr  
    print urllib.unquote(astr)  
    bstr = urllib.quote_plus('this is "K"')  
    print bstr  
    print urllib.unquote(bstr)  

    params = {"a":"1", "b":"2"}  
    print urllib.urlencode(params)  

    l2u = urllib.pathname2url(r'd:\a\test.py')  
    print l2u   
    print urllib.url2pathname(l2u)  

############################################
# 下载远程数据
# urlretrieve方法直接将远程数据下载到本地
# urllib.urlretrieve(url[, filename[, reporthook[, data]]])：
    # filename指定保存到本地的路径（若未指定该，urllib生成一个临时文件保存数据）
    # reporthook回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调
    # data指post到服务器的数据
# 该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。
############################################
def  callback_f(downloaded_size, block_size, romote_total_size):  
    per = 100.0 * downloaded_size * block_size / romote_total_size  
    if per > 100:  
        per = 100   
    print "%.2f%%"% per   
  
def use_urllib_retrieve():  
  local = os.path.join(os.path.abspath("./"), "a.html")  
  print local  
  for i in urllib.urlretrieve(url, local, callback_f): 
    print i

if __name__ == '__main__':
    # use_urllib()
    # urllib_other_functions()
    use_urllib_retrieve()
