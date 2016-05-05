from flask import Flask, render_template
from flask.ext.script import Manager
import random, datetime

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

# 変数
class ObjEx(object):    #オブジェクト呼び出しのためのテストクラス
    def print_today(self):
        return datetime.datetime.today()#今日の値を返す

@app.route('/variables')
def variables():
    dict_ex = {'key':'キーさんです', 'key2':555}
    list_ex = [34,'コイツです', 55.555]
    rand = random.randint(0,2) #変数渡しのテスト
    obj_ex = ObjEx()
    return render_template('variables.html',
                            mydict=dict_ex,
                            mylist=list_ex,
                            myintvar = rand,
                            myobj=obj_ex)

if __name__ == '__main__':
    manager.run()
