from game_classes import Dragon, Knight, Wizard
import time
import random
import re
import sys
from termcolor import colored
import os

os.system('color')

def main():
    print(colored (f"\nWELCOME TO THE DRAGONSLAYER GAME!\n", 'red'))
    while(True):
        play = input(colored("\nTo start the game type: PLAY otherwise QUIT\n\n", 'green')).title()
        start = st_game(play)
        if start == True:
            break
        else:
            continue
    name = input(colored ("\nFirst of all choose your adventurer name (only letters, max 25 chr and two words)\n\n", 'green'))
    while(True):
        
        allowed_name = check_name(name)
        if allowed_name == True:
            break
        else:
            print("\nOnly letters, max 25 chr and two words are allowed\n")
            name = input()
            continue
    black_dragon = Dragon()
    print(colored ("\nSecond choose your class: Knight or Wizard?\n", 'green'))
    while(True):
        classe = input().title()
        if classe == "Knight" or classe == "Wizard":
            user = class_choise(black_dragon, name, classe)
            break
        else:
            print(colored("\nWrong selection, choose: Knight or Wizard\n",'green'))

    scene1(black_dragon, user)

# Check if input name respect the restriction about length and type of characters allowed

def st_game(play):
    if play == "Play":
        return True
    elif play == "Quit":
        sys.exit("\n")
    else:
        return False

def check_name(name):
        allowed_name = re.search(r"^[a-zA-Z]+\s?[a-zA-Z]+$", name)
        if allowed_name and len(name) <= 25:
            return True
        else:
            return False

# Creation of the instance containing the selected Class

def class_choise(black_dragon, name, classe):

    while (True):
        if classe == "Knight":
            user = Knight(black_dragon,name)
            return user
        elif classe == "Wizard":
            user = Wizard(black_dragon,name)
            return user
        else:
            return False

# First scene of the game with two possible outcome

def scene1(black_dragon, user):
    print(colored("""

Let's start the adventure!

After a long journey through the Vingaard Mountains and the Guardian Swamp you finally arrive in front of the entrance to the Black Dragon Cave.
The stench of death that comes out of the cave makes you turn up your nose and a deep sense of anguish begins to oppress your chest.

""", 'cyan'))
    print(colored ("Type your choice: Enter or Leave?\n", 'green'))
    c1 = input().lower()
    time.sleep(1)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1 == "enter"):
            print(colored ("\nYou begin to descend into the dark cave, courageously overcoming the fear of the dragon", 'cyan'))
            ans = 'correct'
            scene2(black_dragon, user)
        elif(c1 == "leave"):
            print(colored("\nThe fear of the Dragon invades your heart, you turn around and run away deciding to change jobs and start dedicating yourself to less dangerous adventures (although not easier) such as learning to program!", 'cyan'))
            ans='correct'
        else:
            print(colored ("TYPE THE CORRECT CHOICE! Enter or Leave?"), 'green')
            c1 = input().lower()

# Second scene of the game where it's possible pick up an item usuful for the fight, but depends on which class has been selected

def scene2(black_dragon, user):
    print(colored("""

After hours of wandering in the meanders of the cave, you find a corpse of an adventurer on the ground, stuck in a trapdoor.

Looking carefully you notice three interesting objects on the body, a Spear, a Potion and a Gem. You can choose whether to take one or leave.
""", 'cyan'))
    print(colored ("\nType your choice: Spear,  Potion, Gem or Leave?\n", 'green'))
    loot_item = { "spear" : "Dragonlance", "potion" : "Unstable Potion", "gem": "Shining Gem"}
    c1 = input().lower()
    time.sleep(1)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1 in loot_item):
            user.items.append(loot_item[c1])
            print(colored(f"\nYou carefully pick up the {c1} from the body and step back just in time before the trap door reopened totally swallowing the adventurer with rest of his equipment\n",'cyan'))
            ans = 'correct'
            scene3(black_dragon, user)
        elif(c1 =="leave"):
            print(colored("\nYou decide not to risk your luck with the mortal trap and pass over\n",'cyan'))
            ans='correct'
            scene3(black_dragon, user)
        else:
            print(colored("\nTYPE A VALID CHOICE: Spear,  Potion, Gem or Leave?\n",'green'))
            c1 = input().lower()

# Third and final scene that implement the combat system promting the player for actions and automatically exert the enemy actions

def scene3(black_dragon, user):
    print(colored("""

You finally arrive at end of the undergound labyrinth and a huge cave is opening in front of you. At the center of the cave there is a mountain of shining gold

and all kind of treasure. On top of this there is the biggest Black Dragon you ever seen sleeping.


You start to get close when one of his eye opened, and showing what seems to you a evil reptilian grin he gives you the welcome

Black Dragon: "You little mouse, you made me wait a long time. I have smelled the stench of your kind since before you entered the cave.


But finally my dinner is arrived! "

""", 'cyan'))
    print(colored("FIGHT!\n", 'green'))
    time.sleep(1)
    combat = "started"
    print("\nYou can attack, use an item or check your HP\n")

    #combat full turn with reset of shield function and check of poison status and poison damage
    while (combat =="started"):
        user.shield = False
        if user.turns_poison > 0:
            user.poison_dmg += 5
            user.hp -= 5
            user.turns_poison -= 1
            print("\nYou receive -5 hp damage from poison\n")
        else:
            user.status = "Healthy"
        turn = "ongoing"

        #user turn, where is possible to choose among check healt point or items/attacks list without loosing the turn or select one of the attacks/items available
        while (turn == "ongoing"):
            action = ""
            print(colored("\nTo consult the list of attacks or items available type: ATTACKS LIST or ITEMS LIST, while for use one of them just type its name. To check your current health points type: HP\n",'yellow'))
            action = input().title()
            if action == "Attacks List":
                attacks_list = []
                print("\nAttacks available:\n")
                for key, value in user.attacks.items():
                    attacks_list.append(key)
                print(colored(f"{attacks_list}",'magenta'))

            elif action == "Items List":
                print(colored(f"{user.items}",'magenta'))

            elif action in user.attacks:

                doSomething = getattr(user, user.attacks[action])
                doSomething(black_dragon)
                print(black_dragon.hp)
                turn = "end"

            elif action == "Hp":
                print(colored(f"\nYour HP: {user.hp}\n",'blue'))

            elif action in user.items:
                if action == "Dragonlance" or action == "Shining Gem":
                    user.item_use(action)
                else:
                    user.item_use(action)
                    turn = "end"
            else:
                print(colored("\nWrong command! Try again\n", 'green'))

        if black_dragon.hp <= 0:
            print(colored("\nWith your last blow you kill the Dragon gaining fortune and glory! Well done adventurer!\n",'cyan'))
            # combat = "ended"
            break
        elif black_dragon.hp < 100:
            print(colored("\nThe Black Dragon is gravely wounded\n",'red'))
        elif black_dragon.hp < 200:
            print(colored("\nThe Black Dragon is moderate wounded\n", 'red'))
            time.sleep(1)
        # Check of dragon action if will do a normal attack or prepare for power attack
        dragon_attack = random.randint(1, 100)
        if dragon_attack > 85 and black_dragon.power_attack == False:
            black_dragon.power_attack = True
            print(colored("\nThe Dragon holds his breath and prepare to attack\n", 'green'))
        else:
            if black_dragon.power_attack == True:
                black_dragon.breath(user)
                black_dragon.power_attack = False
            else:
                black_dragon.bite(user)
        if user.hp <= 0:
            print(colored("\nYOU DIED!\n", 'red'))
            combat = "ended"



if __name__ == '__main__':
    main()