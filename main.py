"""Main program for Hunt the Wumpus game"""
from cave import Cave
from character import Enemy
from item import Item 

cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave.")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings.")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack.") 
tower = Cave("tower")
tower.set.description("A tall stone tower with echoing winds")
chamber = Cave("Chamber")
chamber.set.description("A hidden chamber behind a waterfall")
libary = Cave("libary")
libary.set.description("A dusty old room with key information and ancient books")
throne = Cave("Thrown Room")
throne.set.description("A large majestic room empty with the exception of a large cracked golden throne")
forge = Cave("Forge")
forge.set.description(" A blazing forge filled with tools and sparks")
dock = Cave("Dock")
dock.set.description("An abandoned dock looking over the vast ocean")
crater = Cave("Crater")
crater.set.description("A smoldering pit of rock with feint magical hums")
overlook = Cave("Overlook")
overlook.set.description("A cliff that views alll the paths below")
archives = Cave("Archives")
archives.set.description("A sealed vault of relics and ancient loot")

dungeon.linked_cave(cavern,"North")
cavern.linked_cave(dungeon, "South")
dungeon.linked_cave(grotto, "West")

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Come closer. I can't see you!")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

current_cave = cavern
dead = False

while dead is False:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) is True:
                print("Bravo, hero you won the fight!")
                current_cave.set_character(None)
            else:
                print("Scurry home, you lost the fight.")
                print("That's the end of the game.")
                dead = True
        else:
            print("There is no one here to fight with")
