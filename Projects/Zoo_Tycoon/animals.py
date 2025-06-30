from abc import ABC, abstractmethod
import datetime
##from playsound import playsound

#base class
class Animal(ABC):
    def __init__(self, name, species, dob):
        self.name = name
        self.species = species
        self.dob = dob

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def characteristic(self):
        pass

    def show_details(self):
        print(f'{self.name}, {self.species}, {self.dob}')

# sub-classes

class Lion(Animal):
    def __init__(self, name, species, dob, sound, characteristic):
        super().__init__(name, speecies, dob)
        self.sound = sound
        self.characteristic = characteristic

    def sound(self):
        print(f'{self.sound}')

    def characteristic(self):
        if self.characteristic == 'yes':
            return 'Lions are the ones who never look back on barking dogs.'
        else:
            return 'Meow.'

class Monkey(Animal):
    def __init__(self, name, species, dob, sound, characteristic):
        super().__init__(name, speecies, dob)
        self.sound = sound
        self.characteristic = characteristic

    def sound(self):
        print(f'{self.sound}')

    def behavior(self):
        if self.characteristic == 'playful':
            return 'playful'
        else:
            return 'rude'

class Owl(Animal):
    def __init__(self, name, species, dob, sound, characteristic):
        super().__init__(name, speecies, dob)
        self.sound = sound
        self.behavior = behavior

    def sound(self):
        print(f'{self.sound}')

    def characteristic(self):
        if self.characteristic == 'watchful':
            return 'watchful'
        else:
            return 'Not a real owl.'

leo = Lion('Leo', 'Lion', 08162020, 'Rarrrr', 'yes')
print(leo)
print(leo.sound())

curious = Monkey('Curious George', 'Monkey', 04202021, 'Eee...eee...eee', 'playful')
print(curious)
print(curious.sound())

hedwig = Owl('Hedwig', 'Owl', 10102010, 'hooo hooo hooo', 'watchful')
print(hedwig)
print(hedwig.sound())