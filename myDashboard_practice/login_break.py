import session

def commition():
    if session.getSigninedMemberId() == '':
        print('Please SIGN-IN!!')
        return