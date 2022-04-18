import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header
from getInformation import getInformation
import random


def sentforecast(city):

    if city=="测试":
        city ="北京"
        reciver_dic = {"北京": ["ysyysy2001@126.com"],
                       "沈阳": ["ysyysy2001@126.com"]}

        mm_to_dic = {"北京": "<ysyysy2001@126.com>",
                     "沈阳": "<ysyysy2001@126.com>"}
    else:
        reciver_dic = {"北京": ["993811659@qq.com", "ysyysy2001@126.com", "1374405852@qq.com"],
                       "沈阳": ["ysyysy2001@126.com", "cloudmirrorgo@163.com", "1471127927@qq.com", "959288458@qq.com"]}

        mm_to_dic = {"北京": "<993811659@qq.com>,<ysyysy2001@126.com>,<1374405852@qq.com>",
                     "沈阳": "<ysyysy2001@126.com>,<cloudmirrorgo@163.com>,<1471127927@qq.com>,<959288458@qq.com>"}

    weatherclass = getInformation()
    weathertext = weatherclass.text(city)
    # SMTP服务器,这里使用163邮箱
    mail_host = "smtp.163.com"
    # 发件人邮箱
    mail_sender = "ysyysy2019@163.com"
    # 邮箱授权码
    mail_license = "BEPQRQWLAEVMRMPX"
    # 收件人邮箱，可以为多个收件人

    #mail_receivers = ["ysyysy2001@126.com", "cloudmirrorgo@163.com", "1471127927@qq.com", "959288458@qq.com"]
    mail_receivers = reciver_dic.get(city)
    #print(type(mail_receivers))
    mm = MIMEMultipart('related')

    # 邮件主题

    subject_content = """明日天气提醒"""
    # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
    mm["From"] = "小姚的天气提醒bot<ysyysy2019@163.com>"
    # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
    # mm["To"] = "<ysyysy2001@126.com>,<cloudmirrorgo@163.com>,<1471127927@qq.com>,<959288458@qq.com>"
    # mm["To"] = "<ysyysy2001@126.com>,<1079481391@qq.com>"
    mm["To"] = mm_to_dic.get(city)
    # print(type(mm["To"]))
    # 设置邮件主题
    mm["Subject"] = Header(subject_content, 'utf-8')
    # 邮件正文内容
    body_content = weathertext
    # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
    message_text = MIMEText(body_content, "plain", "utf-8")
    # 向MIMEMultipart对象中添加文本对象
    mm.attach(message_text)

    # 二进制读取图片
    i = random.randint(1, 4)
    image_data = open('cute_cats/'+str(i)+'.png', 'rb')
    # 设置读取获取的二进制数据
    message_image = MIMEImage(image_data.read())
    # 关闭刚才打开的文件
    image_data.close()
    # 添加图片文件到邮件信息当中去
    mm.attach(message_image)
    #
    # # 构造附件
    # atta = MIMEText(open('sample.xlsx', 'rb').read(), 'base64', 'utf-8')
    # # 设置附件信息
    # atta["Content-Disposition"] = 'attachment; filename="sample.xlsx"'
    # # 添加附件到邮件信息当中去
    # mm.attach(atta)

    # 创建SMTP对象

    # 设置发件人邮箱的域名和端口，端口地址为25
    stp = smtplib.SMTP_SSL(mail_host,465)
    # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
    stp.set_debuglevel(1)
    # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    stp.login(mail_sender, mail_license)
    # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    stp.sendmail(mail_sender, mail_receivers, mm.as_string())
    print("邮件发送成功")
    # 关闭SMTP对象
    stp.quit()
