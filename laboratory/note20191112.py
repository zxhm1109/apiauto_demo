'''
@File   :note20191112.py
@BY     ：zhaofy
@data   :2019/11/12
'''

import time
import requests
from PIL import Image
import pytesseract

def get_timestamp():
    t=time.time()
    timestamp=(int(round(t * 1000)))
    return timestamp


if __name__ =='__main__':
    img_url=r'https://api-uat.daoyitong.com/api/v1/captcha/getCaptchaPic/13120806671'
    data={'timeStamp':get_timestamp()}
    reponese=requests.get(img_url,data,stream=True)
    f= open('one.jpg', 'wb')
    f.write(reponese.content)
    f.close()

    result=pytesseract.image_to_string('one.jpg')
    print(result)



'''  # 把结果发送至邮箱
    # source=json.dumps(dict(zip(source_name,source_location)))
    # SendEmail.mail(source)

    def get_ModulePathList(self, SourceName=None):
        source = self.get_ModuleList(SourceName)
        paths = []
        global method,body_name
        for SourceName in source.keys():
            url = self.swagger_cloud + source[SourceName]
            # print('{}--->{}'.format(SourceName,url))
            paths = requests.get(url)
            data=paths.json()

            for k, v in data['paths'].items():  # k: /接口地址
                method_list = []
                self.k=k

                for _k, _v in v.items():  # _k: 请求方式
                    interface = {}  # 初始化
                    method_list.append(_k)
                    api = k  # api地址
                    if len(method_list) > 1:  # api地址下的请求方式不止一个的情况
                        for i in range(len(method_list)):
                            body_name = api.replace('/', '_') + '_' * i  # json文件对应参数名称，excel中body名称
                            method = method_list[-1]  # 请求方式 同一个api地址，不同请求方式
                    else:  # 第一次内循环
                        body_name = api.replace('/', '_')
                        method = _k
                    # self.interface_params = self.retrieve_excel(_v, interface, api)

    def retrieve_excel(self, _v, interface, api):
        """解析参数，拼接为dict--准备完成写入excel的数据"""
        parameters = _v.get('parameters')  # 未解析的参数字典
        if not parameters:  # 确保参数字典存在
            parameters = {}
        case_name = _v['summary']  # 接口名称
        tags = _v['tags'][0]  # 标签名称（属于当前fcb模块中的哪个功能小模块）
        params_dict = self.retrieve_params(parameters)  # 处理接口参数，拼成dict形式
        if params_dict and parameters != {}:  # 单个或多个参数
            interface['row_num'] = self.row  # 写入excel时的所在行
            interface['id'] = 'test_' + str(self.num)  # case id
            interface['tags'] = tags  # 标签名称
            interface['name'] = case_name
            _type = 'json'  # 参数获取方式
            interface['method'] = method  # 请求方式
            interface['url'] = self.k + api  # 拼接完成接口url
            interface['headers'] = 'yes'  # 是否传header
            interface['body'] = body_name
            interface['type'] = _type
            self.num += 1
            self.row += 1
            self.interface_params[body_name] = params_dict
            print("传入excel的数据:", interface)
            # self.write_excel(interface, self.excel_path)  # 参数写入excel
        else:  # 没有参数
            _type = 'data_old'
            interface['name'] = case_name
            interface['row_num'] = self.row
            interface['id'] = 'test_' + str(self.num)
            interface['tags'] = tags
            interface['method'] = method
            interface['url'] = self.url_json + api
            interface['headers'] = 'yes'
            interface['body'] = ''
            interface['type'] = _type
            self.num += 1
            self.row += 1
            self.interface_params[body_name] = params_dict
            # self.write_excel(interface, self.excel_path)
        return self.interface_params

        # for pathurl in path.keys():
        #     url.append(paths['host'] + paths['basePath'] + pathurl)

        # path=json.dumps(path)
        #         print(type(parms))

        # print(self.interface_params)

    # print(self.interface)
    def retrieve_params(self, parameters):
        """处理参数，转为dict"""
        params = ''
        _in = ''
        for each in parameters:
            _in += each.get('in') + '\n'  # 参数传递位置
            params += each.get('name') + '\n'  # 参数
        _in = _in.strip('\n')
        _in_list = _in.split('\n')
        params = params.strip('\n')
        params_list = params.split('\n')
        del_list = params_list.copy()
        for i in range(len(_in_list)):
            if _in_list[i] == 'header':
                params_list.remove(del_list[i])  # 只保存在body传的参数
        test_list = params_list.copy()
        params_dict = dict(zip(params_list, test_list))  # 把list转为dict
        return params_dict

    def write_excel(self, interface, filename):
        """把dict中的值写入对应的excel行中"""
        wt = ExcelRW.Write().write(filename, self.title)
        try:
            wt.write(interface['row_num'], 1, interface['id'])
            wt.write(interface['row_num'], 2, interface['tags'])
            wt.write(interface['row_num'], 3, interface['name'])
            wt.write(interface['row_num'], 4, interface['method'])
            wt.write(interface['row_num'], 5, interface['url'])
            wt.write(interface['row_num'], 7, interface['headers'])
            wt.write(interface['row_num'], 8, interface['body'])
            wt.write(interface['row_num'], 10, interface['type'])
            print("数据写入excle成功！")
        except Exception as e:
            print("出错了，请联系管理元")
            return'''