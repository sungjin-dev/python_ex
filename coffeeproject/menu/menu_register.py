def menuResister(menudict):

    menuId = input('추가할 메뉴 ID를 입력하세요.')
    menuName = input('추가할 메뉴를 입력하세요.')
    menuPrice = input('추가할 메뉴 가격을 입력하세요.')
    menuTag = input('추가할 메뉴 카테고리를 입력하세요. (주류 or 안주)')

    if menuId in menudict:
        print('이미 존재하는 ID입니다.')
        return

    menuItems = {
        'menuId': menuId,
        'menuName': menuName,
        'menuPrice': menuPrice,
        'menutag':menuTag,
    } 

    menudict[menuId] = menuItems

    return menudict
