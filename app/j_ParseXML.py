import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2
import urllib
import json
import xml.etree.ElementTree as ET
import time
import re
from app import wx_template

def parse_return(data):
    xml_recv = ET.fromstring(data)
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    Content = xml_recv.find("Content").text
    Talk_json = Turing_talk(Content, FromUserName)


    reply = wx_template.text_reply
    Content = Talk_json['text']
    str_reply = reply % (FromUserName, ToUserName, str(int(time.time())), Content)
    #之前正常版本
    # if Talk_json['code'] == 200000:
    #     wx_template.response_link(ToUserName, FromUserName,str(int(time.time())) ,Talk_json)
    #     # reply = wx_template.link_reply
    #     # Content = Talk_json['text']
    #     # Url = Talk_json['url']
    #     # print(Url)
    #     # str_reply = reply % (FromUserName, ToUserName, str(int(time.time())), Talk_json['url'], Content)
    return str_reply


def Turing_talk(content, userid):
    values = {}
    values['key'] = 'db9fcfd70818ee5e7fb68e2d6d9a5a2c'
    values['info'] = content
    values['userid'] = re.sub(r'[^a-zA-Z0-9]', '', userid)
    data = urllib.urlencode(values)
    url='http://www.tuling123.com/openapi/api?'
    full_url = url+data
    response = urllib2.urlopen(full_url)
    html = response.read()
    hjson = json.loads(html.decode('utf-8'))
    return hjson
    #print(hjson['code'])
    #print(hjson['text'])
    #print(html.decode('utf-8'))


