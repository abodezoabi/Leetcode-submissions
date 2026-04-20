class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkingsystem = [big,medium,small]
  

    def addCar(self, carType: int) -> bool:
        if self.parkingsystem[carType-1] <= 0:
            return False
        elif self.parkingsystem[carType-1] > 0:
            self.parkingsystem[carType-1] -= 1
            return True 


        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)