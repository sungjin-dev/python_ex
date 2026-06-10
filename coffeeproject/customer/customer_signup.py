import session

def signUp(customerdict):

    if session.getloginedcustomer() != '':
        print('이미 로그인되어있습니다.')
        return
    
    cId = input('ID를 입력하세요.')

    if cId in customerdict:
        print('이미 존재하는 ID입니다.')
        return
    
    cPw = input('PW를 입력하세요.')
    # cTier = input('등급을 입력하세요.') # 이건 외부에서 만들어서 해보기 
    cPhone = input('PHONE를 입력하세요.')

    customers = {
        'cId':cId,
        'cPw':cPw,
        # 'cTier':cTier,
        'cPhone':cPhone,
    }
   
    customerdict[cId] = customers

    session.getloginedcustomer(cId)

    return customerdict

    