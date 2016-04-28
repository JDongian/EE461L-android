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
    if not data:
        data = request.json
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
    # rip apis
    api_logout()
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_categories')
def get_categories():
    # TODO: replace dummy
    return jsonify(**{'categories': ['beyblade', 'magic', 'plushies', 'adult']})

@app.route('/api/get_items', methods=['GET', 'POST'])
def get_items_by_category():
    # TODO: replace dummy
    data = request.form
    if not data:
        data = request.json
    category = data['category']
    return jsonify(**{'category': category,
        'items': ['my little pony 450', 'care bear Mysteria', 'dragon egg', 'pika plush']})


@app.route('/category')
def category():
    # TODO: replace dummy
    return render_template('test.html')

@app.route('/inventory')
def inventory():
    # TODO: replace dummy
    return render_template('show_entries.html')

@app.route('/home')
def home():
    # TODO: replace dummy
    return render_template('home.html')

@app.route('/about')
def about():
    # TODO: replace dummy
    return render_template('about.html')

@app.route('/contact')
def contact():
    # TODO: replace dummy
    return render_template('contact.html')

if __name__ == '__main__':
    import sys

    debug_mode = False
    if len(sys.argv) > 1 and sys.argv[1] == "DEBUG":
        debug_mode = True

    app.run(debug=debug_mode)
