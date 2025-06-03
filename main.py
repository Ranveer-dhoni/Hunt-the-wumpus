from cave import Cave 

cavern = Cave("Cavern")
cavern.set_definition("A damp and diry cave")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack.")

cavern.link_caves(dungeon, "South")
dungeon.link_cave(cavern, "North")
dungeon.link_caves(grotto, "West")
grotto.link_caves(dungeon, "East")

current_cave = cavern
while True:
    print("\n")
    current_cave.get_details()
    command = input("> ")
    current_cave = current_cave.move(command)
