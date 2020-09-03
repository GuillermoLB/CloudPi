from root import bdd, login
from datetime import datetime

from werkzeug.security import generate_password_hash as genph #generar hash
from werkzeug.security import check_password_hash as checkph #descifrar hash

from flask_login import UserMixin


class User(UserMixin, bdd.Model):
  id = bdd.Column(bdd.Integer, primary_key=True)
  username = bdd.Column(bdd.String(64), index=True, unique=True)
  password = bdd.Column(bdd.String(128))
  files = bdd.relationship('File', backref='user', lazy='dynamic')

  def __repr__(self):
    return '<User {}>'.format(self.username)

  #asignar al atributo password la clave con el hash
  def def_password(self, key):
    self.password = genph(key)


  #devuelve true si el atributo password coincide con la key pasada
  def verif_password(self, key):
    return checkph(self.password, key)

  def return_files(self):
    return self.Files.query.filter_by(id_usuario=self.id)

class File(bdd.Model):
  id = bdd.Column(bdd.Integer, primary_key=True)
  filename = bdd.Column(bdd.String(256), index=True, unique=True)
  timestamp = bdd.Column(bdd.DateTime, index=True, default=datetime.now)
  id_user = bdd.Column(bdd.Integer, bdd.ForeignKey('user.id'))


@login.user_loader
def load_user(id):
  return User.query.get(int(id))