import os
import app
import unittest
import tempfile
import setup

class AppTestCase(unittest.TestCase):
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ), follow_redirects=True)

        def logout(self):
            return self.app.get('/logout', follow_redirects=True)

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        # app.init_db()
        setup.setup_database()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def test_web_index(self):
        rv = self.app.get('/')
        assert str(rv.data).find('log in') >= 0
        assert str(rv.data).find('OneBase') >= 0

    def test_web_category(self):
        #cat = self.app.get('/category')
        #assert str(cat.data).find('Select Category') >= 0
        pass

    def test_web_inventory(self):
        inv = self.app.get('/inventory')
        assert str(inv.data).find('OneBase') >= 0

    def test_web_home(self):
        ho = self.app.get('/home')
        assert str(ho.data).find('We are OneBase') >= 0

    def test_web_about(self):
        ab = self.app.get('/about')
        assert str(ab.data).find('database management tool') >= 0

    def test_web_contact(self):
        con = self.app.get('/contact')
        assert str(con.data).find('following emails') >= 0

    def test_web_login(self):
        lg = self.app.get('/login')
        assert str(lg.data).find('Login') >= 0

    def test_web(self):
        self.test_web_index()
        self.test_web_category()
        self.test_web_inventory()
        self.test_web_home()
        self.test_web_about()
        self.test_web_contact()
        self.test_web_login()


#    def test_login_logout(self):
#        rv = self.login('admin', 'default')
#        assert 'You were logged in' in rv.data
#        rv = self.logout()
#        assert 'You were logged out' in rv.data
#        rv = self.login('adminx', 'default')
#        assert 'Invalid username' in rv.data
#        rv = self.login('admin', 'defaultx')
#        assert 'Invalid password' in rv.data


if __name__ == '__main__':
    unittest.main()
