# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
# Webform用のクラス
class NameForm(Form):
    name = StringField('あなたのお名前は？', validators=[Required()])
    submit = SubmitField('送信')
