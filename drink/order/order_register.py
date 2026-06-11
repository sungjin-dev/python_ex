def orderRegister(menudict, orders):

    sortedList = sorted(menudict.items(), key=lambda x:x[1], reverse =True)

    print(f'상품목록 : {sortedList}')

    mId = input('주문한 상품의 ID를 입력하세요.')
    oCount = input(' 주문 시킨 회수를 입력하세요. ')

    orderCheck = {
        'mId':mId,
        'oCount': oCount
    }

    orderCheck[mId] = orders  

    return menudict, orders

