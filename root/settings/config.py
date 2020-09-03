import os

class Adjusts(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'contraseña'