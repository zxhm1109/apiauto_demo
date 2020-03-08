'''
@File   :swagger-demo.py
@BY     ：zhaofy
@data   :2019/11/26
'''
import requests
from laboratory.swagger_interface import AnalysisJson
from Config.Logi import logger


class loadSwagger:
    def __init__(self, SourceName=None):
        self.swagger_cloud = r'https://api-uat.daoyitong.com/cloud'
        self.swagger_resource = 'https://api-uat.daoyitong.com/cloud/swagger-resources'
        '''
        :param SourceName: 服务名称list(为空返回所有)
        :return: 全量服务列表+地址||入参服务列表+地址
        '''
        reponese = requests.get(self.swagger_resource)
        reponese = reponese.json()
        source_name = []
        source_location = []
        source2 = {}
        for cloud in reponese:
            location = self.swagger_cloud + cloud['location']
            name = cloud['name']
            source_name.append(name)
            source_location.append(location)
        source = dict(zip(source_name, source_location))
        logger.info('swagger中的全部服务：{}'.format(source_name))
        if SourceName is None:
            self.get_ModuleList(source)

        elif type(SourceName) is str:
            if SourceName in source.keys():
                source2[SourceName] = source[SourceName]
                print(source2)
                self.get_ModuleList(source2)
            else:
                logger.info('未找到该{}服务'.format(SourceName))
        else:
            for name1 in SourceName:
                if name1 in source:
                    source2[name1] = source[name1]
                else:
                    logger.info('未找到该{}服务'.format(name1))

            logger.info('查询成功，已找到{}服务'.format(list(source2.keys())))
            self.get_ModuleList(source2)


    def get_ModuleList(self, source):
        if len(source) ==1:
            self.url_json = source[0]
            AnalysisJson(self.url_json, source).retrieve_data(self.url_json)
        else:
            for module in source:
                self.url_json = source[module]
                AnalysisJson(self.url_json, module).retrieve_data(self.url_json)


if __name__ == "__main__":
    # aa = get_ApiList('physicalexam')
    SourceName = 'card'
    loadSwagger(SourceName)
