from root import app
from root.forms import FormLogin
import os #para ejecutar comanmdos linux
from flask import render_template, request, send_from_directory, send_file

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    selectedFile = request.files['selectedFile'] #variable fileStorage recibida del form 'selectedFile' (en index.html)
    selectedFile_name = selectedFile.filename
    selectedFile_route = 'root/static/uploads/{}'.format(selectedFile_name) #probar con ruta absoluta de modo
    selectedFile.save(selectedFile_route)
    os.system('cd root/static/uploads && mkdir dir5')
    
    return selectedFile.filename

@app.route('/return_file', methods=['GET','POST'])
def return_file():
    return send_file('routes.py')


@app.route('/login', methods=['GET','POST'])
def login():
    form = FormLogin()
    return render_template('login.html', form = form)
