from app import db
from sqlalchemy import Column , Integer , String
from werkzeug.security import generate_password_hash

class user(db.Model):
    __tablename__ = 'users'
    id = Column(Integer , primary_key=True )
    fullname = Column(String(60) , nullable=False , unique=False)
    email = Column(String(100) , nullable=False , unique=True)
    password = Column(String(128) , nullable=False , unique=False)
    role = Column(Integer() , nullable=True , default=0)
    def set_password(self , password):
        self.password = generate_password_hash(password)


# from mode_users.models import user
# >>> user = user()
# >>> user.fullname = 'manasoifj'
# >>> user.email = 'akjehfiahf'
# >>> user.set_password('12314')
# >>> db.session.add(user)
# >>> db.session.commit()


#  flask db init   for create migration
#  flask db migrate  for create table in migration
#  flask db upgrade  for create table in database