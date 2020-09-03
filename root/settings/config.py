import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Adjusts(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'contraseña'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False