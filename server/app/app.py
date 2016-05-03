import json
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

g_items = {
    'plushies': {
        1000: {'name': "my little pony Honolulu", 'count': 3},
        1001: {'name': "care bear Jey", 'count': 0},
        1002: {'name': "tickle-me elmo", 'count': 4},
        1003: {'name': "pikachu plush", 'count': 50}},
    'trading cards': {
        1004: {'name': "MTG", 'count': 3032},
        1005: {'name': "yugioh", 'count': 1},
        1006: {'name': "pocket monsters", 'count': 3}},
    'spinning tops': {
        1007: {'name': "beyblade", 'count': 14},
        1008: {'name': "dreydl", 'count': 42}}}

g_cat = {'categories': ['trading cards', 'spinning tops', 'plushies']}


## API

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

@app.route('/api/logout', methods=['GET', 'POST'])
@login_required
def api_logout():
    logout_user()
    return jsonify(**{'action': 'logout'})

@app.route('/api/get_categories', methods=['GET', 'POST'])
def get_categories():
    return jsonify(**g_cat)

@app.route('/api/get_items', methods=['GET', 'POST'])
def get_items_by_category():
    # TODO: replace dummy
    data = request.form
    if not data:
        data = request.json
    category = data['category']
    print(data)
    print({'items': g_items.get(category, None)})
    return jsonify(**({'items': g_items.get(category, None)}))

@app.route('/api/add_category', methods=['GET', 'POST'])
def add_category():
    """Add a category.
    API spec:
        input: {'category': <category>}
        output: {'action': "add_category"|"none",
                 'category': <category>,
                 'status': "ok"|"category already exists"})
    """
    data = request.form
    if not data:
        data = request.json
    if not data:
        data = request.args
    category = data['category']
    g_cat['categories'].append(category)
    return jsonify(**{'action': "add_category",
                      'category': category,
                      'status': "ok"})

@app.route('/api/delete_category', methods=['GET', 'POST'])
def delete_category():
    """Delete a category.
    API spec:
        input: {'category': <category>}
        output: {'action': "delete_category"|"none",
                 'category': <category>,
                 'status': "ok"|"category already exists"})
    """
    data = request.form
    if not data:
        data = request.json
    if not data:
        data = request.args
    category = data['category']
    g_cat['categories'].remove(category)
    return jsonify(**{'action': "delete_category",
                      'category': category,
                      'status': "ok"})

@app.route('/api/insert_item', methods=['GET', 'POST'])
def insert_item():
    """Add a new item.
    API spec:
        input: {'category': <category>,
                'item_id': <item>,
                'name': <name>,
                'count': [1]}
        output: {'action': "insert_item"|"none",
                 'status': "ok"|"category not found"})
    """
    data = request.form
    if not data:
        data = request.json
    category = data['category']
    item = data['item_id']
    name = data['name']
    count = int(data.get('count', 1))
    print(data)
    print(g_items[category])
    if not item in g_items[category].keys():
        g_items[category][item] = {'name': name, 'count': count}
        result = {'action': "insert_item",
                  'status': "ok"}
    else:
        result = {'action': "none",
                  'status': "fail"}
    return jsonify(**result)


@app.route('/api/add_item', methods=['GET', 'POST'])
def add_item():
    """Add an item to a category.
    API spec:
        input: {'category': <category>,
                'item_id': <item>,
                'count': [1]}
        output: {'action': "add_item"|"none",
                 'status': "ok"|"category not found"})
    """
    data = request.form
    if not data:
        data = request.json
    category = data['category']
    item = data['item_id']
    count = int(data.get('count', 1))
    print(data)
    print(g_items[category])
    g_items[category][int(item)]['count'] += count
    result = {'action': "add_item",
              'status': "ok"}
    return jsonify(**result)

@app.route('/api/delete_item', methods=['GET', 'POST'])
def delete_item():
    """Delete an item to a category.
    API spec:
        input: {'category': <category>,
                'item_id': <item>,
                'count': [1]}
        output: {'action': "delete_item"|"none",
                 'status': "ok"|"category not found"})
    """
    data = request.form
    if not data:
        data = request.json
    category = data['category']
    item = data['item_id']
    count = int(data.get('count', 1))
    print(data)
    print(g_items[category])
    g_items[category][int(item)]['count'] -= count
    result = {'action': "delete_item",
              'status': "ok"}
    return jsonify(**result)

## Views

@app.route('/')
def index():
    return render_template('home.html')

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
        return redirect(url_for('home'))
    else:
        if form.username.data:
            flash(u'Invalid username or password')
        return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    # rip apis
    api_logout()
    return redirect(url_for('index'))

@app.route('/category')
@login_required
def category():
    #import IPython; shell = IPython.terminal.embed.InteractiveShellEmbed(); shell.mainloop()
    #categories = json.loads(category_json)['categories']
    #print(categories)
    # TODO: replace dummy
    return render_template('test.html', categories=g_cat['categories'])

@app.route('/inventory')
@login_required
def inventory():
    data = request.args
    category = data.get('category', None)
    return render_template('show_entries.html', items=g_items.get(category))

@app.route('/home')
@login_required
def home():
    # TODO: replace dummy
    return render_template('home.html')

@app.route('/about')
@login_required
def about():
    # TODO: replace dummy
    return render_template('about.html')

@app.route('/contact')
@login_required
def contact():
    # TODO: replace dummy
    return render_template('contact.html')

if __name__ == '__main__':
    import sys

    debug_mode = False
    if len(sys.argv) > 1 and sys.argv[1] == "DEBUG":
        debug_mode = True

    app.run(debug=debug_mode)
