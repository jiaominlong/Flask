import time


def Response_mach_message(receive_data, Turing_message):
    #return text info
    if Turing_message['code'] == 100000:
        text_reply = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    <FuncFlag>0</FuncFlag>
                </xml>'''
        reply = text_reply
        Content = Turing_message['text']
        str_reply = reply % (receive_data['FromUserName'], receive_data['ToUserName'], str(int(time.time())), Content)
        return str_reply
    #return link_text info
    elif Turing_message['code'] == 200000:
        link_reply = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[<a href='%s'>%s</a>]]></Content>
                    <FuncFlag>0</FuncFlag>
                </xml>'''
        Content = Turing_message['text']
        Url = Turing_message['url']
        str_reply = link_reply % (receive_data['FromUserName'], receive_data['ToUserName'], str(int(time.time())), Url, Content)
        return str_reply
    #return news or image info
    elif (Turing_message['code'] == 308000) or (Turing_message['code'] == 302000):
        news_reply = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[news]]></MsgType>
                    <ArticleCount>%d</ArticleCount>
                    <Articles>%s</Articles>
                </xml>'''
        new_template = '''<item>
                            <Title><![CDATA[%s]]></Title>
                            <Description><![CDATA[%s]]></Description>
                            <PicUrl><![CDATA[%s]]></PicUrl>
                            <Url><![CDATA[%s]]></Url>
                        </item>'''
        new_str = ''
        count = 0
        news_list = Turing_message['list']
        #return news
        if Turing_message['code'] == 308000:
            for new_item in news_list:
                if count < 5:
                    new_str += new_template % (new_item['name'], new_item['info'], new_item['icon'], new_item['detailurl'])
                    count += 1
                else:
                    break
            str_reply = news_reply % (receive_data['FromUserName'], receive_data['ToUserName'], str(int(time.time())), count, new_str)
            return str_reply
        else:
            for new_item in news_list:
                if count < 10:
                    new_str += new_template % (new_item['article'], new_item['source'], new_item['icon'], new_item['detailurl'])
                    count += 1
                else:
                    break
            str_reply = news_reply % (receive_data['FromUserName'], receive_data['ToUserName'], str(int(time.time())), count, new_str)
            return str_reply