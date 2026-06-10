import session

def modify(customerdict):

    if session.getloginedcustomer()=='':
        print('로그인부터 해주세요.')
        return
    
    cId =  session.getloginedcustomer()

    if cId not in customerdict:
        pass

        cPw = input('변경하고 싶은 PW를 입력하세요.')
        cPhone = input('변경하고 싶은 PHONE를 입력하세요.')

        customerdict[cId]['cPw'] = cPw
        customerdict[cId]['cPhone'] = cPhone
   
        return customerdict