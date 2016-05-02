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

    def test_empty_db(self):
        rv = self.app.get('/')
        assert str(rv.data).find('log in') >= 0
        assert str(rv.data).find('OneBase') >= 0

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
