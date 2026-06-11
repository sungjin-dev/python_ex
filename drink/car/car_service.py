from car import car_info
from car import car_register
from car import car_check
import database

class CarService:
    def __init__(self):
        self.filename = "cars.json"
        self.cars = {}

        self.cars = database.save_data(self.filename, self.cars)

    def registerCar(self):
        car_register.registerC(self.cars)
        database.save_data(self.filename, self.cars)

    def parkinginfos(self):
        car_info.parkingCars(self.cars)
        database.save_data(self.filename, self.cars)

    def parkingCheck(self)
        car_check.
        database.save_data(self.filename, self.cars)

    def run(self):
        flag = True

        while flag:
            selectedNum = int(input('1. 차량 등록 2. 차량 조회 3.주차 정보 변경 99. 종료'))

            if selectedNum == 1:
                self.registerCar(self.cars)
            elif selectedNum == 2:
                self.parkinginfos(self.cars)
            elif selectedNum == 3:
                pass
            elif selectedNum == 99:
                flag = False



        
    



