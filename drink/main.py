from menu import menu_service
from order import order_service
import config as root_config

def main():

    flag = True

    while flag:
        selectedNum = int(input('1.Menu 2. Order 99. system-out '))

        if selectedNum == root_config.MENU:
            menu_service.MenuService().run()
        elif selectedNum == root_config.ORDER:
            order_service.OrderService().run()
        elif selectedNum == root_config.SYSTEM_OUT:
            flag = False
        else:
            print('오타입니다. 다시 입력해주세요.')

if __name__ == "__main__":
        ()