#ABC = abstract base class; by default python does not support abstrat method but we can do lil with the help of ABC method
from abc import ABC, abstractmethod

#inherit from ABC class (to become a abstract class)
class BankApp(ABC):

    def database(self):
        print("connected to data base")

#there must be atleast one abstract method (to become a abstract class)
    @abstractmethod
    def security(self):
        pass

#to access 'database()' method; MobileApp must write a security function to its class
class MobileApp(BankApp):
    def mobileLogin(self):
        print('Login to MobileApp')


    #after this function m1 object can be created below and access the database()
    def security(self):
        print("Moblile security")#passed code

#cannot create object without the implementation of security major (without security funtion in MobileApp)
m1 = MobileApp()
#TypeError: Can't instantiate abstract class MobileApp without an implementation for abstract method 'security'

m1.security()

#we cannot create the object of abstract class
object = BankApp()