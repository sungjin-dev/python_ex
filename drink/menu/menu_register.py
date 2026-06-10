from util import time

def registerMenu(menudict):

    mId = input('상품 ID를 입력해주세요. ')
    mCheck = input('안주면 F, 술이면 D를 입력해주세요.')
    mName = input('메뉴명(주류명)을 입력해주세요. ')
    mPrice = input('해당 메뉴의 가격을 입력하세요. ')
    
    if mId in menudict:
        print('이미 존재하는 상품입니다.')
        return
    
    RegDate = time.getCurrentDateTime()
    ModDate = time.getCurrentDateTime()

    menuItems = {
        'mId': mId,
        'mCheck':mCheck,
        'mName': mName,
        'mPrice': mPrice,
        'RegDate': RegDate,
        'ModDate': ModDate
    } 

    menuItems[mId] = menudict  

    return menudict
