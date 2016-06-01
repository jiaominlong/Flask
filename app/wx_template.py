text_reply = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    <FuncFlag>0</FuncFlag>
                </xml>'''

link_reply = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[<a href='%s'>%s</a>]]></Content>
                    <FuncFlag>0</FuncFlag>
                </xml>'''

def response_link(FromUserName, ToUserName, n_time, Talk_json):
    link_reply = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[<a href='%s'>%s</a>]]></Content>
                    <FuncFlag>0</FuncFlag>
                </xml>'''
    Content = Talk_json['text']
    Url = Talk_json['url']
    str_reply = link_reply % (FromUserName, ToUserName, n_time, Url, Content)
    return str_reply