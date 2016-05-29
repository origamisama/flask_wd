from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
import random, datetime, os

basedir = os.path.abspath(os.path.dirname(__file__)) # hello.pyの存在するディレクトリ

# 各種オブジェクト生成
app = Flask(__name__) # appオブジェクト
manager = Manager(app) # flask-manager使用のためのオブジェクト
bootstrap = Bootstrap(app) # flask-bootstrap使用のためのオブジェクト
moment = Moment(app) # flask-moment使用のためのオブジェクト

# app.config 設定
app.config['SECRET_KEY'] = 'easytoguess' # flask-WTFで使用するシークレットキー（普通はなんかの乱数）
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite') # sqliteのベースディレクトリ指定
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] =True # データベース変更時に自動コミットする設定

# db操作用のオブジェクト生成
db = SQLAlchemy(app)

# Webform用のクラス
class NameForm(Form):
    name = StringField('あなたのお名前は？', validators=[Required()])
    submit = SubmitField('送信')

# SQLAlchemyのテスト用クラス
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic') # usersテーブルへの逆参照,roleをroles_idの代わりに使える？  

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


# 基本
@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('名前変えたね？')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
                           current_time=datetime.datetime.utcnow(),
                           form = form,
                           name = session.get('name')
                           )

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

@app.route('/form', methods=['GET','POST'])
def form():
    form = NameForm()
    return render_template('form.html',form=form)

if __name__ == '__main__':
    manager.run()


