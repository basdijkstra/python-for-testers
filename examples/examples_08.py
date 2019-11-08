class Car:
    def __init__(self, make, model, year):
        if make == "Ducati":
            raise ValueError("Ducati does not make cars!")
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return "This is a %d %s %s" %(self.year, self.make, self.model)


try:
    my_car = Car("Ducati", "Monster", 2019)
except ValueError:
    print("That was a close call!")

my_other_car = Car("Ducati", "Monster", 2019)
