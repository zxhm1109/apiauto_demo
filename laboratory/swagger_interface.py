'''
@File   :swagger_interface.py
@BY     ：zhaofy
@data   :2019/12/19
'''

import os
import requests
from Config.ExcelRW import write_data, Write_excel
from Config.Logi import logger
import time

title_list = []


class AnalysisJson(object):
    """swagger自动生成测试用例"""

    def __init__(self, url_json, module=1):

        global title_list, json_path
        self.url_json = url_json
        r = requests.get(self.url_json).json()
        self.title = r['info']['title']
        print('ssssssss----{}'.format(r))
        logger.info('标题' + self.title)
        write_data(r, '{}.json'.format(self.title))  # swagger 完整大文件

        self.interface_params = {}
        self.row = 1  # 写入excel起始行数
        self.num = 1  # 初始化case id

        if self.check_data(r):
            # self.json_path = os.path.abspath(
            #     os.path.dirname(
            #         os.path.dirname(__file__))) + '\\common' + '\\report' + '\\{}_data.json'.format(
            #     str(module))  # json file path，执行多个url的情况，区分生成的json文件
            self.data = r['paths']  # paths中的数据是有用的
            title_list.append(self.title)

            # 创建excel 文件
            self.excel_path = os.path.dirname(__file__) + '/report/'
            wt = Write_excel(self.excel_path)
            wt.create_excelFile()

        else:
            print("swagger 请求错误！")

    def check_data(self, r):

        """检查返回的数据是否是dict"""
        if not isinstance(r, dict):
            return False
        else:
            return True

    def retrieve_data(self, module=1):
        """
        :return:
        """
        global body_name, method
        for k, v in self.data.items():  # k: /接口地址

            method_list = []
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
                self.interface_params = self.retrieve_excel(_v, interface, api)  # 写入excel，

        # if self.interface_params:
        #     write_data(self.interface_params, self.json_path)  # 参数写入json文件

    def retrieve_excel(self, _v, interface, api):
        """解析参数，拼接为dict--准备完成写入excel的数据"""
        parameters = _v.get('parameters')  # 未解析的参数字典
        if not parameters:  # 确保参数字典存在
            parameters = {}
        print('1111{}'.format(parameters))
        case_name = _v['summary']  # 接口名称
        tags = _v['tags'][0]  # 标签名称（属于当前fcb模块中的哪个功能小模块）
        params_dict = self.retrieve_params(parameters)  # 处理接口参数，拼成dict形式
        print('asdsada', params_dict)
        if params_dict and parameters != {}:  # 单个或多个参数
            interface['row_num'] = self.row  # 写入excel时的所在行
            interface['id'] = 'test_' + str(self.num)  # case id
            interface['tags'] = tags  # 标签名称
            interface['name'] = case_name
            _type = 'json'  # 参数获取方式
            interface['method'] = method  # 请求方式
            interface['url'] = self.url_json + api  # 拼接完成接口url
            interface['headers'] = 'yes'  # 是否传header
            interface['body'] = body_name
            interface['type'] = _type
            self.num += 1
            self.row += 1
            self.interface_params[body_name] = params_dict
            print("传入excel的数据:", interface)
            self.write_excel(interface, self.excel_path)  # 参数写入excel
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
            self.write_excel(interface, self.excel_path)
        return self.interface_params

    def retrieve_params(self, parameters):
        """处理参数，转为dict"""
        print('1221122{}'.format(parameters))
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
        wt = Write_excel(filename)

        try:
            print(interface)
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
            print(e)
            print("出错了，请联系管理元")
            return


if __name__ == '__main__':
    AnalysisJson("https://api-uat.daoyitong.com/cloud/extra/v2/api-docs").retrieve_data()
