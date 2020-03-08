import json, time
import xlrd
import xlwt
from xlutils.copy import copy
from Config.Logi import logger
import os


def write_data(data, file_name):
    """写入json"""
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


class Write_excel(object):
    def __init__(self, filename):
        self.filename = os.path.dirname(__file__) + '/report/' + filename + 'testapi' + '.xlsx'  # 路径+文件名

    def create_excelFile(self):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('接口测试用例')
        sheet_title = [['id', 'tags', 'name', 'method', 'url', 'params', 'headers', 'body', 'body_type', 'type'], ]
        for j in range(len(sheet_title[0])):
            sheet.write(0, j, sheet_title[0][j])
        workbook.save(self.filename)

    def write(self, hang, lie, data):
        workbook = xlrd.open_workbook(self.filename)
        sheets = workbook.sheet_names()
        worksheet = workbook.sheet_by_name(sheets[0])
        rows_old = worksheet.nrows
        new_workbook = copy(workbook)
        new_worksheet = new_workbook.get_sheet(0)
        new_worksheet.write(hang, lie - 1, data)
        new_workbook.save(self.filename)


class Read_Excel:
    def __init__(self):
        self.filepath = os.path.dirname(__file__) + '\\api_test_case.xlsx'

    def get_excel(self, sheetname):
        try:
            workbook = xlrd.open_workbook(self.filepath)
            me = workbook.sheet_by_name(sheetname)
            rows = me.nrows
            listid = []
            listmodule = []
            listparmas = []
            listurl = []
            listmethod = []
            listheader = []
            listhost = []
            listname = []
            listexpect = []
            listisactive = []
            Skipped = 0
            case_num = 0
            for i in range(1, rows):
                if (me.cell(i, 9).value) != 'N':
                    listid.append(me.cell(i, 0).value)
                    listmodule.append(me.cell(i, 1).value)
                    listname.append(me.cell(i, 2).value)
                    listhost.append(me.cell(i, 3).value)
                    listurl.append(me.cell(i, 4).value)
                    listmethod.append((me.cell(i, 5).value))
                    listheader.append((me.cell(i, 6).value))
                    listparmas.append((me.cell(i, 7).value))
                    listexpect.append((me.cell(i, 8).value))
                    listisactive.append((me.cell(i, 9).value))
                else:
                    Skipped += 1
                case_num += 1
            logger.info('解析excel')
            return listid, listmodule, listname, listhost, listurl, listmethod, listheader, listparmas, listexpect, listisactive, Skipped, case_num
        except Exception as e:
            logger.info('打开测试用例失败，原因是:%s' % e)
            return

    def write(self, hang, lie, data):
        workbook = xlrd.open_workbook(os.path.dirname(__file__) + '\\api_test_case.xlsx')
        sheets = workbook.sheet_names()
        worksheet = workbook.sheet_by_name(sheets[0])
        rows_old = worksheet.nrows
        new_workbook = copy(workbook)
        new_worksheet = new_workbook.get_sheet(0)
        new_worksheet.write(hang, lie - 1, data)
        new_workbook.save(self.filepath)


def check_data(r):
    """检查数据是否是dict"""
    if not isinstance(r, dict):
        return False
    else:
        return True


if __name__ == '__main__':
    '''
    #生成excel
    excel_path = os.path.dirname(__file__) + '/report/'
    name =excel_path+time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    Write_excel(name).create_excelFile()
    '''
    aaa = Read_Excel().get_excel('filesys')
    print(aaa)
