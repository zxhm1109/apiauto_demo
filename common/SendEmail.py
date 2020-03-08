'''
@File   :SendEmail.py
@BY     ：zhaofy
@data   :2019/12/18
'''

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender = 'zz.xinsile@qq.com'
my_pass = 'daxyowvjjapzbbbc'
my_user = 'fuyu.zhao@daoyitong.com'


def mail(sendmessage):
    ret = True
    try:
        msg = MIMEText(sendmessage, 'html', 'utf-8')
        msg['From'] = formataddr(["TEST", my_sender])
        msg['To'] = formataddr(["api-test", my_user])
        msg['Subject'] = "发送邮件测试"

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(e)
        print("邮件发送失败")
        ret = False
    return ret


if __name__ == '__main__':
    # html=html.read()
    # print(html)
    aaa='''<html><a href="https://www.runoob.com/" target="_blank" rel="noopener noreferrer">访问菜鸟教程!</a></html>'''
    ret = mail(aaa)
