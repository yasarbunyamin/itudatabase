from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint
import datetime
from endpoints.utils import login_required, view, login_required_action

from model.product import *
from model.firm import *

product = Blueprint('product', __name__, url_prefix='/product')

@product.route("/",methods = ["GET"])
@view
def getAllProductEnd(*args, **kwargs):


    if session["logged_in"][3] == 1:
        id = session["logged_in"][0]
        print(id)
        firm = getFirmByUserId(id)
        product = getProductsBySupplierId(firm[0][0])
        if product is None:
            product = []
        return render_template("product/firmproducts.html", products=product, **kwargs)

    else:
        product = getAllProduct()
    if product is None:
        product = []
    return render_template("product/products.html", products=product, **kwargs)


@product.route("/<id>", methods=["GET"])
@view
def getProductByIdEnd(id,*args,**kwargs):
    product = getProductListById(id)
    if product is None:
        return redirect(url_for("user.feed"))
    else:
        return render_template("product/products.html", products=product[0],**kwargs)

@product.route("/create",methods = ["GET","POST"])
@login_required
@view
def createProductEnd(*args,**kwargs):

    if request.method == "GET":
        return render_template("product/createProduct.html", **kwargs)

    product_name  = request.form["productname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    product_price = request.form["price"]
    createProduct(product_name, supplier[0][0], product_price)

    return redirect(url_for("product.getAllProductEnd"))

@product.route("/delete/<id>",methods =["GET","POST"])
@login_required
@view
def deleteProductByIdEnd(id, *args,**kwargs):
    deleteProduct(id)
    return (url_for("product.getAllProductEnd"))

@product.route("/delete/", methods =["GET","POST"])
@login_required
@view
def deleteProductByNameEnd( *args, **kwargs):
    if request.method == "GET":
        return render_template("product/deleteproducts.html", **kwargs)
    name = request.form["productname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    product = deleteProductByName(name, supplier[0][0])

    return redirect(url_for("product.getAllProductEnd"))


@product.route("/update", methods=["GET", "POST"])
@login_required
@view
def updatePriceByNameEnd( *args, **kwargs):
    if request.method == "GET":
        return render_template("product/updateproducts.html", **kwargs)
    price = request.form["price"]
    name  = request.form["productname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    product = updateProductByName(price, name, supplier[0][0])

    return redirect(url_for("product.getAllProductEnd"))