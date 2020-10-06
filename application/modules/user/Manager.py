import hashlib

class Manager:
    def __init__(self, db):
        self.db = db

    def registration(self, name, login, password):
        user = self.db.getUserByLogin(login)
        if user:
            return False
        token = self.__generateToken(name, login)
        self.db.insertUser(name, login, password, token)

        return token

    def auth(self, login, hash, rnd):
        if login and hash and rnd:
            if hashlib.md5(str(self.db.getHashByLogin(login) + rnd).encode("utf-8")) == hash:
                return True
        return False

    def logout(self, login):
        user = db.getUserByLogin(login)
        if user:
            db.updateTokenByLogin(login)
            return True
        return False

    def __generateToken(self, name, login = ""):

        if name and login:
            return hashlib.md5(str(name + login).encode("utf-8")).hexdigest()