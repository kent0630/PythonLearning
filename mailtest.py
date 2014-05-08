#!/usr/bin/python
#encoding=utf-8

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 定义发送列表
mailto_list=["xuxiaofeng.nb@ccb.com"]
 
# 设置服务器名称、用户名、密码
mail_host = "36.0.191.1"
mail_user = ""
mail_pass = ""
 
# 发送邮件函数
def send_mail(mail_from,to_list, sub, context):
	'''
	to_list: 发送给谁
	sub: 主题
    context: 内容
    send_mail("xxx.nb@ccb.com","sub","context")
    '''
	msg = MIMEMultipart()  #支持附件

	# 如果html格式，将_subtpye设成html
	# msg = MIMEText(context, _subtype='plain', _charset='utf-8') 

	context += '\n\r'
	txt1 = MIMEText(context, _subtype='plain', _charset='utf-8')
	# txt1.replace_header('Content-Transfer-Encoding', 'quoted-printable')  #否则邮件原文看不懂，但并不影响读信
	msg.attach(txt1)

	# att1=base64.encodestring(open('output.txt','rb').read())  #附件base64编码
	att1=open('output.txt','rb').read() 
	att1=MIMEText(att1)
	att1.replace_header('Content-Type','application/octet-stream;name="%s"' % Header('中文附件测试.txt','utf-8'))
	att1.add_header('Content-Disposition', 'attachment;filename="%s"' %Header('中文附件名测试.txt','utf-8'))
	msg.attach(att1)

	# att2=open('library.zip','rb').read()  
	# att2=MIMEText(att2)
	# att2.replace_header('Content-Type','application/octet-stream;name="%s"' % Header('lib.zip','utf-8'))
	# att2.add_header('Content-Disposition', 'attachment;filename="%s"' %Header('lib.zip','utf-8'))
	# msg.attach(att2)
	
	msg['Subject'] = Header(sub, 'utf-8')
	msg['From'] = Header(mail_from, 'utf-8')
	msg['To'] = ";".join(to_list) 
	try: 
		send_smtp = smtplib.SMTP()
		send_smtp.connect(mail_host)
		#send_smtp.login(mail_user, mail_pass)
		send_smtp.sendmail(mail_from, to_list, msg.as_string())
		send_smtp.close()
		return True
	except Exception, e:
		print str(e)
		return False

if __name__ == '__main__':
    if (True == send_mail("徐小峰<xuxiaofeng.nb@ccb.com>",mailto_list, "鎏国你好", "你好")): 
        print (u"邮件发送成功")
    else: 
        print (u"邮件发送失败")
