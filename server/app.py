from flask import Flask, jsonify, request, abort
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Routes for Heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get_or_404(id)
    return jsonify(hero.to_dict())

# Routes for Powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def handle_power(id):
    power = Power.query.get_or_404(id)

    if request.method == 'PATCH':
        data = request.get_json()
        if 'description' in data and len(data['description']) < 20:
            abort(400, description="Description must be at least 20 characters")
        power.description = data.get('description', power.description)
        db.session.commit()
        return jsonify(power.to_dict())

    return jsonify(power.to_dict())

# Routes for HeroPower
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    if data['strength'] not in ['Strong', 'Weak', 'Average']:
        abort(400, description="Invalid strength value")

    hero_power = HeroPower(
        hero_id=data['hero_id'],
        power_id=data['power_id'],
        strength=data['strength']
    )
    db.session.add(hero_power)
    db.session.commit()
    return jsonify(hero_power.to_dict()), 201
