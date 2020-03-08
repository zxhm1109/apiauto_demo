'''
@File   :Run.py
@BY     ：zhaofy
@data   :2019/12/27
'''

from Config.case_html import createHtml
from Config.ExcelRW import Read_Excel
from Config.Logi import logger
import datetime, time, os
from Case.test_interface import testinterface
from Config.case_html import createHtml
from common.SendEmail import mail

def run_case(source):
    starttime = datetime.datetime.now()
    date = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    listid, listmodule, listname, listhost, listurl, listmethod, listheader, listparmas, listexpect, listisactive,Skipped,case_num = Read_Excel().get_excel(
        source)
    listrelust, list_fail, list_pass, list_json = testinterface()
    filepath = os.path.join('D:\python_package\demo20191112' + ('\\test_Report\\%s-result.html' % date))
    try:
        open(filepath,mode='x')
    except:
        pass
    endtime = datetime.datetime.now()
    report=createHtml(titles=u'测试报告', filepath=filepath, starttime=starttime,
               endtime=endtime, passge=list_pass, fail=list_fail,
               id=listid, name=listname, key=listmodule, coneent=listparmas, url=listurl, meth=listmethod,
               yuqi=listexpect, json=list_json, relusts=listrelust, amount=case_num,Skipped=Skipped)
    contec = u'http接口自动化测试完成，测试通过:%s,测试失败：%s,详情见：%s' % (
        list_pass, list_fail,filepath)
    logger.info(contec)
    mail(report)


if __name__ == '__main__':
    source='physicalexam'
    run_case(source)

