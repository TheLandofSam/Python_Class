from pets import *
from adoption import PetAdoptionSystem
from datetime import datetime

adoption_syustem = PetAdoptionSystem()

#Adding pets to the system (adding objects)

bruno = Dog('bruno', 'Aussie', 1, datetime(2024, 4, 15), True)
#adding pets to system
adoption_system.add_pet(bruno)
adoption_system.add_pet(strider)
adoption_system.show_available_pets()
#removing pets from the system
adoption_system.adopt_pet('bruno')
adoption_system.show_available_pets()
#access to the yield object
pet_behavior = adoption_system.pet_behavior_generator()

print(next(pet_behaviors))

#for pet in pet behaviors:
 #   print(f'')

#for name, behavior in pet_behaviors:
 #   print(f'{name'}, behaves like: (behavior). )