
class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def release_animal(self, animal_name: str):
        for animal in self.zoo:
            if animal_name.lower() == animal.name.lower()
                print(f'{animal_name} has been released. Good luck {animal_name}!')
                self.zoo.remove(pet)
                return pet

    def animal_characteristic_generator(self):
        for pet in self.zoo:
            yield animal.name, animal.characteristic()

    def show_animals_details(self):
        print('*** *** Zoo Residents *** ***')
        for animal in self.zoo:
            animal.show_details()
        print('*** *** *** *** *** *** *** ***')
