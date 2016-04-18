from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

class User(db.Model):
    """An admin user capable of viewing reports.

    :param str username: username address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'user'

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the username address to satisfy Flask-Login's requirements."""
        return self.username

    def logout(self):
        authenticated = False

    def check_password(self, password):
        status = password == self.password
        if status:
            authenticated = True
        return status
