from flask import Blueprint, session, render_template, request, redirect, flash, get_flashed_messages
from werkzeug.exceptions import abort
from flask.helpers import url_for
from modules import db, login_manager
from modules.auth.model.user import User, LoginForm, RegisterForm
from flask_login import login_user, logout_user, current_user, login_required

fauth = Blueprint('fauth', __name__)

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(user_id)


@fauth.route('/register', methods=['GET', 'POST'])
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

@fauth.route('/login', methods=['GET', 'POST'])
def login():
   if current_user.is_authenticated:
      flash("Usuario ya autenticado.")
      return redirect(url_for('product.index'))

   form = LoginForm(meta={'csrf': False})

   if form.validate_on_submit():
      user = User.query.filter_by(username = form.username.data).first()

      if user and user.check_password(form.password.data):
         login_user(user)
         flash("Bienvenido, " + user.username)
         next = request.form['next']

         #if not is_safe_url(next):
            #return abort(400)

         return redirect(next or url_for('product.index'))
      else:
         flash("Credenciales incorrectas.")
   
   if form.errors:
      flash(form.errors, 'danger')

   return render_template('auth/login.html', form=form)

@fauth.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('fauth.login'))

@fauth.route('/protegido')
@login_required
def protegido():
   return "Vista protegida"