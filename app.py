from aiohttp import web
from application.modules.user.User import User
from application.modules.user.Manager import Manager
from settings import SETTINGS
from application.modules.db.DB import DB
from application.modules.mediator.Mediator import Mediator
# user
# chat
# audio ?
# pirates
from application.router.Router import Router

db = DB(SETTINGS['DB'])
manager = Manager(db)
mediator = Mediator(SETTINGS['MEDIATOR']['EVENTS'], SETTINGS['MEDIATOR']['TRIGGERS'])

#mediator.set('GET_USER_BY_ID', db.getUserById)
#mediator.set('GET_USER_BY_TOKEN', db.getUserByToken)
#mediator.get('GET_USER_BY_ID', '1')

user = User("1", "vasya", "12345555", "12345", "12345")

manager.registration("andrew","123","123")


app = web.Application()
Router(app, web, mediator)



web.run_app(app)