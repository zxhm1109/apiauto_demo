'''
@File   :Logi.py
@BY     ：zhaofy
@data   :2019/12/19
'''
import logging.handlers
import sys, time

logger = logging.getLogger('__main__')
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
file_handler = logging.handlers.RotatingFileHandler(
    'D:\python_package\demo20191112\log\\' + sys.argv[0].split("/")[-1][:-3] + time.strftime('%Y%m%d%H%M%S',
                                                                                             time.localtime(
                                                                                                 time.time())) + '.log',
    maxBytes=1024 * 1024 * 10,
    backupCount=3, encoding='utf-8')
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler(sys.stdout)
formatter1 = logging.Formatter()
console_handler.formatter = formatter1
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def all_source():
    listss = ['extra', 'filesys', 'docdata', 'search', 'serotin', 'interpatient', 'general', 'assign', 'commucation',
              'interhosp', 'live', 'card', 'balance', 'action', 'asycstream', 'manage', 'goods', 'healthcheck', 'rpc',
              'tailor', 'physicalexam', 'sms', 'inform']
    return listss
