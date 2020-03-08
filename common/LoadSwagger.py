'''
@File   :LoadSwagger.py
@BY     ：zhaofy
@data   :2019/12/23
'''

import requests, json, os, time
from Config.Logi import logger
from Config.ExcelRW import Write_excel


class get_swagger:
    def __init__(self):

        self.sourcename = []
        self.num = 1  # case编号
        self.case = []

    def load_swagger_data(self):
        '''
        :param SourceName: 服务名称list(为空返回所有)
        :return: 全量服务列表+地址||入参服务列表+地址
        '''
        self.swagger_cloud = r'https://api-uat.daoyitong.com/cloud'
        self.swagger_resource = 'https://api-uat.daoyitong.com/cloud/swagger-resources'

        reponese = requests.get(self.swagger_resource).json()
        for sourcename in reponese:
            self.sourcename.append(sourcename['name'])
        logger.info('swagger中的服务列表：{}'.format(str(self.sourcename)))

        for cloud in reponese:
            location = self.swagger_cloud + cloud['location']
            reponese1 = requests.get(location).json()
            if 'paths' in reponese1:
                for path1 in reponese1['paths']:
                    path = reponese1['paths'][path1]
                    definitions = reponese1['definitions']
                    for method in path:
                        if 'parameters' in path[method]:
                            # 处理接口入参参数
                            self.param = self.retrieve_params(path[method]['parameters'], definitions, path1,
                                                              reponese1['basePath'])
                        else:
                            self.param = ' '
                        definitionss = {}
                        path3 = path1.split('/')
                        a = 0
                        b = 0
                        #移除get接口url{}
                        for ttt in path3:
                            if '{' in ttt:
                                a += len(ttt)
                                b += 1
                        if b != 0:
                            path1 = path1[0:-(a + b - 1)]

                        definitionss['id'] = 'TEST_'+str(self.num)
                        definitionss['host'] = reponese1['host']
                        definitionss['url'] = reponese1['basePath'] + path1
                        definitionss['method'] = method
                        definitionss['param'] = self.param
                        definitionss['consumes'] = path[method]['consumes'][0]
                        definitionss['summary'] = path[method]['summary']
                        definitionss['tags'] = path[method]['tags'][0]
                        definitionss['sourcename'] = reponese1['basePath'].strip('/')
                        self.num += 1
                        if definitionss['url'] not in self.case:
                            self.case.append(definitionss)
                    # dict转json，处理中文编码
                    # reponese1=json.dumps(reponese1,ensure_ascii=False)
        else:
            logger.error('{}服务无接口'.format(reponese1['basePath']))

        return self.case

    def retrieve_params(self, parameters, definitions, path, ssss):
        self.reg = ''
        param = ''
        paramx = ''
        for parameters1 in parameters:
            if 'schema' in parameters1 and parameters1['name'] == parameters1['description'] and parameters1[
                'description'] != 'object':
                if 'items' in parameters1['schema'] and '$ref' in parameters1['schema']['items']:
                    self.reg = parameters1['schema']['items']['$ref'].split('/')[-1]
                    param = definitions[self.reg]
                elif '$ref' in parameters1['schema']:
                    self.reg = parameters1['schema']['$ref'].split('/')[-1]
                    param = definitions[self.reg]
                else:
                    return param
                for paramx in param['properties']:
                    if '$ref' in param['properties'][paramx]:
                        xxx = param['properties'][paramx]['$ref'].split('/')[-1]
                        param[paramx] = definitions[xxx]['properties']
                    else:
                        param = param
                return param
            else:
                param = parameters1
                return param


if __name__ == '__main__':
    case_list = get_swagger().load_swagger_data()
    excel_name = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    Write_excel(excel_name).create_excelFile()
    logger.info('创建{}文件成功'.format(excel_name))
    wt = Write_excel(excel_name)
    row = 1

    for case_num in range(len(case_list) - 1):
        case_list[case_num]['param'] = json.dumps(case_list[case_num]['param'], ensure_ascii=False)
        wt.write(row, 1, case_list[case_num]['id'])
        wt.write(row, 2, case_list[case_num]['sourcename'])
        wt.write(row, 3, case_list[case_num]['tags'])
        wt.write(row, 4, case_list[case_num]['summary'])
        wt.write(row, 5, case_list[case_num]['host'])
        wt.write(row, 6, case_list[case_num]['url'])
        wt.write(row, 7, case_list[case_num]['method'])
        wt.write(row, 8, case_list[case_num]['consumes'])
        # wt.write(row, 9, case_list[case_num]['param'])
        logger.info('{}-写入成功,写入内容：{}'.format(row, case_list[case_num]))
        row += 1
