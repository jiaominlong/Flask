import xml.etree.ElementTree as ET
import time

def parse_return(data):
    xml_recv = ET.fromstring(data)
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    Content = xml_recv.find("Content").text
    new_Content = Content+FromUserName
    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
    str_reply = reply % (FromUserName, ToUserName, str(int(time.time())), new_Content)
    return str_reply






