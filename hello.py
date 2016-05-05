from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

# 基本
@app.route('/')
def index():
    return render_template('index.html')

# URIから受け取り
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

if __name__ == '__main__':
    manager.run()
