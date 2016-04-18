from flask import Flask
from flask import redirect, url_for, abort, render_template, flash
from flask import request, session, g, jsonify
from flask.ext.login import LoginManager
from flask.ext.login import login_user, logout_user, current_user, login_required

from user import User
from user import db as userdb

from forms import LoginForm

app = Flask(__name__)
app.config.from_object("config")

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)


@app.route('/api/login', methods=['POST'])
def api_login():
    """Login the current user by processing the form.
    Something is gravely wrong here."""
    #import IPython; shell = IPython.terminal.embed.InteractiveShellEmbed(); shell.mainloop()
    data = request.form
    print(data)
    user = User.query.get(data['username'])
    print(user)
    if user:
        print('user ok')
        user.check_password(data['password'])
        print('user checked')
        if user.is_authenticated():
            print('user authed')
            login_user(user, remember=True)
            print('user logged in')
        return jsonify(**{'logged_in': True})
    else:
        return jsonify(**{'logged_in': False})

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Display the login form."""
    #print(userdb)

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.username.data)

        login_user(user, remember=True)

        flash(u'Successfully logged in as %s' % form.user.username)

        # Secure against open redirects
        #next_url = request.args.get('next')
        #if not next_is_valid(next_url):
        #    return flask.abort(400)

        #return redirect(next_url or url_for('index'))
        return redirect(url_for('index'))
    else:
        flash(u'Invalid username or password')
        return render_template('login.html', form=form)


@app.route('/api/logout', methods=['GET', 'POST'])
@login_required
def api_logout():
    logout_user()
    return jsonify(**{'action': 'logout'})

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    # wtf is this
    api_logout()
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    import sys

    debug_mode = False
    if len(sys.argv) > 1 and sys.argv[1] == "DEBUG":
        debug_mode = True

    app.run(debug=debug_mode)
