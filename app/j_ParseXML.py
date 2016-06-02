import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2
import urllib
import json
import xml.etree.ElementTree as ET
import re
from app import wx_template

#receive weixin info
def parse_return(data):
    xml_recv = ET.fromstring(data)
    receive_data = {}
    receive_data['ToUserName'] = xml_recv.find("ToUserName").text
    receive_data['FromUserName'] = xml_recv.find("FromUserName").text
    if xml_recv.find("Content") != None:
        receive_data['Content'] = xml_recv.find("Content").text
    else:
        receive_data['Content'] = xml_recv.find("Recognition").text

    Talk_json = Turing_talk(receive_data['Content'], receive_data['FromUserName'])
    return wx_template.Response_mach_message(receive_data, Talk_json)



#Turing return message
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


