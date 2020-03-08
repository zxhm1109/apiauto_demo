'''
@File   :Assert_zx.py
@BY     ：zhaofy
@data   :2019/12/30
'''
from Config.Logi import logger
import json


def assert_in(asserqiwang, fanhuijson):
    if len(asserqiwang.split('=')) > 1 or len(asserqiwang.split(':')) > 1:
        data = asserqiwang.split('&')
        if '=' in asserqiwang:
            result = dict([(item.split('=')) for item in data])
            value1 = ([(str(key)) for key in fanhuijson.values()])
            value2 = ([(str(value)) for value in result.values()])
            if set(value2) < set(value1):
                return {'code': 0, 'result': fanhuijson['results']}
            else:
                return {'code': 1, 'result': fanhuijson}
        else:
            result = dict([(item.split(':')) for item in data])
            value2 = assert_in_plus(result)
            for xx, yy in value2.items():
                if xx in fanhuijson.keys():
                    if yy == fanhuijson[xx]:
                        return {'code': 0, 'result': fanhuijson['results']}
                    else:
                        return {'code': 1, 'result': fanhuijson}
                else:
                    return {'code': 1, 'result': fanhuijson}
    else:
        logger.info('请填写Case预期')
        return {'code': 2, 'result': None}


def assert_in_plus(data1):
    ssss = {}
    for x, y in data1.items():
        key = x.strip(" ").strip('"')
        ssss[key] = y.strip(" ").strip('"')
    return ssss


def get_dict(items, values):
    result = []
    if isinstance(items, dict) and values in items.keys():
        result1 = items[values]
        result.append(result1)
        return result
    elif isinstance(items, (list, tuple)):
        for dt in items:
            data = get_dict(dt, values)
            if data == 'None' or data is None:
                pass
            elif len(data) == 0:
                pass
            else:
                result.append(data)
        return result
    else:
        if isinstance(items, dict):
            for key in items:
                res = get_dict(key, values)
                if res == 'None' or res is None:
                    pass
                elif len(res) == 0:
                    pass
                else:
                    result.append(res)
            return result


def assert_parmas(parma,assert_p):
    if parma is not None and len(parma) >1:
        try:
            parmas = json.loads(parma)
            for xx in parmas:
                if '#' in str(parmas[xx]):
                    try:
                        parmas[xx] = assert_p[parmas[xx].lstrip('#')]
                    except:
                        logger.error('上级联动接口异常：{}'.format(parmas[xx]))
                        break
                else:
                    pass
            return parmas
        except:
            return parma
    else :
        pass

def assert_none(parms):
    if None is parms:
        return False
    else:
        return True


if __name__ == '__main__':
    a = 'message: "SUCCESS"'
    b = {"code": 1, "message": "执行成功", "errors": 0,
         "results": {"instPackPicUrl": "", "packageDetailUrl": 'null', "instAtomicDetailAppDTOList": 'null'}}
    c = '{"recordId":"#TEST_1656","instPackPicUrl": "111"}'
    d={"TEST_1656":"123456"}
    aaa = assert_parmas(c,d)
    print(aaa)
