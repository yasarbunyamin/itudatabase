
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint

from endpoints.utils import login_required, view, login_required_action

from model.order import *
from model.product import *
from model.customer import *

order = Blueprint('order' ,__name__, url_prefix='/order')

@login_required
@order.route("/", methods=["GET"])
@view
def getAllOrderEnd(*args, **kwargs):
    if session["logged_in"][3] == 1:
        orderAll = getAllOrder()
        if orderAll is None:
            orderAll = []
        return render_template("order/firmorders.html", orders=orderAll, **kwargs)

    else:
        id = session["logged_in"][0]
        customer = getCustomerByUserId(id)
        print(customer[0][0])

        product = []
        products = []
        if customer is None:
            customer = []
        else:
            if getOrdersByCustomerId(customer[0][0]) is None:
                products = []
            else:
                for i in getOrdersByCustomerId(customer[0][0]):
                    products.append(getProductListById(i[1])[0])
                print(products)

        if products is None:
            products = []
        return render_template("order/customerorders.html", orders=products, **kwargs)




@order.route("/create", methods = ["GET" ,"POST"])
@login_required
@view
def createOrderEnd(*args, **kwargs):
    if request.method == "GET":
        return render_template(("order/createOrder.html", *kwargs))

    product_name = request.form["productname"]
    product_price = request.form["price"]

    customer_order_id = getCustomerByUserId(session["logged_in"][0])
    product_id = getProductsByNameAndPrice(product_name, product_price)

    if customer_order_id is None:
        customer_order_id = []
    if product_id is None:
        product_id = []
    print(product_id[0][0], customer_order_id[0][0])

    createOrder(product_id[0][0], customer_order_id[0][0])
    return redirect(url_for("order.getAllOrderEnd"))


@order.route("/delete/<id>" ,methods = ["GET" ,"POST"])
@login_required
@view
def deleteOrderEnd(id ,*args ,**kwargs):
    deleteOrderById(id)
    return redirect(url_for("order.getAllOrderEnd"))


@order.route("/update/<id>", methods =["GET" ,"POST"])
@login_required
@view
def updateOrderEnd(id ,*args ,**kwargs):

    order = getOrderListById(id)
    if request.method == "GET":
        if order is None:
            redirect(url_for("user.feed"))
        else:
            return render_template("order/updateOrders.html", orders= order)

    product_id = request.form["product_id"]
    customer_order_id = request.form["customer_order_id"]


    updateOrder(id,product_id  ,customer_order_id )

    return redirect(url_for('order.getOrderByIdEnd', id = id))



