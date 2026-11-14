# Deanna Hardin
# File: Module3_Vehicle.py
# Description:
# This program uses inheritance to collect & display information about an automobile.

# Variables:
# vehicle_type - Stores the vehicle type.
# year - Stores the vehicle year.
# make - Stores the manufacturer.
# model - Stores the vehicle model.
# doors - Stores the number of doors.
# roof - Stores the roof type.
# car - Stores the Automobile object.

# Superclass for storing the vehicle type.
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass that inherits from Vehicle.
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


year = input("Enter the year: ")
make = input("Enter the make: ")
model = input ("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the roof type (solid or sunroof): ")

car = Automobile(year, make, model, doors, roof)


print(f"Vehicle type: {car.vehicle_type}")
print(f"Year: {car.year}")
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Number of doors: {car.doors}")
print(f"Type of roof: {car.roof}")



