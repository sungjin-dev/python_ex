import session

def delete(customerdict):
      
    if session.getloginedcustomer()=='':
        print('로그인부터 해주세요.')
        return
    
    cId = session.getloginedcustomer()

    if cId in customerdict:
        del customerdict[cId] 

    return customerdict  
   




