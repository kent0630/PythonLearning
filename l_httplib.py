# encoding=utf-8

# 使用httplib抓取：
# 表示一次与服务器之间的交互，即请求/响应

# httplib.HTTPConnection ( host [ , port [ ,strict [ , timeout ]]] )

    # host表示服务器主机
    # port为端口号，默认值为80
    # strict的 默认值为false， 表示在无法解析服务器返回的状态行时(status line) （比较典型的状态行如： HTTP/1.0 200 OK ），是否抛BadStatusLine 异常
    # 可选参数timeout 表示超时时间。


# HTTPConnection提供的方法：

    # HTTPConnection.request ( method , url [ ,body [ , headers ]] )
    # 调用request 方法会向服务器发送一次请求

    # method 表示请求的方法，常用有方法有get 和post ；
    # url 表示请求的资源的url ；
    # body 表示提交到服务器的数据，必须是字符串（如果method是”post”，则可以把body 理解为html 表单中的数据）；
    # headers 表示请求的http 头。

    # HTTPConnection.getresponse ()
    # 获取Http 响应。返回的对象是HTTPResponse 的实例，关于HTTPResponse 在下面会讲解。

    # HTTPConnection.connect ()
    # 连接到Http 服务器。

    # HTTPConnection.close ()
    # 关闭与服务器的连接。

    # HTTPConnection.set_debuglevel ( level )
    # 设置高度的级别。参数level 的默认值为0 ，表示不输出任何调试信息。

# httplib.HTTPResponse
# HTTPResponse表示服务器对客户端请求的响应。往往通过调用HTTPConnection.getresponse()来创建，它有如下方法和属性：

    # HTTPResponse.read([amt])
    # 获取响应的消息体。如果请求的是一个普通的网页，那么该方法返回的是页面的html。可选参数amt表示从响应流中读取指定字节的数据。

    # HTTPResponse.getheader(name[, default])
    # 获取响应头。Name表示头域(header field)名，可选参数default在头域名不存在的情况下作为默认值返回。

    # HTTPResponse.getheaders()

    # 以列表的形式返回所有的头信息。
    # - HTTPResponse.msg
    # 获取所有的响应头信息。

    # HTTPResponse.version
    # 获取服务器所使用的http协议版本。11表示http/1.1；10表示http/1.0。

    # HTTPResponse.status
    # 获取响应的状态码。如：200表示请求成功。

    # HTTPResponse.reason
    # 返回服务器处理请求的结果说明。一般为”OK”

def use_httplib():  
    import httplib  
    conn = httplib.HTTPConnection("www.baidu.com")  
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",  
             "Accept": "text/plain"}  
    conn.request("GET", "/", headers = i_headers)
    r1 = conn.getresponse()  

    print "version:", r1.version  
    print "reason:", r1.reason  
    print "status:", r1.status  
    print "msg:", r1.msg  
    print "headers:", r1.getheaders()  
    data = r1.read()  
    print len(data)  
    conn.close()  
  
if __name__ == "__main__":  
    use_httplib()  
