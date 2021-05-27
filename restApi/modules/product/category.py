from flask import Blueprint, render_template, request, redirect, flash, get_flashed_messages
from flask.helpers import url_for
from flask_login import login_required
from modules import db, rol_admin_need
from sqlalchemy.sql.expression import not_, or_
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from modules.product.model.category import Category, CategoryForm

category = Blueprint('category', __name__)

@category.before_request
@login_required
@rol_admin_need
def constructor():
   pass

@category.route('/category')
@category.route('/category/<int:page>')
def index(page=1):
   return render_template('category/index.html', categories = Category.query.paginate(page, 5))

@category.route('/category/<int:id>')
def show(id):
   category = Category.query.get_or_404(id)
   return render_template('category/show.html', category = category)

@category.route('/create-category', methods=['GET', 'POST'])
def create():
   form = CategoryForm(meta={'csrf': False})

   if form.validate_on_submit():
      p = Category(request.form.get('name'))
      db.session.add(p)
      db.session.commit()
      flash("Categoría guardada exitosamente.")
      return redirect(url_for('category.create'))
   
   if form.errors:
      flash(form.errors, 'danger')

   return render_template('category/create.html', form=form)  

@category.route('/update-category/<int:id>', methods=['GET', 'POST'])
def update(id):
   form = CategoryForm(meta={'csrf': False})
   category = Category.query.get_or_404(id)

   if request.method == 'GET':
      form.name.data = category.name

   if form.validate_on_submit():
      category.name = form.name.data
      db.session.add(category)
      db.session.commit()
      flash("Categoría actualizada exitosamente.")
      return redirect(url_for('category.update', id=category.id))
   
   if form.errors:
      flash(form.errors, 'danger')


   return render_template('category/update.html', category=category, form=form)

@category.route('/test')
def test():
   # Consultas
   # p = Category.query.limit(2).all()
   # p = Category.query.first()
   # p = Category.query.order_by(Category.id.desc()).limit(3).all()
   # p = Category.query.get({ "id": 1})
   # p = Category.query.filter_by(name = "Categoryo 2").all()
   # p = Category.query.filter(Category.id > 1).all()
   # p = Category.query.filter_by(id = 2, name = "Categoryo 2").all()
   # p = Category.query.filter(Category.name.like('Categoryo%')).all()
   # p = Category.query.filter(not_(Category.id > 2)).all()
   # p = Category.query.filter(or_(Category.id > 2, Category.name == "Categoryo 2")).all()
   # print(p)

   # Crear
   # p = Category("Categoryo 5", 60.8)
   # db.session.add(p)
   # db.session.commit()

   # Actualizar
   # p = Category.query.filter_by(name = "Categoryo 1", id = 1).first()
   # p.name = "Teléfono 1"
   # db.session.add(p)
   # db.session.commit()

   # Eliminar
   # p = Category.query.filter_by(id = 5).first()
   # db.session.delete(p)
   # db.session.commit()
   return "CRUD"

@category.route('/delete-category/<int:id>')
def delete(id):
   category = Category.query.get_or_404(id)
   db.session.delete(category)
   db.session.commit()
   flash("Categoryo eliminado exitosamente.")
   return redirect(url_for('category.index'))

@category.route('/filter/<int:id>')
def filter(id):
   category = PRODUCTS.get(id)
   return render_template('category/filter.html', category = category)

@category.app_template_filter('iva')
def iva_filter(category):
   if category['price']:
      return category['price'] * 0.12
   else:
      return "Sin precio, no puede calcularse IVA."