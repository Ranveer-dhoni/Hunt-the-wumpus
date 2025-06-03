class Character:
    def __init__(self, char_name, char_decription):
        self.name = char_name
        self.description = char_decription
        self.conversation = None 

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """"""
        self.conversation = conversation

    def talk(self):
        """Allows characters to talk to the player"""
        if self.conversation is not None:
            print(self.name + " says:" + self.conversation)
        else:
            print(self.name + " does not want to talk to you")



