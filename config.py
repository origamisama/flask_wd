# -*- coding: utf-8 -*-

"""
アプリケーションの設定を行うモジュール
アプリケーションを生成するときに呼ばれ、各種パラメータを設定する
開発、テスト、商用の3設定を想定
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__)) # このファイルが存在するディレクトリ

class Config:
    """全てのconfigで使用されるパラメータを保持"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True # Commit自動実行
    MAIL_SUBJECT_PREFIX = '[Flask Web Development]' # 名称変更
    MAIL_SENDER = 'Flask Web Development Admin <flask_wd@example.com>' # 名称変更
    ADMIN = os.environ.get('FLASK_WD_ADMIN')

    @staticmethod
    def init_app(app):
        """appを変数として扱い特定の初期設定を行える"""
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestConfig(Config):
    TESTING = True # テストのためにはこれを加える必要あり
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

