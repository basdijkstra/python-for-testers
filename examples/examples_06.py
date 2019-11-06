class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("This is a %d %s %s" %(self.year, self.make, self.model))

my_car = Car("Ford", "Focus", 2019)
my_car.print_info()
