#!/usr/bin/python
# encoding=utf-8

############ 读文件 ################
# open默认的第二个参数是'r',代表读文件
try:
    file_object = open('out.txt')
    try:
        # all_the_text = file_object.read( )
        chunk = file_object.read(100) #读取100字节
        # print chunk
        list_of_all_the_lines = file_object.readlines()
        for line in list_of_all_the_lines:
            pass
            # print line
        # print all_the_text
    finally:
        file_object.close()
except IOError,e:
   print e.message 
finally:
    pass

############ 写文件 ################
output = open('data/output.txt', 'w')
# a 追加写文件
# output = open('data', 'a')
output.write("文件的内容111\nrksjdfsjdf\n")
output.writelines("sdfsdf")
output.close()

########### 构建File对象 ###########
f = file('data/output.txt', 'a')
print f.__class__
print f.name
print f.newlines
print f.encoding
print f.mode
print f.fileno
f.close()
