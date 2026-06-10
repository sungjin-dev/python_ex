import database
from order import config as order_config

class OrderService:
    def __init__(self, menuInfos):
        self.filename = "orders.json"
        self.menudict = menuInfos
        self.orders = {}

        self.menudict = database.save_data(self.filename, self.menudict)  

    def orderRegister(self):
        pass    

    def run(self):

        flag = True
        while flag:
            selectedNum = int(input('1. 주문 입력, 2. 주문 현황, 3.주문 수정, 4. 결제금액, 99.종료' ))

            if selectedNum == order_config.INPUT_ORDER:
                self.register(self.menudict)  
            elif selectedNum == order_config.ORDER_STATUS:
                self.menuCheck(self.menudict)
            elif selectedNum == order_config.ORDER_MODIFY:
                self.menuModify(self.menudict)
            elif selectedNum == order_config.FINAL_PAYMENT:
                self.menuDelete(self.menudict)
            elif selectedNum == order_config.SYSTEM_OUT:
                flag = False
            else:
                print('오타거나 없는 메뉴입니다. 다시 입력해주세요.')
                return

if __name__=="__main__":
    OrderService().run()
