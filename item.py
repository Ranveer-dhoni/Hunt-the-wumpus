class Item:
    def __init__(self, name, description):
        self.name = name 
        self.description = description 

    def  describe(self):
        print("You see a" + self.name + ": " + self.description)
    def get_name(self):
        return self.name    