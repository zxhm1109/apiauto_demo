'''
@File   :case_html.py
@BY     ：zhaofy
@data   :2019/12/27
'''
# encoding: utf-8
"""
@author: lileilei
@file: py_Html.py
@time: 2017/6/5 17:04
"""
import os
from Config.Logi import logger

titles = '接口测试'


def title(titles):
    title = '''<!DOCTYPE html>
<html>
<head>
	<title>%s</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 引入 Bootstrap -->
    <link href="https://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    <!-- HTML5 Shim 和 Respond.js 用于让 IE8 支持 HTML5元素和媒体查询 -->
    <!-- 注意： 如果通过 file://  引入 Respond.js 文件，则该文件无法起效果 -->
    <!--[if lt IE 9]>
     <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
     <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <style type="text/css">
        .hidden-detail,.hidden-tr{
            display:none;
        }
    </style>
    <script type="text/javascript">
        //显示悬浮层
        function showInform() {
            document.getElementById("inform").style.display = 'block';
            // document.getElementById("inform").css("display","block");
        }

        //隐藏悬浮层
        function hiddenInform(event) {
            var informDiv = document.getElementById('inform');
            var x = event.clientX;
            var y = event.clientY;
            var divx1 = informDiv.offsetLeft;
            var divy1 = informDiv.offsetTop;
            var divx2 = informDiv.offsetLeft + informDiv.offsetWidth;
            var divy2 = informDiv.offsetTop + informDiv.offsetHeight;
            if (x < divx1 || x > divx2 || y < divy1 || y > divy2) {
                document.getElementById('inform').style.display = 'none';
            }

        }


    </script>
    <style type="text/css">
        body {
            position: relative;
        }

        #inform {
            position: absolute;
            max-height: 250px; /* 设置最大高度，当高度达到此值时出现滚动条 */
            z-index: 10;
            background-color: #E0E5E5;
            overflow: auto; /* 自动添加滚动条 */
            box-shadow: 0px 0px 10px #000; /* 外阴影 */
            display: none; /* 默认隐藏 */
        }

        #informTable {
            table-layout: fixed; /* 用于实现表格td自动换行的部分代码*/
            width: 325px;
        }

        #informTable tr td {
            width: 325px;
            height: 30px;
            font-size: 16px;
            font-family: Georgia;
            color: #555555;
            word-wrap: break-word; /*自动换行*/
            padding: 0 0 0 0;
        }

        #informTable tr td:hover {
            background-color: #D9D9D9;
        }

        #inform hr {
            border: 1;
            width: 325px;
            margin-bottom: 0px;
        }

    </style>
</head>
<body>
	''' % (titles)
    return title


connent = '''
<div  class='col-md-4 col-md-offset-4' style='margin-left:3%;'>
<h1>接口测试的结果</h1>'''


def shouye(starttime, endtime, passge, fail, amount, Skipped):
    beijing = '''
    <table  class="table table-hover table-condensed">
            <tbody>
                <tr>
		<td><strong>开始时间:</strong> %s</td>
		</tr>
		<td><strong>结束时间:</strong> %s</td></tr>
		<td><strong>耗时:</strong> %s</td></tr>
		<td><strong>结果:</strong>
			<span >用例总数: <strong >%s</strong>
			通过: <strong >%s</strong>
			失败: <strong >%s</strong>
			未执行: <strong >%s</strong></span></td>                  
			   </tr> 
			   </tbody></table>
			   </div> ''' % (starttime, endtime, (endtime - starttime), amount, passge, fail, Skipped)
    return beijing


shanghai = '''<div class="row " style="margin:60px">
        <table class="table table-hover table-condensed table-bordered" style="word-wrap:break-word; word-break:break-all;  margin-top: 7px;"
        border='2'cellspacing='1' cellpadding='1' width="100%" align="center">
		<tr >
            <td width="5%"><strong>用例ID</strong></td>
            <td width="10%"><strong>名称</strong></td>
            <td width="10%"><strong>模块</strong></td>
            <td width="30%" ><strong>入参</strong></td>
            <td width="20%"><strong>接口</strong></td>
            <td width="10%"><strong>期望</strong></td>
            <td width="5%"><strong>实际</strong></td>
            <td width="5%"><strong>结果</strong></td>
        </tr>
    '''


def passfail(tend):
    if tend == 'pass':
        htl = '''<td bgcolor="green">pass</td>'''
    elif tend == 'fail':
        htl = '''<td bgcolor="fail">fail</td>'''
    else:
        htl = '<td bgcolor="crimson">exect</td>'
    return htl


def ceshixiangqing(reslt, id, name, key, coneent, url, meth, yuqi, json, relust):
    xiangqing = '''
        <tr class="case-tr %s">
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
             <td>
                <a id="btn" onMouseOver="javascript:showInform();" onMouseOut="hiddenInform()">
                    %s
                </a>
                <div id="inform" onMouseOver="javascript:showInform();" onMouseOut="hiddenInform(event)">
                    <a>11</a>
                </div>
            </td>
            
            %s
        </tr>
    ''' % (reslt, id, name, key, coneent, url, yuqi, json, passfail(relust))
    return xiangqing


weibu = '''</div></div></table><script src="https://code.jquery.com/jquery.js"></script>
<script src="https://cdn.bootcss.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<script type="text/javascript">
</script>
</body></html>'''


def relust(titles, starttime, endtime, passge, fail, id, name, key, coneent, url, meth, yuqi, json, relust, amount,
           Skipped):
    if type(name) == list:
        relus = ' '
        for i in range(len(name)):
            if relust[i] == "pass":
                clazz = "success"
            elif relust[i] == "fail":
                clazz = "warning"
            else:
                clazz = 'error'
            relus += (
                ceshixiangqing(clazz, id[i], name[i], key[i], coneent[i], url[i], meth[i], yuqi[i], json[i], relust[i]))
        text = title(titles) + connent + shouye(starttime, endtime, passge, fail, amount, Skipped
                                                ) + shanghai + relus + weibu
    else:
        text = title(titles) + connent + shouye(starttime, endtime, passge, fail,
                                                amount) + shanghai + ceshixiangqing(id, name, key, coneent, url,
                                                                                    meth,
                                                                                    yuqi, json, relust) + weibu
    return text


def createHtml(filepath, titles, starttime, endtime, passge, fail, id, name, key, coneent, url, meth, yuqi, json,
               relusts, amount, Skipped):
    texts = relust(titles, starttime, endtime, passge, fail, id, name, key, coneent, url, meth, yuqi, json, relusts,
                   amount, Skipped)
    with open(filepath, 'wb') as f:
        f.write(texts.encode('utf-8'))
    logger.info('html报告处理完毕')
    return texts
