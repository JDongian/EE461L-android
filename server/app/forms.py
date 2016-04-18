from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Required
from user import User


class LoginForm(Form):
    username = StringField('Username', [Required()])
    password = PasswordField('Password', [Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.get(self.username.data)
        if user is None:
            print('user fail')
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            print('pwd fail')
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True
