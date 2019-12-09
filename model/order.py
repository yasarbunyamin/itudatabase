
from model.base import Base

class OrderModel(Base):

    def __init__(self):
        super(OrderModel,self).__init__()
        self.table_name = "ORDERS"

    def create(self, *args, **kwargs):

        command = """ CREATE TABLE IF NOT EXISTS ORDERS(
            order_id serial PRIMARY KEY,
            product_id integer NOT NULL,
            customer_order_id integer NOT NULL,
            FOREIGN KEY (customer_order_id) REFERENCES CUSTOMERS(customer_id) ON UPDATE CASCADE,
            FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id) ON UPDATE CASCADE
            )
        """
        self.execute(command)
    def insert(self,*args,**kwargs):
        command = """
        INSERT INTO ORDERS(product_id,customer_order_id)
        VALUES ('{}','{}')
        """.format(*args)
        self.execute(command)

    def update(self,*args,**kwargs):

        raise NotImplementedError
    def delete(self,id):

        raise NotImplementedError
    def read(self,*args,**kwargs):
       command="""SELECT * FROM ORDERS"""
       return self.execute(command)

orderModel = OrderModel()

def createOrder(product_id,customer_order_id):
    command = """
            INSERT INTO ORDERS(product_id,customer_order_id)
            VALUES ('{}','{}')
            """.format(product_id, customer_order_id)
    return orderModel.execute(command)
def getAllOrder():
    command = """
    SELECT * FROM ORDERS"""
    order = orderModel.execute(command)
    return order
def getOrderListById(id):
    command = """SELECT * FROM ORDERS where order_id ={}""".format(id)
    return orderModel.execute(command)

def deleteOrderById(id):
    command = """
       DELETE FROM ORDERS WHERE order_id={} 
       """.format(id)
    return orderModel.execute(command)

def updateOrder(id,product_id,customer_order_id):
    command ="""
    UPDATE ORDERS SET order_id='{}',product_id='{}',customer_order_id='{}'
    """.format(id,product_id,customer_order_id)
    return orderModel.execute(command)

def drop():
    command = """
        DELETE FROM ORDERS"""
    return orderModel.execute(command)

def createOrderTable():
    return orderModel.create()


def getOrdersByCustomerId(id):
    command = """SELECT * FROM ORDERS WHERE customer_order_id ='{}'""".format(id)
    return orderModel.execute(command)
def getProductIds(id):
    command = """SELECT product_id FROM ORDERS WHERE customer_order_id ='{}'""".format(id)
    return orderModel.execute(command)