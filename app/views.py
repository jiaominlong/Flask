from app import app
from flask import render_template, request, make_response
import hashlib
from app.j_ParseXML import parse_return


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weixin',methods=['GET', 'POST'])
def weixin():
    if request.method == 'GET':
        token = 'jiaominlong'
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')

        s = [token, timestamp, nonce]
        s.sort()
        s = ''.join(s)
        print(s)
        if (hashlib.sha1(s.encode('utf-8')).hexdigest() == signature):
            print('===========')
            return make_response(echostr)
        else:
            print('wei xin Access fial')

    # Get the infomations from the recv_xml.


    rep_str = parse_return(request.data)
    response = make_response(rep_str)
    response.content_type = 'application/xml'
    return response