#!/usr/bin/python
# encoding=utf-8
import logging
import logging.config
from logging.handlers import RotatingFileHandler
# 初始化Logger,filemode='w'每次清空日志重写，'a'追加重写
logging.basicConfig(level    = logging.DEBUG,
                    format   = '%(asctime)s %(name)-12s %(levelname)-8s [%(filename)s line:%(lineno)d] %(message)s',
                    datefmt  = '%Y-%m-%d %H:%M:%S',
                    filename = 'log/testlog.log',
                    filemode = 'w')
# 定义控制台日志
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# 定义了一个 最大10m，可备份5个的日志
rthandler = RotatingFileHandler('myapp.log', maxBytes=10*1024*1024, backupCount=5)
rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(rthandler)

# 通过配置文件配置日志输出
logging.config.fileConfig(u"/Users/xuxiaofeng/百度云同步盘/python/config/logger.conf")

logging.info('Jackdaws love my big sphinx of quartz.')
logger1 = logging.getLogger('myapp1')
logger2 = logging.getLogger('myapp2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')
logger2.critical('中文日志测试')
logger2.info('长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长长')
