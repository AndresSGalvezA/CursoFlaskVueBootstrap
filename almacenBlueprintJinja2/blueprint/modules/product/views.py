from flask import Blueprint, render_template
from werkzeug.exceptions import abort
from modules.product.model.products import PRODUCTS

product = Blueprint('product', __name__)

@product.route('/')
@product.route('/home')
def index():
   return render_template('product/index.html', products = PRODUCTS)

@product.route('/product/<int:id>')
def show(id):
   product = PRODUCTS.get(id)

   if not product:
      abort(404)

   return render_template('product/show.html', product = product)

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