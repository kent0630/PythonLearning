#!/usr/bin/python
#coding=utf-8
"""
ConfigParser 用法:
    1、config=ConfigParser.ConfigParser()  
    创建ConfigParser实例  
      
    2、config.sections()  
    返回配置文件中节序列  
      
    3、config.options(section)  
    返回某个项目中的所有键的序列  
      
    4、config.get(section,option)  
    返回section节中，option的键值  
      
    5、config.add_section(str)  
    添加一个配置文件节点(str)  
      
    6、config.set(section,option,val)  
    设置section节点中，键名为option的值(val)  
      
    7、config.read(filename)  
    读取配置文件  
      
    8、config.write(obj_file)  
    写入配置文件  
"""
import ConfigParser
      
def writeConfig(filename):  
    config = ConfigParser.ConfigParser()  
    # set db  
    section_name = 'db'  
    config.add_section(section_name)
    config.set(section_name, 'dbname', 'MySQL')  
    config.set(section_name, 'host', '127.0.0.1')  
    config.set(section_name, 'port', '80')  
    config.set(section_name, 'password', '123456')  
    config.set(section_name, 'databasename', 'test')  
  
    # set app
    section_name = 'app'  
    config.add_section(section_name)  
    config.set(section_name, 'loggerapp', '192.168.20.2')  
    config.set(section_name, 'reportapp', '192.168.20.3')  
  
    # write to file  
    config.write(open(filename, 'w'))  
  
def updateConfig(filename, section, **keyv):
    config = ConfigParser.ConfigParser()  
    config.read(filename)
    print config.sections()

    for section in config.sections():
        print "[",section,"]"  
        items = config.items(section)
        for item in items:  
            print "\t", item[0],"=",item[1]

    # has_option  
    print config.has_option("dbname", "MySQL")  
    print config.has_option("db", "dbname")  
    print config.set("db", "dbname", "Oracle")

    for key in keyv:  
        print "\t",key," = ", keyv[key]  
        print config.set("app", key, keyv[key])

    config.write(open(filename, 'w'))
    
  
if __name__ == '__main__':  
    file_name = 'config/test.ini'  
    writeConfig(file_name)  
    updateConfig(file_name, 'app', reportapp = '192.168.100.100')
