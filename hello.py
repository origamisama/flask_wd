from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '''<h1>こんにちは<h1>
    <h2>あなたのブラウザは %s です<h2>''' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>こんにちは、%s<h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
