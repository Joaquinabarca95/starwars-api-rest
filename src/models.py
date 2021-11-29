from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


user_character_fav = db.Table('user_character_fav',
    db.Column('id_user', db.Integer, db.ForeignKey('users.id'),primary_key=True),
    db.Column('id_character', db.Integer, db.ForeignKey('characters.id'),primary_key=True)
)
user_planet_fav = db.Table('user_planet_fav',
    db.Column('id_user', db.Integer, db.ForeignKey('users.id'),primary_key=True),
    db.Column('id_character', db.Integer, db.ForeignKey('planets.id'),primary_key=True)
)
user_starship_fav = db.Table('user_starship_fav',
    db.Column('id_user', db.Integer, db.ForeignKey('users.id'),primary_key=True),
    db.Column('id_starship', db.Integer, db.ForeignKey('starships.id'),primary_key=True)
)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), default="")
    last_name = db.Column(db.String(80), default="")
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites_character= db.relationship('Character', secondary=user_character_fav)
    favorites_planet= db.relationship('Planet', secondary=user_planet_fav)
    favorites_starship= db.relationship('Starship', secondary=user_starship_fav)
    
    def serialize(self):
        return {
            "user_id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
    
    def serialize_with_favorites(self):
        return {            
            "user_id":self.id,
            "first_name": self.first_name,
            "favorites":{
                "favorite_planets": list(map(lambda planet: planet.serialize(), self.favorites_planet)),
                "favorites_character": list(map(lambda character: character.serialize(), self.favorites_character)),
                "favorite_starship": list(map(lambda starship: starship.serialize(), self.favorites_starship))
            }
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Float())
    mass = db.Column(db.Float())
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(15))
    starship = db.Column(db.Integer, db.ForeignKey('starships.id'))
    homeworld = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def serialize(self):
        return {
            "character_id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "starship": self.starship,
            "homeworld": self.homeworld
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    rotation_period = db.Column(db.Float())
    orbital_period = db.Column(db.Float())
    diameter = db.Column(db.Float())
    climate = db.Column(db.String(20))
    gravity = db.Column(db.String(20))
    terrain = db.Column(db.String(20))
    surface_water = db.Column(db.Float())
    population = db.Column(db.Integer)

    def serialize(self):
        return {
            "planet_id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Starship(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(50))
    length = db.Column(db.Integer)
    starship_class = db.Column(db.String(50))

    def serialize(self):
        return {
            "starship_id": self.id,
            "name": self.name,
            "model": self.model,
            "length": self.length,
            "starship_class": self.starship_class
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
