class Cave:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def link_cave(self, cave, direction):
        self.linked_caves[direction.lower()] = cave

    def get_details(self):
        print(f"\n{self.name}\n--------------------\n{self.description}")
        for direction, cave in self.linked_caves.items():
            print(f"The {cave.name} is {direction}")
        if self.item:
            self.item.describe()

    def move(self, direction):
        direction = direction.lower()
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way.")
            return self

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def remove_item(self):
        self.item = None

 