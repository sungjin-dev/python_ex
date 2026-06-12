def menuModify(menudict):

    for idx, value in enumerate(menudict):
        print(f'번호: {idx+1} , 상품 ID: {value}')
 
    menuId = input('변경할 메뉴 ID를 입력하세요.')

    if menuId not in menudict:
        print('없는 ID입니다.')
        return

    menuName = input('변경할 메뉴를 입력하세요.')
    menuPrice = input('변경할 메뉴 가격을 입력하세요.')
    menuTag = input('변경할 메뉴 카테고리를 입력하세요.')

    menudict[menuId]['menuId'] = menuId
    menudict[menuId]['menuName'] = menuName
    menudict[menuId]['menuPrice'] = menuPrice
    menudict[menuId]['menuTag'] = menuTag

    return menudict