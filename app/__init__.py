# -*- coding: utf-8 -*-

"""
アプリケーションパッケージのコンストラクタ
appをグローバルスコープで宣言するのではなく、関数内で作成することで、
設定値の変更を容易にし、テストを行いやすくする

Blueprintを使用することで、appをグローバルスコープで宣言した時と
ほぼ同じようにrouteを扱えるようにする
"""

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    """ appを生成するための関数（application factory)"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # routesとerror page はここに記述
    from .main import main as main_blueprint # main->.mainに変更
    app.register_blueprint(main_blueprint)

    return app
