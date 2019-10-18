__author__ = 'Les Pounder'

"""
    The lines below import modules of code into our game,
    in particular these import time functions allow us to pause and stop the game,
    and random provides a method of choosing random numbers or characters.
"""
from time import *
from random import *
import os,sys
from art import *

"""
    Simple function that clears the terminal screen
"""
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def title():
    print(text2art('I', font='alpha'))
    print(text2art('Cant', font='alpha'))
    print(text2art('Code', font='alpha'))

def north():
    print ("To go to the third floor press 3 then enter")

def east():
    print ("To go to the first floor press 1 then enter")

def west():
    print ("To go to the lunch room press l then enter")


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What does your school ID say?")
    #randint is a great way of adding some variety to your players statistics through randomness
    HP = randint(5,20)
    MP = randint(5,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi", "Are you a hero?", "Are you from this village?", "There has been a dark shadow cast across the village"]
    npcnamechoice = ["Bordon", "Sheehan", "Alexander", "Barvey"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to play basketball with me?\n")
    shuffle(responses)
    print ("Press y to talk to athletic kid")
    if input() == "y":
        print ("%s: %s" % (npcname, responses[0]))
    else:
        print ("%s: Goodbye" % npcname)

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "Boss Messina"
    print ("\nSuddenly you hear a gunshot far in the distance, and from the shadows you see an "+enemyname+" slowly trotting towards you with his son Frankie at his side....")
    #print enemyname
    print ("Your enemy has %s Health Points" % str(enemyHP))
    print ("Your enemy has %s Magic Points" % str(enemyMP))


"""
    We now use our functions in the game code, we call functions title() and setup() for our character.
"""
clear_screen()
title()
setup()
global name
global HP
global MP
global move
global enemyHP
print ("Welcome to the land of Brooklyn friends Highschool, %s" % name)
#Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour Determination is" + " " + str(HP))
print ("Your Intellegence skill is" + " " + str(MP))



print ("Would you like to venture out into the land? Press y then enter to continue")
#Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    print ("You wake up in your home, with the beeping of cars right outside of your window, on your doorknob, you see your backpack and pens")
    print ("Would you like to take your Backpack and pens? Press y then enter to continue")
    if input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("pens")
        weapons.append("backpack")
        print ("You are now walking to Brooklyn Friends carrying your %s and your %s" % (weapons[0], weapons[1]))
        print ("Armed with your %s and %s you swing open the front doors doors at BFS and are immediatly welcomed by Donna." % (weapons[0], weapons[1]))
    elif input() == "n":
        print ("You choose not to take your weapons")
        print ("Armed with your sense of humour, you swing open the front doors doors at BFS and are immediatly welcomed by Donna.")
elif input() == "sick":
    print ("You stay at home, curled up in bed with a box of tissues at your side watching tv. Your class will miss you.")
    print ("Game Over")
    sys.exit(0)

print ("You look down at your crinkled schedule, You have a freei, do you want to go to the lunch room, the 1st floor, or the 3rd floor.")

#Remember those functions we created at the start of the code? Well here we are using them in the game.
print ("\n")
north()
east()
west()
move = input("Where would you like to go? ")
if move == '3':
    print ("\nYou walk to the 3rd floor to go to math class.")
    print ("Michael Leibis is in your path and greets you")
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == '1':
    print ("\nYou walk to the 1st floor to go to art history class.")
    print ("Mark Buenzle is in your path and greets you")
elif move == 'l':
    print ("\nYou walk to the lunch room, to get food")
    print ("Frankie Messina is in your path and greets you\n")

villager()
enemy()
sleep(3)

fight = input("Do you wish to fight?" )

if fight == "y":
    while HP > 0:
#This loop will only work while our characters HP is greater than 0.
        hit = randint(0,5)
        print ("You swing your sword and cause %s of damage" % str(hit))
        enemyHP = enemyHP - hit
        print (enemyHP)
        enemyhit = randint(0,5)
        print ("The ogre swings a club at you and causes %s of damage" % str(enemyhit))
        HP = HP - enemyhit
        print (HP)
else:
    print ("You turn and run away from the ogre")

print ("This is where this template ends, this is now YOUR world, build your adventure and share it with the world")

print ("   _       _                 _")
print ("  /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___")
print (" //_\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ")
print ("/  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/")
print ("\_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|)")

print ("                     _ _")
print ("  __ ___      ____ _(_) |_ ___")
print (" / _` \ \ /\ / / _` | | __/ __|")
print ("| (_| |\ V  V / (_| | | |_\__ \ ")
print (" \__,_| \_/\_/ \__,_|_|\__|___/)")

print (" _   _  ___  _   _")
print ("| | | |/ _ \| | | |")
print ("| |_| | (_) | |_| |")
print (" \__, |\___/ \__,_|")
print (" |___/")
