import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2
import urllib
import json
import xml.etree.ElementTree as ET
import time
import re

def parse_return(data):
    xml_recv = ET.fromstring(data)
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    Content = xml_recv.find("Content").text
    new_Content = Turing_talk(Content, FromUserName)
    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
    str_reply = reply % (FromUserName, ToUserName, str(int(time.time())), new_Content)
    return str_reply


def Turing_talk(content,userid):
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
    return hjson['text']
    #print(hjson['code'])
    #print(hjson['text'])
    #print(html.decode('utf-8'))


