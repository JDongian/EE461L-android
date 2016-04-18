from user import User
from user import db

def setup_database():
    db.create_all()
    users = [User('admin@jdong.me', 'admin'),
            User('guest@jdong.me', 'guest')]
    for user in users:
        db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    setup_database()
