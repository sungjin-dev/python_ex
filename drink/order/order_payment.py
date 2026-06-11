def payment(menudict, orders):

    totalPayment = 0

    mids = sorted(menudict, reverse=True)

    for id in mids:

        mPrice = menudict[id]['mPrice']   

        oCount = orders[id]['oCount']      
    
        orderPayment = mPrice * oCount

        totalPayment += orderPayment
        
    return totalPayment 

