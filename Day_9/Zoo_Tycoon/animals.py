from abc import ABC, abstractmethod
import datetime
##from playsound import playsound

#base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def behavior(self):
        pass

    def __str__(self):
        return f'{self.name} '

# sub-classes

class Lion(Animal):
    def __init__(self, name, behavior):
        super().__init__(name)
        self.behavior = behavior

    def sound(self):
        #playsound(C:\Users\lucky\Python_Class\sound_files)
        print('Rarrrr')

    def behavior(self):
        print('behavior')

leo = Lion('Leo', True)

print(leo)

leo.behavior()

class Monkey(Animal):
    def __init__(self, name, behavior):
        super().__init__(name)
        self.behavior = behavior

    def sound(self):
        #playsound(C:\Users\lucky\Python_Class\sound_files)
        return ('Eee...eee...eee')

    def behavior(self):
        if self.behavior:
            return 'playful'
        return 'rude'

class Owl(Animal):
    def __init__(self, name, behavior):
        super().__init__(name)
        self.behavior = behavior

    def sound(self):
        #playsound(C:\Users\lucky\Python_Class\sound_files)
        return ('hooo hooo hooo')

    def behavior(self):
        if self.behavior:
            return 'watchful'
        return 'Not a real owl'