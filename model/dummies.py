
from model.address import *
from model.product import *
from model.customer import *
from model.firm import *
from model.user import *
from model.order import *


addressInstance = AddressModel()
productInstance = ProductModel()
customerInstance = CustomerModel()
firmInstance = FirmModel()
userInstance = UserModel()
orderInstance = OrderModel()

def DeleteAllTable():

    OrderModel().drop()
    ProductModel().drop()
    FirmModel().drop()
    CustomerModel().drop()
    addressInstance.drop()
    UserModel().drop()






def CreateAllTable():
    createAddressTable()
    createUserTable()
    createCustomerTable()
    createFirmTable()
    createProductTable()
    createOrderTable()

#if user type==0 then it is type of customer otherwise "1" it is type of firm
def InsertUser():

    create_user("testcustomer", "1234", "testcustomer@mail.com", 0)
    create_user("testfirm", "1234", "testfirm@mail.com", 1)

    create_user("testcustomer1", "1234", "testcustomer1@mail.com", 0)
    create_user("testfirm1", "1234", "testfirm1@mail.com",1)

    create_user("testcustomer2", "1234", "testcustomer2@mail.com", 0)
    create_user("testfirm2", "1234", "testfirm2@mail.com",1)


def InsertAddress():

    createAddress("Altınbasak", 9, 10, "Maslak", "Istanbul", 2000)
    createAddress("Cicek", 2, 11, "Ayazaga", "Istanbul", 2100)
    createAddress("Kagıt", 3, 12, "Besiktas", "Istanbul", 1000)
    createAddress("Havuzbası", 4, 13, "Uskudar", "Istanbul", 1000)

def InsertFirm():

    createFirm("Marmara", 1, 2, 21600000)
    createFirm("Karadeniz", 2, 4, 21600001)
    createFirm("Ege", 3, 6, 21600002)

def InsertCustomer():

    createCustomer("testName", 1, 2160010, 1)
    createCustomer("testName1", 2, 2160011, 3)
    createCustomer("testName2", 3, 2160012, 5)

def InsertOrder():

    createOrder(1, 1)
    createOrder(2, 2)
    createOrder(3, 3)

def InserProduct():

    createProduct("Hamburger", 1, 10.0)
    createProduct("Sandwich", 2, 25.0)
    createProduct("Tost", 1, 5.0)

def CreateStarter():

    InsertUser()
    InsertAddress()
    InsertCustomer()
    InsertFirm()
    InserProduct()
    InsertOrder()













