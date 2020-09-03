from root import app, bdd
from root.tables import User, File

@app.shell_context_processor
def make_shell_context():
  return {'bdd':bdd,'User':User, 'File':File}