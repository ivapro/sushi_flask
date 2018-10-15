from app import login
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, ID, username, password, points):
        self.id = ID
        self.username = username
        self.password = password
        self.point = points

    def is_active(self):
        return self.is_active()

    def is_anonymous(self):
        return self.is_anonymous()

    def is_authenticated(self):
        return self.is_authenticated()

    def get_id(self):
        return self.id


@login.user_loader
def load_user(id):
    return User.query.get(int(id))