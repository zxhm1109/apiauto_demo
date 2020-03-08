'''
@File   :test_interface.py
@BY     ：zhaofy
@data   :2019/12/27
'''

from Config.ExcelRW import Read_Excel
import requests, json
from common.RequestPlus import requestspuls
from Config.Logi import logger
from Config.Assert_zx import assert_in,assert_none,assert_parmas

listid, listmodule, listname, listhost, listurl, listmethod, listheader, listparmas, listexpect, listisactive, Skipped, case_num = Read_Excel().get_excel(
    'physicalexam')


def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust = []
    assert_p={}
    logger.info('开始执行case')
    for i in range(len(listurl)):
        if listhost[i][0:4] != 'https':
            listhost[i] = 'https://' + listhost[i]
        if listisactive[i] != 'N':
            header = {}
            header['Content-Type'] = listheader[i]
            listparmas[i]=assert_parmas(listparmas[i],assert_p)
            if listmethod[i] == 'post':
                parma = listparmas[i]
            else:
                parma = listparmas[i]
            api = requestspuls(url=listhost[i] + listurl[i], parmas=parma, method=listmethod[i], header=header)
            print(parma)
            re_assert = assert_in(asserqiwang=listexpect[i], fanhuijson=api)
            if re_assert.get('code') == 0:
                logger.info('Case执行成功>%s 参数:%s, url:%s ,返回:%s,预期:%s' % (listid[i],parma, listurl[i], api, listexpect[i]))
                listrelust.append('pass')
                list_json.append(api['message'])
                list_pass += 1
                if assert_none(api['results']):
                    assert_p[listid[i]]=api['results']
                continue
            else:
                logger.info('Case执行失败>%s 参数:%s, url:%s ,返回:%s,预期:%s' % (listid[i],parma, listurl[i], api, listexpect[i]))
                list_fail += 1
                list_json.append(api['message'])
                listrelust.append('fail')
                if assert_none(api['results']):
                    assert_p[listid[i]]='Null'
        else:
            listrelust.append('delay')
            list_json.append('delay')
    logger.info('执行完毕，处理报告')
    return listrelust, list_fail, list_pass, list_json

    # except Exception as e:
    #     logger.error('请检查入参格式:{}'.format(listurl[i]))
    # print(api)
