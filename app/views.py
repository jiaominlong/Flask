from app import app
from flask import render_template, request
import hashlib

@app.route('/')
def index():
    token = 'jiaominlong'
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    s = [token, timestamp, nonce]
    s.sort()
    s = ''.join(s)

    if (hashlib.sha1(s.encode('utf-8')).hexdigest() == signature):
        print('===========')
        return True
    else:
        print('fiall')
        return render_template('index.html')

@app.route('/weixin')
def weixin():
    pass