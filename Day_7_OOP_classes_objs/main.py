'''
Basics of OOP starts today, lots of concepts in the codeworks syllubus

OOP makes code eaiser to use
it is an object, has data structure, has its own attributes and values

Bruno is dog and can be an object. He has attributes like name, age, color

Bruno:
    name = Bruno

    age = 1

    color = brown

Perla:

    name = Perla

    age = 14

    color = white

class is a blueprint for creating objects, reusable, start class name with capital (Dog, not dog)
classes share the same attributes and same methods, when you call them you pass in the individule values, like name, age, etc

best practice self is always the first parameter in the fx
best practice to use self.name instead of self.n


'''
class Dog:
    def __init__(self, name, age, color): # the first fx is going to add...
        self.name = name
        self.age = age
        self.color = color

    def print_details(self):
        print(f'Hi, I am {self.name}, I am{self.age} years old, and I have cool {self.color} color')

# creating objects

bruno = Dog('Bruno', 1, 'brown')
perla = Dog('Perla', 14, 'white')
cherry = Dog ('Cherry', 1, 'black-brown')

print(bruno.name)

# Building the game --- Parent class; gender = '' is initializing the gender, and when initilizing must be at the end
class Character:
    def __init__(self, name, health, attack_power, gender= ''):
        self.name = name
        self.health = health
        self.gender = gender
        self.attack_power = attack_power

    def attack(self, enemy: 'Character'): #quotes because it is inside of Character and we are saying it inherets from itself, own class from inside class
        print(f'{self.name} attacks')
        damage = self.attack_power
        enemy.health -= damage
        print(f'{damage} >< {enemy.health}')

    def is_alive(self):
        return self.health > 0

    def print_details(self): #methods
        print(f'\n*** {self.name}***')
        print(f'\n*** {self.health}***')
        print(f'\n*** {self.gender}***') if self.gender else ''
        print(f'\n*** {self.attack_power}***')
        print('*************************************')

# Creating Character objects --- child class

slate = Character('slate', 80, 20, 'male')
kim = Character('Kim', 80, 26, 'female')
slate.print_details()
kim.print_details()

# Monster class inherits from Character class thus why it is in parenthesis
# you don't have to use all of what character has, maybe no gender on goblins
class Monster(Character):
    def __init__(self):
        name = 'Goblin'
        health = 40
        attack_power = 12
        super()._init_(name, health, attack_power)
        # super is required, connects class, it tells the class that it is inheriting from what it is inheriting, this way you can use the methods of Character

    #Monster objects

    monster = Monster()
    monster.print_details

    def dungeon_room(adventurer: Character): 
        print(f'\n You enter a dark room in the dungeon!!')
        adventurer.print_details()
        monster = Monster() # create a monster by calling a monster class
        print('A monster appears!!')
        monster.print_details
    
    adventurer = Character('slate', 80, 20, 'male')
    monster = Monster()
    adventurer.attack(monster)

dungeon_room()    # see Paula's notes, I got lost and decided to just listen

## following is Paula's code:

class Character:
    def __init__(self, name, health, attack_power, gold, gender = ''):
        self.name = name
        self.health = health
        self.gender = gender
        self.gold = gold
        self.attack_power = attack_power
    
    def attack(self, enemy: 'Character'):
        print(f'{self.name} attacks🤺 to {enemy.name}')
        damage = self.attack_power
        enemy.health -= damage
        print(f'{damage} 💢 {enemy.health}')
    
    def is_alive(self):
        return self.health > 0
    
    def print_details(self):
        print(f'\n*** {self.name} *************')
        print(f'health: {self.health}')
        print(f'💰 {self.gold}')
        print(f'gender: {self.gender}') if self.gender else ''
        print(f'Attack power: {self.attack_power}')
        print('************************')
        
# Creating character objects --- child class

# slate = Character('slate', 80, 'male', 20)
# kim = Character('Kim', 80, 'female', 26)
# slate.print_details()
# kim.print_details()

# Monster class --- child class tha Inheritance from Character class
class Monster(Character):
    def __init__(self):
        name = random.choice(['Goblin', 'orc', 'troll'])
        health = random.randint(5, 80)
        attack_power = random.randint(5, 15)
        gold = random.randint(0, 25)
        super().__init__(name, health, attack_power, gold) # Passing attributes to the parent class (Character)

# Monster objects

# monster = Monster()
# monster.print_details()

def dungeon_room(adventurer: Character):
    print(f'\nYou enter a dark room in the dungeon!! 🕷🕸🕷')
    adventurer.print_details()
    monster = Monster()
    print('A monster appears!! 👺')
    monster.print_details()
    battle(adventurer, monster)

# adventurer = Character('slate', 40, 30, 'female')
# monster = Monster()
# monster.print_details()
# adventurer.attack(monster)
# monster.print_details()
#dungeon_room(adventurer)

def battle(adventurer: Character, monster: Monster):
    
    while adventurer.is_alive() and monster.is_alive():
        adventurer.attack(monster)
        monster.attack(adventurer)

        choice = input('Keep 1️⃣ Figthing, 2️⃣ run: ')

        if choice == '2':
            break

    if not monster.is_alive():
        adventurer.gold += monster.gold

    adventurer.print_details()

def play_game():
    print("\nWelcome to the Dungeon Adventure")
    name = input("Enter your Adventurer's name: ")
    gender = input('What it is the gender')
    adventurer = Character(name, 30, 20, 2, gender)
    dungeon_room(adventurer)
    while adventurer.is_alive():
        choice = input('Continue exploring> [y,n]')
        if choice == 'n':
            print('Good bye quitter!! 😑')
            break
        else:
            dungeon_room(adventurer)
    
    if adventurer.is_alive():
        print(f' You flee the dungeon with this amount of money {adventurer.gold}')
    else:
        print('You die sorry 😭')

play_game()
