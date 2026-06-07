def modify(memberdict):

    flag = True
    while flag:
        mId = input('변경하고 싶은 ID를 입력하세요.')
        mPw = input('변경하고 싶은 PW를 입력하세요.')
        mEmail = input('변경하고 싶은 EMAIL를 입력하세요.')
        mPhone = input('변경하고 싶은 PHONENUMBER를 입력하세요.')

        if mId in memberdict:
            print('이미 존재하는 ID입니다.')
            return
        else:
            memberdict['mId'] = mId   
            memberdict[mId]['mPw'] = mPw
            memberdict[mId]['mEmail'] = mEmail
            memberdict[mId]['mPhone'] = mPhone
            break

    return memberdict    