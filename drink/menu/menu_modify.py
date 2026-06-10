from util import time

def menuModify(menudict):

    if not menudict:
        print('등록된 상품이 없습니다.')
        return menudict
    
    print(f'상품ID LIST: {menudict}')
    
    selectedId = input('변경할 상품을 선택하세요.') 

    if selectedId not in menudict:
        print('오타거나 없는 ID입니다.')
        return
    else: 
        mCheck = input('안주면 F, 술이면 D를 입력해주세요.')
        mName = input('메뉴명(주류명)을 입력해주세요.')
        mPrice = input('해당 메뉴의 가격을 입력하세요.')

        ModDate = time.getCurrentDateTime()

        menudict[selectedId]['mCheck'] = mCheck
        menudict[selectedId]['mName'] = mName
        menudict[selectedId]['mPrice'] = mPrice
        menudict[selectedId]['ModDate'] = ModDate

        return menudict
