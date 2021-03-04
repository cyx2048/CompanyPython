#coding=UTF-8
#remark=

from flask import Flask
from flask import request
import json

app = Flask(__name__)
@app.route('/passport/user/login',methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        data = json.dumps({
            'username':username,
            'password':password,
            'code':'200'
        })
    else:
        data = json.dumps({
            'message':'请传递参数'
        })
    print(type(data))
    return data

if __name__=='__main__':
    app.run()

# http://127.0.0.1:5000/passport/user/login?username=dsadas&password=dsafdasf