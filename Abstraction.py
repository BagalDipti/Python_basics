
#----------------Abstraction in python-------------------------------------------------------
from  abc import ABC,abstractmethod

class Payment(ABC):
    def bill_print(self,amount):
         print(amount)

    @abstractmethod
    def payment(self,amount):
         pass


class Credit(Payment):
    def payment(self,amount):
        print(amount)

c=Credit()
c.payment(10000)
c.bill_print(10000)