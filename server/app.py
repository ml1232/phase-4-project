from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, LegoPieces, UserLegoPieces
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
api = Api(app)
db.init_app(app)

@app.route('/')

def index():

    return '<</h1>'


class Users(Resource):
    
    def get(self):
        users = [user.to_dict(rules=('-legopieces', 'userlegopieces',)) for user in 
                 Users.query.all()]
        
        return make_response(users, 200)
    

    def post(self):

        new_user = User()

        data = request.get_json()
        try:

            for key in data:

                setattr(new_user, key, data[key])

            db.session.add(new_user)

            db.session.commit()

            return make_response(new_user.to_dict(rules=('-legopieces', '-userlegopieces',)), 201) 
        
        except ValueError as error:

            new_error = {"validation errors": str(error)}

            return make_response(new_error, 400)

    
class UserById(Resource):
    def get(self, id):
        user = User.query.filter(User.id ==id).first()
        
        if not user:
            
            return make_response({"error": "User not found"}, 404)
        
        return make_response(user.to_dict(), 200)

    def post(self):
        pass
                 

class LegoPiece(Resource):
    def get(self):
        lego_pieces = [lego_piece.to_dict(rules=('-userlegopieces', '-user',)) 
                       
        for lego_piece in LegoPieces.query.all()]
        return make_response(lego_pieces, 200)
    
class UserLegoPiecesById(Resource):
    def get(self, id):
        user_lego_piece = UserLegoPieces.query.filter(LegoPieces.id == id).first()
        if not user_lego_piece:
            return make_response({"error": "Lego Piece not found"}, 404)
        return make_response(user_lego_piece.to_dict(), 200)
    
    def post(self):
        new_lego_piece = LegoPieces
        data = request.get_json()

        try:
            for key in data:
                setattr(new_user, key, data[key])
            db.session.add(new_lego_piece)
            db.session.commit()
            return make_response(new_lego_piece.to_dict(rules=('-legopieces', '-user',)), 201) 
        
        except ValueError as error:
            new_error = {"validation errors": str(error)}
            return make_response(new_error, 400)





api.add_resource(Users, '/users',)
api.add_resource(UserById, '/users/<int:id>',)   
api.add_resource(LegoPieces, '/legopieces',)
api.add_resource(LegoPiecesById, '/legopieces/<int:id>',)
api.add_resource(UserLegoPiecesById, '')


if __name__ == '__main__':

    app.run(port=5555, debug=True)



# Add Functinoality for the Lego Data Base API "Rebrickable" and cross check it with userlegopiece database



#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

