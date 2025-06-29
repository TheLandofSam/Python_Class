import random

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
        if enemy.health < 0:
            enemy.health = 0
        print(f'{damage}  💢  {enemy.name} has {enemy.health} health remaining')

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


ninja_cat = Hero('NinjaCat', 100, 20, 2, 'copper signet ring')
#ninja_cat.display_status()

class Monster(Character):
    def __init__(self, name, health, attack_power, gold, objects = ['']):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.gold = gold
        super().__init__(name, health, attack_power, gold, objects)

    def print_details(self):
        print(f'\n*** *** {self.name} *** ***')
        print(f'Current health: ?')
        print(f'Attack power: {self.attack_power}')
        print(f'Current gold is: ?')
        print(f'Inventory: ?')
        print('*** *** *** *** *** *** *** ***')

    def taunt(self):
        (f"\n{self.name} snarls: 'You dare to challenge me, weakling?!'")

    def mutter(self):
        (f"\n{self.name} mutters '...mmm, tasty...'")

    def rudeness(self):
        (f"\n{self.name} rudely yells 'you dumb Karen, get out of my dungeon before I end you!'")

giant_spider = Monster(name = 'Giant Spider', health = 45, attack_power = 25, gold = random.randint(1, 6), objects = random.choice(['obsideon pendant', 'emerald and gold cloak pin', 'ruby pinky ring']))

goblin = Monster(name = 'Goblin', health = 25, attack_power = 10, gold = 2, objects = 'a dead frog')

orc = Monster(name = 'Orc', health = 35, attack_power = 13, gold = 4, objects = 'glowing amber amulet')

brownie = Monster(name = 'Brownie', health = 10, attack_power = 3, gold = random.randint(0, 8), objects = random.choice(['a note that reads "pick up fresh bread"', 'a note that reads "the password is strawberry-rhubarb-chocolate-piecakie"', 'a hand drawn map of the northwest corner of the lower level of this dungeon', 'a recipe for veal parmigiana']))

troll = Monster(name = 'Troll', health = 40, attack_power = 16, gold = 8, objects = random.choice(['very dirty rag, rotting apple with a bite missing, silver charm bracelet featuring dainty dangling roses']))

snake = Monster(name = 'Giant Poisonous Snake', health = 25, attack_power = 12, gold = 0, objects = 'a vial of snake venom')

doom = Monster(name = 'large Blue Dragon', health = 190, attack_power = 40, gold = 9647, objects = random.choice(['Arkenstone', 'bloody mangled helmet', 'Ruby', 'Saphire', 'Diamond']))

monster = random.choice([giant_spider, goblin, orc, brownie, troll, snake, doom]) # list for random

def dungeon_room(hero): # repeatable monster attack, battle is in dungeon, dungeon is in play
    monster = random.choice([giant_spider, goblin, orc, brownie, troll, snake, doom])
    print(f'\nYou enter another room in the dungeon. There is enough light to see you are not alone.')
    hero.display_status()
    print(f'\nA {monster.name} is headed in your direction...')
    monster.print_details()
    battle(hero, monster)
    
def giant_spider_start(hero):
    print(f'\nYou enter a dark room in the dungeon!! You have a torch, but it only lights the space 2 feet around you. You see nothing special. But, you have been seen!')
    hero.display_status()
    giant_spider.print_details()
    battle(hero, giant_spider)
     
def battle(hero, monster): # fight logic for dungeon room
    print('The battle begins...')

    while hero.is_alive() and monster.is_alive():

        hero.attack(monster)

        if monster.is_alive():
            monster.attack(hero)

        if not hero.is_alive():
            break

        elif not monster.is_alive():
            hero.gold += monster.gold
            hero.objects.append(monster.objects)
            print('The monster is dead.')

        else:
            choice = input('1️⃣ Continue the fight for riches, 2️⃣ Run for your life: ')

            if choice == '2':
                break      

def play():
    hero = ninja_cat
    print(f'\nWelcome to the Dry Rock Dungeon {ninja_cat.name}, may your future be full of gold and treasure.')
    #start with spider fx, then call dungeon room
    giant_spider_start(hero)
    
    while hero.is_alive():
        choice = input('Continue your dungeon crawl? y or n ... ')
        
        if choice == 'n':
            print(f'\nHopefully you will return someday, but for now NinjaCat is headed home for a catnap. You end your battle for riches and fame with {hero.gold} gold, and backpack filled with: {hero.inventory}.')
            break
        else:
            dungeon_room(hero)
    
        if not hero.is_alive():
            print('\nYour lifeless body falls to the dungeon floor. So ends the story of NinjaCat. Rest in peace knowing some monster of the darkness will soon feed upon your flesh, use your skull for a soup bowl, and make your gold and treasure, their gold and treasure.')


'''
# would be nice to add: 
# more loot items
# useable potions
# ability to use the loot that is collected to augment health or strength or give a defense bonus
# ability to drop items
# max carry weight
# special narrative for doom
# need to re-write and add taunts for the Brownies, but I would like to add a random annoyance handicap to the hero for the taunts

'''
play()