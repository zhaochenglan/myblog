# -*- encoding: utf-8 -*-
'''
@File    :   forms.py
@Time    :   2020/04/02 14:38:13
@Author  :   edgar.zhao 
@Version :   1.0
@Contact :   1101017794@qq.com
@Desc    :   None
'''

# here put the import lib
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[
                           DataRequired()], render_kw={'class': 'test'})
    password = PasswordField('Password', validators=[
        DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

