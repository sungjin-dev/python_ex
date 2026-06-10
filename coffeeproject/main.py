from customer import menu_service
from customer import order_service
from customer import customer_service
from customer import coupon_service
from customer import sales_service
import config as root_config

class 

flag = True

while flag:
    selectedNum = int(input('1.mene 2. order 3.customer 4.coupon 5.sale 99. system-out '))

    if selectedNum == root_config.MENU:
        menu_service.menuService().run()
    elif selectedNum == root_config.ORDER:
        order_service.orderService().run()
    elif selectedNum == root_config.CUSTOMER:
        customer_service.customerService().run()
    elif selectedNum == root_config.COUPON:
        coupon_service.couponService().run()
    elif selectedNum == root_config.SALES:
        sales_service.salesService().run()
    elif selectedNum == root_config.SYSTEM_OUT:
        flag = False

if __name__ == "__main__":
    ()