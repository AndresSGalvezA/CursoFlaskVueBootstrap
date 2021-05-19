from flask import Blueprint, render_template, request, redirect, flash, get_flashed_messages
from flask.helpers import url_for
from modules import db
from sqlalchemy.sql.expression import not_, or_
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from modules.product.model.products import PRODUCTS
from modules.product.model.product import Product, ProductForm

product = Blueprint('product', __name__)

@product.route('/product')
@product.route('/product/<int:page>')
def index(page=1):
   return render_template('product/index.html', products = Product.query.paginate(page, 5))

@product.route('/product/<int:id>')
def show(id):
   product = Product.query.get_or_404(id)
   return render_template('product/show.html', product = product)

@product.route('/create-product', methods=['GET', 'POST'])
def create():
   form = ProductForm(meta={'csrf': False})

   if form.validate_on_submit():
      p = Product(request.form.get('name'), request.form.get('price'))
      db.session.add(p)
      db.session.commit()
      flash("Producto guardado exitosamente.")
      return redirect(url_for('product.create'))
   
   if form.errors:
      flash(form.errors, 'danger')

   return render_template('product/create.html', form=form)  

@product.route('/update-product/<int:id>', methods=['GET', 'POST'])
def update(id):
   form = ProductForm(meta={'csrf': False})
   product = Product.query.get_or_404(id)

   if request.method == 'GET':
      form.name.data = product.name
      form.price.data = product.price

   if form.validate_on_submit():
      product.name = form.name.data
      product.price = form.price.data
      db.session.add(product)
      db.session.commit()
      flash("Producto actualizado exitosamente.")
      return redirect(url_for('product.update', id=product.id))
   
   if form.errors:
      flash(form.errors, 'danger')


   return render_template('product/update.html', product=product, form=form)

@product.route('/test')
def test():
   # Consultas
   # p = Product.query.limit(2).all()
   # p = Product.query.first()
   # p = Product.query.order_by(Product.id.desc()).limit(3).all()
   # p = Product.query.get({ "id": 1})
   # p = Product.query.filter_by(name = "Producto 2").all()
   # p = Product.query.filter(Product.id > 1).all()
   # p = Product.query.filter_by(id = 2, name = "Producto 2").all()
   # p = Product.query.filter(Product.name.like('Producto%')).all()
   # p = Product.query.filter(not_(Product.id > 2)).all()
   # p = Product.query.filter(or_(Product.id > 2, Product.name == "Producto 2")).all()
   # print(p)

   # Crear
   # p = Product("Producto 5", 60.8)
   # db.session.add(p)
   # db.session.commit()

   # Actualizar
   # p = Product.query.filter_by(name = "Producto 1", id = 1).first()
   # p.name = "Teléfono 1"
   # db.session.add(p)
   # db.session.commit()

   # Eliminar
   # p = Product.query.filter_by(id = 5).first()
   # db.session.delete(p)
   # db.session.commit()
   return "CRUD"

@product.route('/delete-product/<int:id>')
def delete(id):
   product = Product.query.get_or_404(id)
   db.session.delete(product)
   db.session.commit()
   flash("Producto eliminado exitosamente.")
   return redirect(url_for('product.index'))

@product.route('/filter/<int:id>')
def filter(id):
   product = PRODUCTS.get(id)
   return render_template('product/filter.html', product = product)

@product.app_template_filter('iva')
def iva_filter(product):
   if product['price']:
      return product['price'] * 0.12
   else:
      return "Sin precio, no puede calcularse IVA."