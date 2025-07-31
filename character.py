"""Character class for Hunt the Wumpus game"""

class Character():
    """Defines the Character class"""
    
    def __init__(self, char_name, char_description):
        self.name = char_name 
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Outputs description of the character"""
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """What the character says when talked to"""
        self.conversation = conversation

    def talk(self):
        """Manages talking to characters"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self):
        """Manages fighting with characters"""
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    """Defines the Enemy subclass"""
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.attacks = []

    def set_weakness(self, item_weakness):
        """Sets a weakness for the enemy"""
        self.weakness = item_weakness

    def get_weakness(self):
        """Returns the enemy's weakness when fighting"""
        return self.weakness
    
    def add_attacks(self,attack):
        self.attacks.append(attack)

    def get_attacks(self):
        return self.attacks 
    

    def fight(self, combat_item):
        import random
        selected_attacks = random.sample(self.attacks, 2) if len(self.attacks) >= 2 else self.attacks 
        print("\n["+ self.name + " uses: ")
        print("]")

        if combat_item == self.weakness:
         print("You fend" + self.name + "off with the " + combat_item)
         return True
        else:
            print(self.name + "swallows you, little wimp")
            return False 



