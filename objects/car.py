class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return ("This is a %d %s %s" %(self.year, self.make, self.model))