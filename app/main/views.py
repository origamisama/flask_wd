# -*- coding: utf-8 -*-

"""
ページを生成する関数
Blueprint で記述する場合の違いは2点
- routeデコレータはBlueprintより記述
- url_for('.index'): ネームスペースの違い
  blueprintごとに違うindexを作成可能
"""

from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())

