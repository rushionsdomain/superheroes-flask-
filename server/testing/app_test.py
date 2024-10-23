from app import app, db
from models import Hero, Power, HeroPower
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_get_heroes(client):
    response = client.get('/heroes')
    assert response.status_code == 200

def test_get_hero_by_id(client):
    hero = Hero(name='Test Hero', super_name='Test Super')
    db.session.add(hero)
    db.session.commit()

    response = client.get(f'/heroes/{hero.id}')
    assert response.status_code == 200

def test_invalid_hero_id(client):
    response = client.get('/heroes/999')
    assert response.status_code == 404

def test_create_hero_power(client):
    hero = Hero(name='Test Hero', super_name='Test Super')
    power = Power(name='Invisibility', description='Become invisible to the naked eye.')
    db.session.add_all([hero, power])
    db.session.commit()

    response = client.post('/hero_powers', json={
        'hero_id': hero.id,
        'power_id': power.id,
        'strength': 'Strong'
    })
    assert response.status_code == 201

def test_invalid_power_description(client):
    power = Power(name='Weak Power', description='Short desc')
    db.session.add(power)
    db.session.commit()

    response = client.patch(f'/powers/{power.id}', json={
        'description': 'New'
    })
    assert response.status_code == 400
