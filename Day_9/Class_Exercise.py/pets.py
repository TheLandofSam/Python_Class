from abc import ABC, abstractmethod
import datetime

#Base Class
class Pet(ABC):
    def __init__(self, name, breed, age, found_date = 0): 
        self.name = name
        self.breed = breed
        self.age = age
        self.found_date = found_date

    def show_details(self):
        print (f'{self.name} the {self.breed}, Age: {self.age}, Time in Shelter {(datetime.datetime.today() - self.found_date).days}')

    @abstractmethod # when you have an abstract class you cannot create your objects from that class, you need to make sub classes and use those
    def behavior(self):
        'Each pet has a unique behavior'
        pass

#bruno = Pet('Bruno, 'Aussie', 1, 2024)

bruno.show_detials()

#Sub classes

class Dog(Pet):
    def __init__(self, name, breed, age, found_date = 0, is_smart):
        super().__init__(name, breed, age, found_date)
        self.is_smart = is_smart

    def behavior(self): # must be the same as the base class since it inherets ie behavior
        if self.is_smart:
            return 'It is good with commands and loves to fetch'
        else:
            return 'Agressive, and barks at the mail man'

class Cat(Pet):
    def __init__(self, name, breed, age, found_date, is_trait)
        super().__init__(name, breedm age, found)
        self.is_trait = is_trait

    def behavior(self)
        if self.is_trait:
            return 'This cat has special traits!'
        return 'This cat is boring.' # else not needed because return command is terminal

#class Rabbit(Pet):
 #   def 

strider = Cat('Strider', 'Tuxie', 8, datetime.datetime(2017, 8, 15), True)
strider.show_details()
print(strider.behavior()) 


