from customer import config as customer_config
import database
from customer import customer_signup
from customer import customer_modify
from customer import customer_delete

class customerService:
    def __init__(self):
        self.fileName = "customer.json"
        self.customerdict = {}

        self.customerdict = database.load_data(self.fileName, self.customerdict)

    def sign_up(self):
        customer_signup.signUp(self.customerdict)
        database.save_data(self.fileName, self.customerdict)
    def sign_in(self):
        pass

    def modifyinfo(self):
        customer_modify.modify(self.customerdict)
        database.save_data(self.fileName, self.customerdict)
    def deleteinfo(self):
        customer_delete.delete(self.customerdict)
        database.save_data(self.fileName, self.customerdict)
   
    def run(self):

        flag = True

        while flag:

            selectedNum = int(input('1. sign-up 2. sign-in  3. modify 4. delete 0. back to main'))  

            if  selectedNum == customer_config.RESISTER:
                self.sign_up() 
            elif  selectedNum == customer_config.INFOCHECK:
                self.sign_in()  
            elif  selectedNum == customer_config.MODIFY:
                self.modifyinfo()    
            elif  selectedNum == customer_config.DELETE:
                self.deleteinfo() 
            elif  selectedNum == customer_config.BACKTOMAIN:
                flag = False 

if __name__ == "__main__":
    customerService().run()