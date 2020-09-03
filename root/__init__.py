from flask import Flask

from root.settings.config import Adjusts

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Adjusts)

bdd = SQLAlchemy(app)
migrar = Migrate(app,bdd)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Por favor inicia sesión para acceder a esta página.'

from root import routes, tables