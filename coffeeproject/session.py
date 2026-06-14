loginedcustomer = ''
loginedboss = ''

def setloginedcustomer(cId):
    global loginedcustomer
    loginedcustomer = cId

def getloginedcustomer(): 
    global loginedcustomer  
    return loginedcustomer

def setloginedboss(bId):
    global loginedboss
    loginedboss = bId  

def getloginedboss():
    global loginedboss
    return loginedboss