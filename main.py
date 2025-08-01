"""Main program for Hunt the Wumpus game"""
from cave import Cave
from character import Enemy
from item import Item 
import random

# Create Caves
cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave.")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings.")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack.") 
tower = Cave("Tower")
tower.set_description("A tall stone tower with echoing winds")
chamber = Cave("Chamber")
chamber.set_description("A hidden chamber behind a waterfall")
libary = Cave("Libary")
libary.set_description("A dusty old room with key information and ancient books")
throne = Cave("Throne Room")
throne.set_description("A large majestic room empty with the exception of a large cracked golden throne")
forge = Cave("Forge")
forge.set_description("A blazing forge filled with tools and sparks")
dock = Cave("Dock")
dock.set_description("An abandoned dock looking over the vast ocean")
crater = Cave("Crater")
crater.set_description("A smoldering pit of rock with faint magical hums")
overlook = Cave("Overlook")
overlook.set_description("A cliff that views all the paths below")
archives = Cave("Archives")
archives.set_description("A sealed vault of relics and ancient loot")

# Link Caves
dungeon.link_cave(cavern,"North")
cavern.link_cave(dungeon, "South")
dungeon.link_cave(grotto, "West")
grotto.link_cave(dungeon, "East")
cavern.link_cave(tower, "East")
tower.link_cave(cavern, "West")
tower.link_cave(chamber, "South")
chamber.link_cave(tower, "North")
chamber.link_cave(libary, "East")
libary.link_cave(chamber, "West")
libary.link_cave(throne, "South")
throne.link_cave(libary, "North")
throne.link_cave(forge, "West")
forge.link_cave(throne, "East")
forge.link_cave(dock, "South")
dock.link_cave(forge, "North")
throne.link_cave(crater, "East")
crater.link_cave(throne, "West")
crater.link_cave(overlook, "North")
overlook.link_cave(crater, "South")
overlook.link_cave(archives, "East")
archives.link_cave(overlook, "West")

# Create Enemies
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Come closer. I can't see you!")
harry.set_weakness("Math Problems")
harry.add_attacks("Fearsome Flop - The Wumpus flops dramatically onto the ground causing a tremor that unbalances everyone.")
harry.add_attacks("Tempest Spiral - Creates a mini tornado that lifts up enemies")
harry.add_attacks("Moon Howl - Summons a lunar pulse that buffs the wumpus and destroys the weak willed")
dungeon.set_character(harry)

boss = Enemy("Lord Brookali", "The guardian of the one piece")
boss.set_conversation("Only the worthy shall claim the treasure")
boss.set_weakness("Sword of Gryffindor")
dock.set_character(boss)

# Create Items
sword = Item("sword", "A sharp silver blade with a ruby handle")
math_problems = Item("Math Problems","A collection of tricky math problems that melts the Wumpus's brain")
armour = Item("Golden Armour", "Radiates with divine energy and blocks most attacks")
amulet = Item("Protective Lunar Amulet", "Emits a soft hum that wards off evil")
mug = Item("Mr Brook's coffee mug", "Still warm and rumored to grant wisdom and courage")
gryffindor = Item("Sword of Gryffindor", "A sword pulled out of the sorting hat")
one_piece = Item("the one piece", "The ultimate treasure. Legends say it either brings peace or chaos")

# Defense Items for Wumpus Attacks
quake_boots = Item("quake boots", "Heavy boots that negate tremors from Fearsome Flop")
tornado_helm = Item("tornado helm", "A helm that anchors the wearer against vortexes")
luna_charm = Item("lunar charm", "Protects the mind from Moon Howl's fear effect")

# Junk Items
rubber_duck = Item("rubber duck", "Squeaky and silly but useless against real threats")
cheese_slice = Item("cheese slice", "Delicious but useless in battle")
stale_biscuit = Item("stale biscuit", "Dry and brittle, may cause a tummy ache")
gravity_glove = Item("gravity glove", "Cool but no real defense")
scythe = Item("scythe", "Looks deadly but too heavy to wield")

# Place Key Items
grotto.set_item(sword)
cavern.set_item(math_problems)
tower.set_item(armour)
chamber.set_item(amulet)
libary.set_item(mug)
throne.set_item(gryffindor)
dock.set_item(one_piece)

# Player State
current_cave = cavern
inventory = []
dead = False

# Required defense items will be available later
defense_required = {
    "Fearsome Flop": "quake boots",
    "Tempest Spiral": "tornado helm",
    "Moon Howl": "lunar charm"
}

print("Welcome to Hunt the Wumpus!")
print("Explore the caves, gather items, and prepare to face mighty foes.")

# Main Game Loop (exploration first)
while not dead:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant:
        inhabitant.describe()

    command = input("> ").strip().lower()

    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)

    elif command == "talk":
        if inhabitant:
            inhabitant.talk()
        else:
            print("There is no one here to talk to.")

    elif command == "fight":
        if inhabitant and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input("> ").strip().lower()

            item_names = [item.get_name().lower() for item in inventory]
            if fight_with in item_names:
                selected_attacks = inhabitant.get_attacks()
                attack = random.choice(selected_attacks) if selected_attacks else None

                if attack:
                    print(f"{inhabitant.name} prepares a powerful move: {attack}")
                    move_name = attack.split(" -")[0]
                    required_defense = defense_required.get(move_name)
                    if required_defense and required_defense.lower() not in item_names:
                        print(f"You were unprepared for {move_name}. You are defeated.")
                        dead = True
                        continue

                if inhabitant.fight(fight_with):
                    print("Bravo, hero! You won the fight!")
                    current_cave.set_character(None)
                else:
                    print("You lost the fight. Game over.")
                    dead = True
            else:
                print("You don't have that item.")
        else:
            print("There is no one here to fight.")

    elif command == "take":
        item = current_cave.get_item()
        if item:
            inventory.append(item)
            print("You picked up the " + item.get_name() + ".")
            current_cave.remove_item()
        else:
            print("There is nothing to take here.")

    elif command == "inventory":
        if inventory:
            print("You have:")
            for i in inventory:
                print("- " + i.get_name())
        else:
            print("Your inventory is empty.")

    elif command == "chests":
        print("You found a locked chest! Choose one item from each!")
        chest_rooms = {
            "Crater": [quake_boots, rubber_duck, cheese_slice],
            "Overlook": [tornado_helm, scythe, stale_biscuit],
            "Archives": [luna_charm, stale_biscuit, gravity_glove] 
        }

        for room_name, items in chest_rooms.items():
            print(f"You open a mysterious chest in the {room_name}...")
            print("Inside, there are three items. Choose one:")
            for item in items:
                print(f"- {item.get_name()}")
            choice = ""
            item_lookup = {item.get_name().lower(): item for item in items}
            while choice not in item_lookup:
                choice = input("Which item do you choose? ").strip().lower()
            inventory.append(item_lookup[choice])
            print(f"You picked up the {choice}.\n")

        print("You feel prepared now. Face the challenges ahead!")

    else:
        print("I don't understand that command. Try 'north', 'take', 'talk', 'fight', 'inventory', or 'chests'.")
