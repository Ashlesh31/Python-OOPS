class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        print(f'the brand name is {self.brand} and the model is {self.model} of the year {self.year}')
        print('car starts')
    def stop(self):
        print('car stopped')
mrt = Car('suzuki', 'celerioX', 2018)
mrt.start()
mrt.stop()