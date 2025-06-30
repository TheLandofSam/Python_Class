from animal import ^
from adoption import Zoo
from datetime import datetime

def main():

    zoo = Zoo()

    leo = Lion('Leo', 'Lion', 08162020, 'Rarrrr', 'yes')
    curious = Monkey('Curious George', 'Monkey', 04202021, 'Eee...eee...eee', 'playful')
    hedwig = Owl('Hedwig', 'Owl', 10102010, 'hooo hooo hooo', 'watchful')

    zoo.add_animal(leo)
    zoo.add_animal(curious)
    zoo.add_animal(hedwig)

    print ('*** *** Sam-Sam Zoo *** ***')

    while True:

        zoo.show_zoo_animals()

        print('1️⃣ Release an animal')
        print('2️⃣ See the animal\'s characteristics')
        print('3️⃣ Exit')

        choice = int(input('What would you like to do? '))

        if choice == 1:
            animal_name = input('What animal would you like to release? ')
            zoo.release_animal(animal_name)
        elif choice == 2:
            animial_char = zoo.animal_characteristic_generator()
            for name, characteristic in animal_char:
                print(f'{name} has the characteristic of being {characteristic}.')
        elif choice == 3:
            break

    print('Good bye')

    main()
