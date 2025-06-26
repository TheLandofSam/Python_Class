class Character:
    
    
    def __init__(self, name, health, attack_power, gold, objects = ['']):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.gold = gold
        self.objects = objects

    def attack(self, enemy: 'Character'):
        print(f'\n{self.name} attacks 💥 {enemy.name}')
        damage = self.attack_power
        enemy.health -= damage
        print(f'{damage}  💢  {enemy.name} has {enemy.health} remaining')

    def is_alive(self):
        return self.health > 0

    def display_status(self):
        print(f'\n*** *** {self.name} *** ***')
        print(f'Current health: {self.health}')
        print(f'Attack power: {self.attack_power}')
        print(f'Current gold is {self.gold}')
        print(f'Inventory: {', '.join(self.objects)}') if self.objects else ''
        print('*** *** *** *** *** *** *** ***')

class Hero(Character):

    def __init__(self, name, health, attack_power, gold, hero_inventory = ['']):
        inventory = ['torch', 'sword']
        inventory.append(hero_inventory) if hero_inventory else ''
        super().__init__(name, health, attack_power, gold, inventory)


ninja_cat = Hero('NinjaCat', 50, 20, 2, 'copper insignit ring')
ninja_cat.display_status()

class Monster(Character):
    def __init__(self, objects = ['']):
        super().__init__(name, health, attack_power, gold, objects)   

    def taunt(self):
        (f"\n{self.name} snarls: 'You dare to challenge me, weakling?!'")

    def mutter(self):
        (f"\n{self.name} mutters '...mmm, tasty...'")

    def rudeness(self):
        (f"\n{self.name} rudely yells 'you dumb Karen, get out of my dungeon before I end you!'")

giant_spider = Monster(name = 'Giant Spider', health = 65, attack_power = 34, gold = 5, objects = ['obsideon pendant'])

goblin = Monster(name = 'Goblin', health = 25, attack_power = 13, gold = 2)

orc = Monster(name = 'Orc', health = 35, attack_power = 18, gold = 4, objects = ['glowing amber amulet'])

brownie = Monster(name = 'Brownie', health = 10, attack_power = 6, gold = random.randint(0, 8), objects = random.choice(['a note that reads "pick up fresh bread"', 'a note that reads "the password is strawberry-rhubarb-chocolate-piecakie"', 'a hand drawn map of the northwest corner of the lower level of this dungeon', 'a recipe for veal parmigiana']))

troll = Monster(name = 'Troll', health = 50, attack_power = 25, gold = 8, objects = ['very dirty rag, rotting apple with a bite missing, silver charm bracelet featuring dainty dangling roses'])

# * def dungeon_room(Hero: Character, Monster: Character): # repeatable monster attack, battle is in dungeon, dungeon is in play


# * monster = [giant_spider] # finish list for random

    
def giant_spider_start():
    print(f'\nYou enter a dark room in the dungeon!! You have a torch, but it only lights the space 2 feet around you. You see nothing special. But, you have been seen!')
    ninja_cat.display_status()
    giant_spider.print_details()
    battle(ninja_cat, giant_spider)
    
def battle(hero: Character, monster: Character): # fight logic for dungeon room
    print('The battle begins...')

    while hero.is_alive() and monster.is_alive():
        ninja_cat.display_status()
        giant_spider.display_status()

        ninja_cat.attck

def play():
    #start wit spider fx, then call dungeon room
    giant_spider_start()
    #loop with dungeon, battle, and monsters in a list for random call

    # need to finish
