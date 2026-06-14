import session

def totalSales(menudict, orders):
    grand_total = 0

    for cId, customer_orders in orders.items():
        
        for oName, order_info in customer_orders.items():
            oCount = order_info['oCount']