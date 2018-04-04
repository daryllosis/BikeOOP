'''
Author: Daryll osis
Date: April 04, 2018
Description: It's a simple program that uses Class. it's an introduction to class.
'''

class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print("Price of this bike is $", self.price, sep='')
        print("Maximum speed of this bike is ", self.max_speed, "mph", sep='')
        print("Total miles of this bike is", self.miles, "miles")
    def ride(self):
        print("Riding....")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing....")
        self.miles -= 5
        return self


bike1 = Bike(25, 30, 0)
bike1.displayInfo()
bike1.ride()
bike1.displayInfo()
bike1.reverse()
bike1.displayInfo()
