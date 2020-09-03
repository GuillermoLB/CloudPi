from flask import Flask
from root.settings.config import Adjusts

app = Flask(__name__)
app.config.from_object(Adjusts)

from root import routes