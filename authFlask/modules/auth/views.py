from flask import Blueprint, session, render_template, request, redirect, flash, get_flashed_messages
from flask.helpers import url_for
from modules import db
from modules.auth.model.user import User, LoginForm, RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
   form = RegisterForm(meta={'csrf': False})

   if form.validate_on_submit():
      if User.query.filter_by(username = form.username.data).first():
         flash("Usuario no válido.", 'danger')
      else:
         u = User(form.username.data, form.password.data)
         db.session.add(u)
         db.session.commit()
         flash("Usuario creado exitosamente.")
         return redirect(url_for('auth.register'))
   
   if form.errors:
      flash(form.errors, 'danger')

   return render_template('auth/register.html', form=form)  

@auth.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm(meta={'csrf': False})

   if form.validate_on_submit():
      user = User.query.filter_by(username = form.username.data).first()

      if user and user.check_password(form.password.data):
         session['id'] = user.id
         session['username'] = user.username
         session['rol'] = user.rol.value
         flash("Bienvenido, " + user.username)
         return redirect(url_for('product.index'))
      else:
         flash("Credenciales incorrectas.")
   
   if form.errors:
      flash(form.errors, 'danger')

   return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
   session.pop('id')
   session.pop('username')
   session.pop('rol')
   return redirect(url_for('auth.login'))