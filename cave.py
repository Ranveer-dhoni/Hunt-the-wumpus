"""Cave class for Hunt the Wumpus game"""
class Cave:
    """Defines the cave object' attributes"""

    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.item = None 

    def set_description(self, cave_description):
        """Sets description for the cave object"""
        self.description = cave_description 

    def get_description(self):
        """Returns the cave object description"""
        return self.description

    def set_name(self, cave_name):
        """Sets the name for cave objects"""
        self.name = cave_name

    def get_name(self):
        """Returns the name of a cave object"""
        return self.name

    def set_character(self, new_character):
        """Places character objects into a cave"""
        self.character = new_character

    def get_character(self):
        """Returns if a character object is present in a cave"""
        return self.character
    
    def set_item(self,item):
        self.item = item 
    
    def get_item(self):
        return self.item
    
    def remove_item(self):
        self.item = None 

        

    def describe(self):
        """Prints cave object description to screen"""
        print(self.description)

    def link_cave(self, cave_to_link, direction):
        """Defines links to other caves"""
        self.linked_caves[direction] = cave_to_link
        # print(self.name + " linked caves: " + repr(self.linked_caves))

    def get_details(self):
        """Prints details about the current cave"""
        print(self.name)
        print("----------")
        print(self.description)
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        """Manages movement between caves"""
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self
 