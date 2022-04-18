import json

import bs4  # 网页解析，获取数据
import re  # 正则表达式+进行文字匹配
import urllib.request, urllib.error  # 指定url，获取网页数据

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class getInformation:
    urldic = {"天津": "101030100", "北京": "101010100", "沈阳": "101070101"}
    url_prefix = "http://t.weather.itboy.net/api/weather/city/"

    #输入一个城市的名字，返回若干天天气预报
    def askcity(self, city):
        url = self.url_prefix + self.urldic.get(city)
        js = self.askURL(url)
        return js

    #输入一个url，返回对应的js，含有若干天天气预报
    def askURL(self, url):
        global js
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, "
                          "like Gecko)Chrome/89.0.4389.90 Safari/537.36 "
        }
        # 用户代理，告诉服务器，我们是什么类型的机器
        req = urllib.request.Request(url=url, headers=header)

        try:
            response = urllib.request.urlopen(req)
            js_text = response.read().decode("utf-8")
            js = json.loads(js_text)

        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)

        return js

    #输入若干天天气预报，返回明天的str
    def text(self, city):
        js = self.askcity(city)
        cityname = js.get("cityInfo").get("city")
        dic = js.get("data").get("forecast")[0]
        text = "明日{}天气:\n最{},最{}。\n日出时间：{},日落时间：{}。\n空气质量{},风向为{},风力为{}。\n天气状况为{}。\n温馨提示：{}".format(
            cityname,
            dic.get("high"),dic.get("low"),dic.get("sunrise"),dic.get("sunset"),dic.get("aqi"),dic.get("fx"),dic.get("fl"),
            dic.get("type"),dic.get("notice")
        )

        return text
