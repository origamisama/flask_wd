# -*- coding: utf-8 -*-

"""
エラーハンドラについて記述
errorhandler: 特定のblueprint内でのみ動作するエラー
app_errorhandler: app下部全体のエラーについて記述できる
"""

from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 505

