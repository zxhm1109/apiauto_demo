'''
@File   :LoadPhysicalOrder.py
@BY     ：zhaofy
@data   :2020/3/16
'''

import xlrd, os
import requests
import pymysql
# from sshtunnel import

mysql = pymysql.connect(host='10.254.162.231',
                        user='daoyitong', password='dyt_mysql_456', database='pavo_physicalexam', charset='utf8')
cursor = mysql.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchall()  # fetchone获取一条
print(data)
mysql.close()
















# filepath = os.path.dirname(__file__) + '/physicalexamorder.xlsx'
# workbook = xlrd.open_workbook(filepath)
# sheet =workbook.sheet_by_index(0)
# rows=sheet.nrows
# url='https://api.daoyitong.com/cloud/physicalexam/manual/refreshOrder'
# num=0
# errornum=0
# for xx in range(1,rows):
#     rid=sheet.cell(xx,0).value
#     data='id='+'1091531702534410240'
#     result=requests.get(url,data)
#     result=result.json()
#     if result['code'] == 1:
#         num+=1
#         print('{}-->pass'.format(num))
#     else:
#         errornum+=1
#         print('【{}】--fail--{}'.format(errornum,result))
