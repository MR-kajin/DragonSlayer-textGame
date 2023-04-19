THE DRAGONSLAYER GAME

Description: This program is a small text-based game that will let you descend in a dragon's cave and fight him! 
This Python Program was created as a Final Project for the HarvardX CS50P: Introduction to Programming in Python 2022 course via edx.org. This code has been created by Marco Raffaele, EdX user: marco-raffaele, Github user: MR-kajin. Submission Period: August 2022.

Goal of the Final Project: Create a program that let the user have a short role player game (RPG) adventure, prompt him for different actions and use various attacks or items to fight against an imaginary Dragon. 
I wanted to create a program where I could apply the knowledge learned during the course and especially play with the class and objects. I've always been a fan of PC RPG games and creating one as the first small project came naturally and fun to implement. 
I think I could have made the experience of the game longer and deeper, or integrated a GUI, but I also think that as a first python project it is sufficiently complex, and also for the future I would like to focus on some more practical project maybe oriented to the web. 

Getting Started: To use this software, the following libraries must be installed in terminal.

random
Installed as part of Python Standard Library

time
Installed as part of Python Standard Library

termcolor
Python library for color and formatting in terminal 
pip install termcolor

re - Regular expression operations
Installed as part of Python Standard Library

os 
Installed as part of Python Standard Library

sys
Installed as part of Python Standard Library


both project.py and game_classes.py files have to be in the same folder. 



To Use�. Lunch the program using the terminal command: python project.py
The game will start asking the user if he wants to play or exit the game, then to choose a name and one of the two classes of players available, Knight or Wizard, for his adventurer. The two classes are characterized by different attacks and items as well as a different amount of max health points.  To interact with the 3 scenes of the game you will need to type one of the options provided, it is not case sensitive. 
The use of an object will consume it, and the most powerful attacks require the presence in your stock of objects of a particular object, different for the two classes. Using the powerful attack will consume the object. 

List of command in the game and effects:
1.	Attacks list: shows a list of the attacks available for that class
2.	Items list: shows a list of the items available in that moment
3.	HP: shows the health point left to your character (check them often!)

Knight attacks:
1.	Sword slash: sword attack with chances to deal a critical or lethal hit!
2.	Shield: spend your action giving you protection for the next Dragon attack
3.	Spear pierce: powerful attack with chances to deal critical hit.

Wizard attacks:
1.	Magic dart: cast a magic with chances to deal a critical or lethal hit!
2.	Magic shield: spend your action giving you protection for the next Dragon attack
1.	Healing: cure your health points (limited number of spell available, points (HP can�t exceed the maximum for the class)
3.	Fire ball: powerful magic with chances to deal critical hit.

Items:
1.	Cure potion: increase your health points (HP can't exceed the maximum for the class)
2.	Shield: needed for the proper action (it is not consumed with the action)
3.	Herbs: cure the poisoned status and regain part of the lost HP
4.	Unstable Potion: can heals you for a large amount of HP or there is a small chance that instead is getting you poisoned
5.	Dragonlance: needed for the Knight powerful attack. 
6.	Shining gem: needed for the Wizard powerful attack

What is in the folder: project.py --- main Python Program, game_classes.py --- file containing the code related to the classes used in the main program, README.md --- This File you are reading right now, requirements.txt--- Required Libraries needing to be installed that are not included in the python standard library, test_project.py --- Test File for ensuring selected functions work

