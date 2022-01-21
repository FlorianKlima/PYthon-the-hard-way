class Elevator:
    def __init__(self, starting_floor):
        self.make = 'The Elevator Company'
        self.floor = starting_floor

# The Object:
# The object is the instance of the class.

elevator = Elevator(1)
print(elevator.make)
print(elevator.floor)
