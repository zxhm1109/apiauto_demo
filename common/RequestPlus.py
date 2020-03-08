'''
@File   :RequestPlus.py
@BY     ：zhaofy
@data   :2019/12/27
'''
import requests, json


def requestspuls(url, method, parmas, header={"Accept": "*/*", "Content-Type": "application/json;charset=utf-8"}):
    requests.packages.urllib3.disable_warnings()
    if method == 'post':
        res = requests.post(url, data=json.dumps(parmas), headers=header,verify=False)
        result = res.json()
        return result
    elif method == 'get':
        result = requests.get(url, params=parmas, verify=False)
        result = result.json()
        return result

if __name__ == '__main__':
    url = 'https://api-uat.daoyitong.com/cloud/filesys/file/urlAllpathModel/byIds'
    header = {'Content-Type': 'application/json'}
    params = {"ids": ["1161577467045744640"]}
    requestspuls(url, parmas=params, method='post', header=header)
