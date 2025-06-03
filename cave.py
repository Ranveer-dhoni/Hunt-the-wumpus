"""Cave class for hunt a wumpus"""
class Cave: 
    """Defines attributes and methods for cave objects"""
    def __init__(self, cave_name):
        """Sets the class attributes"""
        self.name = cave_name
        self.description = None 
        set.linked_caves = {}

    def set_name(self, cave_name):
        """Sets the cave name"""
        self.name = cave_name 

        def get_name(self):
            """Gets the cave name"""
            return self.name 

    def set_definition(self, cave_description):
        """Sets the description"""
        self.description = cave_description

    def get_decription(self):
        """gets the description"""
        return self.description 
     
    def describe(self):
        """Prints teh caves description"""
        print(self.descrpition)

    def link_caves(self, cave_to_link, direction):
        """Populates dictionary of linked caves"""
        self.linked_caves[direction] = cave_to_link
       # print(self.name + "Linked caves:" + repr(self.linked.caves))

    def get_details(self):
        print(self.name)

        for direction, cave in self.linked_caves.items():
            print("The " + cave_get_name() + "is" + direction)
    
    def move(self, direction):
        if direction in self.linked_caves[direction]:
            return self.linked_caves[direction]
        
        else:
            print("You cannot go that way")
            return self
