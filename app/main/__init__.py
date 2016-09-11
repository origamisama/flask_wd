# -*- cofing: utf-8 -*-

"""
Blueprintの作成
"""

from flask import Blueprint

main = Blueprint('main', __name__)
# Blueprintの引数にはblueprint name とモジュールのある場所を渡す

from . import views, errors
# この2つはコード最下部へ記述する: 循環参照を回避するため
#（この2つを使用するためにはmainをインポートする必要があるため)
