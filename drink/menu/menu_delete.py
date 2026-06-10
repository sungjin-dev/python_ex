def menuDelete(menudict):

    if not menudict:
        print('등록된 상품이 없습니다.')
        return menudict

    sortedMenus = menudict.sorted(reverse = False)

    print(f'상품ID LIST: {sortedMenus}')
    
    selectedId = input('삭제할 상품(ID)을 선택하세요.') 

    if selectedId not in menudict:
        print('오타거나 없는 ID입니다.')
        return
    else: 
        del menudict[selectedId]

    return menudict
