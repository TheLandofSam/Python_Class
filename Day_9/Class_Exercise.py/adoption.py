from pets import Pet

class PetAdmoptionSystem:
    def __init__(self):
        self.available_pets: list[Pet] = []

    def add_pet(self, pet):
        self.available_pets.append(pet)

    def adopt_pet(self, pet_name: str):
        for pet in self.available_pets:
            if pet_name.lower() = pet.name.lower()
            print(f'{pet_name} has been adopted')
            self.available_pets.remove(pet)
            return pet

    def pet_behavior_generator(self):
        # Generator that yieldds pet behavior dynamically
        for pet in self.available_pets:
            yield pet.name, pet.behavior()

    def show_available_pets(self):
        print(' *** Pets available ***')
        for pet in self.available_pets:
            pet.show_details()
        print(' *** *** *** ')

        
