def registerC(cars):

    carNum = input('차량번호를 입력하세요.')
    uName = input('고객성함을 입력하세요.')
    isParking = input('주차 여부를 입력하세요.(Y/N)')

    carlist = {
        'carNum':carNum,
        'uName':uName,
        'iscar':isParking
    }

    carlist[carNum] = cars

    return cars