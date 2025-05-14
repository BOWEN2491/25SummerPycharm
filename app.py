from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Flask!'


@app.route('/hello/<username>/<password>')
def hello(username, password):
    dic = {'bowen':106}
    result = "登陆失败"
    tf = dic.__contains__(username)
    value = dic.get(username)
    tf2= dic.get(username)==password
    if dic.__contains__(username)&(dic.get(username)==int(password)):
        result = "登陆成功"
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
