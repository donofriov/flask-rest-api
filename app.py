from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# turns off flask sqlalchemy tracker in favor of original sqlalchemy tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'vince'  # real secure lolol
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates /auth endpoint

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')

# this makes sure app.run is only run if running python app.py (which is
# __main__ in this file), if not __main__ we have imported this file from
# somewhere else
if __name__ == '__main__':
    # importing here instead of top (circular imports)
    from db import db
    db.init_app(app)
    # port=5000 isn't necessary because it's the default, debug shows html page
    app.run(port=5000, debug=True)
