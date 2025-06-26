# hides did data, need to use (__private_variable) for it
# can only be used inside the class not outside of the class
# the data appears hidden, when executed it gives and error and says there is no attribute that mataches

class Dog:
    def __init__(self, name, age, owner_phone):
        self.__name = name
        self.__age = age
        self.__owner_phone = owner_phone
# getters and setters allow you to get encapsulated info outside of the class
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
        else:
            print('Name cannot be empty!')

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age:
            self.__age = new_age
        else:
            print('Age cannot be empty!')

    @property
    def name (self): #"Gets name, @property it is using for the getters" ; can put only a getter, but not just a setter alone
        return self.__name

    @name.setter
    def name(self, new_name): # @name.setter
        if new_name:
            self.__name = new_name
        else:
            print('Name cannot be empty!')

    #creating objects

dog = Dog('bruno', 1, 2023)
#print(dog.age)
#print(dog.__owner_phone) #encapulated, will give error, data cannot be seen when run
print(dog.get_name())
#dog.set_name('Sparkle_Butt')
#print(dog.get_name())                                             

'''
decodators
@property
def name (self):
        return self.__age

@name.setter
'''

print(dog.name) # way to call getter, like an attribute not like a method
dog.name = 'Sparkle_Butt' # way to set a setter, like attribute, not like a method
print(dog.name)

# Abstract Methods
'''abstract classes define a structure that subclasses must follow

dog is abstract it cannot be used directly

labrador and beagle must implement make_sound().
'''

from abc import ABC, abstractmethod

class Dog(ABC): #called base class because we are using abstract methods
    def __init__(self, name, age, owner_phone):
        self.__name = name
        self.__age = age
        self.__owner_phone = owner_phone

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
        else:
            print('Name cannot be empty!')

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age:
            self.__age = new_age
        else:
            print('Age cannot be empty!')

    @abstractmethod
    def makes_sound(self):
        pass

    def perform_trick(self):
        pass

# Sub Classes

class Aussie(Dog):
    def makes_sound(self):
        print('Woof, woof!')

    def peerform_trick(self):
        print('Fetch ball')
        print('Understand 10 commands')

bruno = Aussie('bruno', 3)
print(bruno.print_details())

class Schnauzer(Dog):
    def makes_sound(self):
        print('Bark bark')

    def perform_trick(self):
        print('roll over')
        print('speaks spanish')

    

