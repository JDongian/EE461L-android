from user import User
from user import db

def setup_database():
    db.drop_all()
    db.create_all()
    users = [User('admin@jdong.me', 'admin'),
            User('test', 'test'),
            User('guest@jdong.me', 'guest')]
    for user in users:
        db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    setup_database()
