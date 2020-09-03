from root import app, bdd
from root.forms import FormLogin, FormRegister
import os #para ejecutar comanmdos linux
from flask import render_template, request, send_from_directory, send_file, redirect, url_for, flash
from werkzeug.urls import url_parse

from flask_login import  current_user, login_user, login_required, logout_user

from root.tables import User, File

@app.route('/')
@app.route('/index')
@login_required
def index():
    files = current_user.files
    return render_template('index.html', files =  files)


@app.route('/', methods=['POST'])
@app.route('/index')
@login_required
def my_form_post():
    selectedFile = request.files['selectedFile'] #variable fileStorage recibida del form 'selectedFile' (en index.html)
    selectedFile_name = selectedFile.filename
    selectedFile_route = 'root/static/uploads/{}'.format(selectedFile_name)
    selectedFile.save(selectedFile_route)
    #os.system('cd root/static/uploads && mkdir dir5')

    file = File(filename=selectedFile_name, user=current_user)
    bdd.session.add(file)
    bdd.session.commit()
    
    return redirect(url_for('index'))

@app.route('/return_file')
def return_file():
    return send_from_directory(directory = "static/uploads", filename="Carta_de_pago (2).pdf", as_attachment=True)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = FormLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.verif_password(form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('index')
                return redirect(next_page)
            else:
                flash('Usuario o contraseña inválido')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/register', methods=['GET','POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = FormRegister()
  if form.validate_on_submit():
    user = User(username=form.username.data)
    user.def_password(form.password.data)
    bdd.session.add(user)
    bdd.session.commit()
    flash('Usuario registrado correctamente, ahora puedes iniciar sesión.')
    return redirect(url_for('login'))
  return render_template('register.html', form=form)