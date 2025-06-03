class Cave: 
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None 
        set.linked_caves = {}

    def set_name(self, cave_name)
        self.name = cave_name 

        def get_name(self):
            return self.name 

    def set_definition(self, cave_description)
        self.description = cave_description

    def get_decription(self):
        return self.description 
     
    def describe(self):
        print(self.descrpition)

    def link_caves(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
       # print(self.name + "Linked caves:" + repr(self.linked.caves))

    def get_details(self):
        print(self.name)
        
        for direction, cave in self.linked_caves.items():
            print("The " + cave_get_name() + "is" + direction)
    
    def move(self, direction):
        if direction in self.linked_caves[direction]
            return self.linked_caves[direction]
        
         else:
            print("You cannot go that way")
            return self
