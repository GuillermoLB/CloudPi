from root import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    selectedFile = request.files['selectedFile'] #variable fileStorage
    selectedFile_name = selectedFile.filename
    selectedFile_route = 'root/static/uploads/{}'.format(selectedFile_name) #probar con ruta absoluta de modo
    selectedFile.save(selectedFile_route)
    return selectedFile.filename