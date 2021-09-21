"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorite, Planet, Character, Ship
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# GET users
@app.route('/api/users', methods=['GET'])
def get_users():

    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200

# GET user favorites
"""
@app.route('/api/users/favorites/', methods=['GET'])
def get_user_favorites():
    user_favorites = User.query.get(user.id)
    user_favorites = list(map(lambda user_favorite: user_favorite.serialize_with_favorites(), user_favorites))

    return jsonify(favorites), 200
"""

# GET people/characters
@app.route('/api/characters', methods=['GET'])
def get_characters():

    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))

    return jsonify(characters), 200

# GET a single character
@app.route('/api/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.filter_by(character_id=Characters.id).first()
    return jsonify(character), 200

# GET planets
@app.route('/api/planets', methods=['GET'])
def get_planets():

    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.serialize(), planets))

    return jsonify(planets), 200

# GET a single planet
@app.route('/api/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.filter_by(planet_id=Planets.id).first()
    return jsonify(planet), 200

#


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
