from app import app
from models import db, Hero, Power, HeroPower

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create heroes
        hero1 = Hero(name='Clark Kent', super_name='Superman')
        hero2 = Hero(name='Bruce Wayne', super_name='Batman')

        # Create powers
        power1 = Power(name='Flying', description='Grants the ability to fly at high speeds.')
        power2 = Power(name='Super Strength', description='Grants incredible physical strength.')

        # Add relationships
        hp1 = HeroPower(hero=hero1, power=power1, strength='Strong')
        hp2 = HeroPower(hero=hero2, power=power2, strength='Average')

        db.session.add_all([hero1, hero2, power1, power2, hp1, hp2])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
