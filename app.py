from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/')
def index():
    return 'Hello, Flask!'


@app.route('/hello/<username>/<password>')
def hello(username, password):
    dic = {'bowen':'106'}
    result = "登陆失败"
    if (username in dic) and (password is not None) and (dic.get(username) == password):
        result = "登陆成功"
    response = make_response(jsonify(result))
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
