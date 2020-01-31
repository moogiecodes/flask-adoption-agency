from models import db, Pet
from app import app

db.drop_all()
db.create_all()

# add dummy pets
deejay = Pet(name='Deejay', species='cat',
             age=6, notes='very friendly', available=False)
gizmo = Pet(name='Gizmo', species='gremlin', age=100,
            notes='don\'t feed after midnight', available=True)
chili = Pet(name='Chili', species='dog', age=5,
            notes='doesn\'t care about people', available=True)

db.session.add_all([deejay, gizmo, chili])

db.session.commit()
