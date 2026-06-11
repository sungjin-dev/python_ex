def isCar(cars):

    print(f'현재 주차 현황: {cars}')

    if "Y" not in cars[isCar]:
        print('주차된 차량이 없습니다.')
        return cars
    
    print(f'주차 LIST: {cars}')
    
    selectedCar = input('변경할 차량을 선택하세요.') 

    if selectedCar not in cars:
        print('오타거나 없는 차량입니다.')
        return cars
    else: 
        isCar = input('주차 여부를 갱신하세요.(Y/N)')

        cars[selectedCar]['isCar'] = isCar

        return cars
