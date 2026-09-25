class Vehicle:
    def start(self):
        print('Vechiles start')

class Car(Vehicle):
    def start(self):
        print('Car starts with keys')

class Bike(Vehicle):
    def start(self):
        print('Bike starts with kick')
v1 = Vehicle()
c1 = Car()
b1 = Bike()

v1.start()
c1.start()

v1.start()
b1.start()