from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
import random, datetime

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

# 基本
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.datetime.utcnow())

# URIから受け取り
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

# 変数
class ObjEx(object):    # オブジェクト呼び出しのためのテストクラス
    def print_today(self):
        return datetime.datetime.today()  # 今日の値を返す

@app.route('/variables')
def variables():
    dict_ex = {'key':'キーさんです', 'key2':555}
    list_ex = [34,'コイツです', 55.555]
    rand = random.randint(0,2)  # 変数渡しのテスト
    obj_ex = ObjEx()
    return render_template('variables.html',
                            mydict=dict_ex,
                            mylist=list_ex,
                            myintvar = rand,
                            myobj=obj_ex)

@app.route('/filters')
def escape():
    return render_template('filters.html',
                            safe = '<h1>ふはは</h1>',
                            capitalize = 'oRZ',
                            lower = 'ORZ',
                            upper = 'otz',
                            title = 'orz orz orz',
                            trim = 'o r z',
                            striptags = '<h1>ふ<br />は<br />は</h1>'
                            )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    manager.run()
