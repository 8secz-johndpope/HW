from application.modules.db.DB import DB as DB


class User:
    def __init__(self, userId, name, login, password, token):
        self.userId = userId
        self.name = name
        self.login = login
        self.password = password
        self.token = token
