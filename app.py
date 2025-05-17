from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Flask!'


@app.route('/hello/<username>/<password>')
def hello(username, password):
    dic = {'bowen':'106'}
    result = "登陆失败"
    if (username in dic) and (password is not None) and (dic.get(username) == password):
        result = "登陆成功"
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
