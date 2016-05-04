from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

# 基本
@app.route('/')
def index():
    return '<h1>こんにちは</h1>'

# URIから受け取り
@app.route('/user/<name>')
def user(name):
    return '<h1>こんにちは、%s</h1>' % name

# UserAgent情報
@app.route('/user-agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return '<h1>あなたのブラウザは %s です</h1>' % user_agent

# 返すコードを指定
@app.route('/error')
def error():
    return '<h1>400を返します</h1>', 400

# クッキー(まだクッキーについて理解しきれていない)
@app.route('/cookie')
def cookie():
    response = make_response('<h1>クッキーを使用します</h1>')
    response.set_cookie('treasure', '555')
    return response

# リダイレクト
@app.route('/redirect')
def redirect_test():
    return redirect('http://google.com')

# 例外に404を返す（まだ理解しきれていない）
@app.route('/user_verify/<id>')
def get_user(id):
    user = load_user(id) #この関数は？
    if not user:
        abort(404)
    return '<h1>こんにちは、%s' % user.name

if __name__ == '__main__':
    app.run(debug=True)
