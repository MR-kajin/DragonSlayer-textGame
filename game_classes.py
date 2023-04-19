import random
from termcolor import colored


# Defining the main class for players
class Pg_class:

    hp = 0
    items = []
    status = ""
    poison_dmg = 0
    initial_hp = 0
    def __init__(self, enemy):
        self.status = "healthy"
        self.poison_dmg = 0
        self.turns_poison = 0
        self.magic_user = False

    # Item function contaning the event for the use of each item by the player

    def item_use(self, item):
        if item in self.items:
            if item == "Unstable Potion":
                luck = random.randint(1, 100)
                if luck < 20:
                    poison_dmg = random.randint(10, 18)
                    self.status = "poisoned"
                    self.hp -= poison_dmg
                    self.poison_dmg += poison_dmg
                    self.turns_poison += 4
                    self.items.remove(item)
                    print(colored(f"\n{self.username}: poisoned! -{poison_dmg} HP\n", 'green'))
                else:
                    hp_healed = random.randint(50, 100)
                    if self.hp + hp_healed >=  self.initial_hp:
                        hp_healed = self.initial_hp - self.hp
                        self.hp = self.initial_hp
                    else:
                        self.hp += hp_healed
                    print(colored(f"\n{self.username}: healed of {hp_healed} HP\n",'green'))
                    self.items.remove(item)

            elif item == "Cure Potion":
                hp_healed = random.randint(30, 50)
                if self.hp + hp_healed >=  self.initial_hp:
                    hp_healed = self.initial_hp - self.hp
                    self.hp = self.initial_hp
                else:
                    self.hp += hp_healed
                self.items.remove(item)
                print(colored(f"\nYou are healed of {hp_healed} HP\n", 'green'))

            elif item == "Dragonlance":
                if self.magic_user == True:
                    print(colored("\nSorry you are not strong enough to use it\n", 'green'))
                else:
                    print("\nYou can use it to pierce your enemy\n")

            elif item == "Shining Gem":
                if self.magic_user == True:
                    print(colored("\nYou can use it to cast powerful spells\n",'green'))
                else:
                    print(colored("\nIt is a really beatiful gem pulsing of magical energy, but you don't know how to use it\n", 'green'))

            elif item == "Herbs":
                if self.status == "poisoned":
                    hp_herbs = int(self.poison_dmg / 2)
                    self.hp += hp_herbs
                    self.status = "healthy"
                    print(colored(f"\n{self.username}: Poison cured! + {hp_herbs} HP\n", 'green'))
                    self.items.remove(item)
                    self.turns_poison = 0
                else:
                    print(colored("\nExcept the bitter taste, you don't feel any effect\n", 'green'))
                    self.items.remove(item)
            elif item == "Shield":
                self.shield = True
        else:
            print(colored("\nItem not available\n", 'green'))
    def check_hp(self):
        return self.hp

# First subclass that can be choosen by the player and contain all the function/action that the player can do and its status

class Knight(Pg_class):
    initial_hp = 250
    def __init__(self,enemy, name="User"):
        self.username = name
        self.hp = 250
        self.items = ["Shield", "Cure Potion","Cure Potion","Cure Potion","Cure Potion", "Herbs","Herbs"]
        self.shield = False
        self.turns_poison = 0
        self.magic_user = False
        self.attacks = {"Sword Slash": "sword_slash" , "Shield" : "iron_shield", "Spear Pierce" : "spear_pierce"}
    def sword_slash(self,enemy):
        dmg = random.randint(14, 20)
        accuracy = random.randint(1, 100)
        if accuracy < 10:
            dmg = 0
            print(colored(f"\n{self.username}: Miss!\n", 'blue'))
        elif accuracy > 95:
            dmg *= 3
            print(colored(f"\n{self.username}: Lethal blow! {dmg} damage\n",'blue'))
        elif accuracy > 85:
            dmg *= 2
            print(colored(f"\n{self.username}: Critical hit! {dmg} damage\n",'blue'))
        else:
            print(colored(f"\n{self.username}: Hit! {dmg} damage\n",'blue'))
        enemy.hp -= dmg

    def iron_shield(self, enemy):
        self.shield = True
        print(colored(f"\n{self.username}: Shield: ON\n", 'blue'))

    def spear_pierce(self, enemy):
        if "Dragonlance" in self.items:
            dmg = random.randint(60, 90)
            accuracy = random.randint(1, 100)
            if accuracy < 10:
                dmg = 0
                print(colored(f"\n{self.username}: Miss!\n", 'blue'))
            elif accuracy > 85:
                dmg *= 2
                print(colored(f"\n{self.username}: Critical hit! {dmg} damage\n",'blue'))
            else:
                print(f"\n{self.username}: {dmg} damage\n")
            enemy.hp -= dmg
            self.items.remove("Dragonlance")
        else:
            print(colored("\nYou don't have a lance\n", 'green'))

 # Second subclass that can be choosen by the player and contain all the function/action that the player can do and the status

class Wizard(Pg_class):
    initial_hp = 160
    def __init__(self, enemy, name="User"):
        self.username = name
        self.hp = 160
        self.items = ["Cure Potion", "Herbs","Herbs"]
        self.shield = False
        self.turns_poison = 0
        self.attacks = {"Magic Dart" : "magic_dart", "Magic Shield" : "magic_shield","Healing": "healing_spell", "Fire Ball": "fire_ball"}
        self.magic_user = True
        self.n_healing = 4


    def magic_dart(self, enemy):
        dmg = random.randint(19, 26)
        accuracy = random.randint(1, 100)
        if accuracy < 10:
            dmg = 0
            print(colored(f"\n{self.username}: Miss!\n", 'blue'))
        elif accuracy > 95:
            dmg *= 3
            print(colored(f"\n{self.username}: Lethal blow! {dmg} damage\n",'blue'))
        elif accuracy > 85:
            dmg *= 2
            print(colored(f"\n{self.username}: Critical hit! {dmg} damage\n",'blue'))
        else:
            print(colored(f"\n{self.username}: Hit! {dmg} damage\n",'blue'))
        enemy.hp -= dmg        # funzione per sottrazione hp drago

    def magic_shield(self, enemy):
        self.shield = True
        print(colored(f"\n{self.username}: Magic Shield: ON\n", 'blue'))

    def healing_spell(self, enemy):
        if self.n_healing > 0:
            hp_healed = random.randint(45, 60)
            if self.hp + hp_healed >=  160:
                hp_healed = 160 - self.hp
                self.hp = 160
            else:
                self.hp += hp_healed
            self.n_healing -= 1
            print(colored(f"\n{self.username}: Healed of {hp_healed} HP, {self.n_healing} healing spells left\n", 'blue'))

        else:
            print(colored("\nYou don't have any healing spell left\n",'green'))


    def fire_ball(self, enemy):
        if "Shining Gem" in self.items:
            dmg = random.randint(40, 80)
            accuracy = random.randint(1, 100)
            if accuracy < 10:
                dmg = 0
                print(colored(f"\n{self.username}: Fireball Miss!\n", 'blue'))
            elif accuracy > 85:
                dmg *= 2
                print(colored(f"\n{self.username}: Fireball Critic hit! {dmg} damage\n"),'blue')
            else:
                print(colored(f"\n{self.username}: Fireball Hit! {dmg} damage\n",'blue'))
            enemy.hp -= dmg
            self.items.remove("Shining Gem")
        else:
            print(colored("\nYou don't have the necessary ingredient to lunch this magic spell\n", 'green'))

# Class of the enemy, defining its attacks and health point

class Dragon():
    hp = 0
    status = ""
    poison_dmg = 0
    def __init__(self):
        self.hp = 400
        self.power_attack = False
    def bite(self, enemy):
        dmg = random.randint(12, 18)
        if enemy.shield == True:
            dmg = int(dmg / 2)
        accuracy = random.randint(1, 100)
        if accuracy < 10:
            dmg = 0
            print(colored("\nDragon: Miss!\n",'magenta'))
        elif accuracy > 95:
            dmg *= 3
            print(colored(f"\nDragon: Lethal blow! {dmg} damage\n", 'magenta'))
        elif accuracy > 85:
            dmg *= 2
            print(colored(f"\nDragon: Critic hit! {dmg} damage\n", 'magenta'))
        else:
            print(colored(f"\nDragon: Hit! {dmg} damage\n", 'magenta'))
        enemy.hp -= dmg

    def breath(self, enemy):
        dmg = random.randint(25, 50)
        if enemy.shield == False:
            print(colored ("\nThe Dragon blast his lethal acid breath!\n", 'magenta'))
        else:
            dmg = int(dmg / 2)
            print(colored("\nThe Dragon blast his lethal acid breath but you hide behind your shield limiting the damages!\n", 'magenta'))
        accuracy = random.randint(1, 100)

        if accuracy < 5:
            dmg = 0
            print(colored("\nDragon Miss!\n", 'magenta'))
        elif accuracy > 85:
            dmg *= 2
            print(colored(f"\nDragon Critic hit! {dmg} damage\n",  'magenta'))
        else:
            print(colored(f"\nDragon hit! {dmg} damage\n",  'magenta'))
        enemy.hp -= dmg    
        poisoning_chance = random.randint(1, 100)
        if dmg != 0 and poisoning_chance > 70:
            enemy.status = "poisoned"
            enemy.turns_poison += 6
            print(colored(f"\n{enemy.username} have been poisoned!\n",  'magenta'))