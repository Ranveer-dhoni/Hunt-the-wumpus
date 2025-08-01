class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is here! {self.description}")

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

class Enemy(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None
        self.attacks = []

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, item):
        if item == self.weakness:
            print(f"You fend off {self.name} with the {item}!")
            return True
        else:
            print(f"{self.name} crushes you effortlessly. Your {item} is useless.")
            return False

    def add_attacks(self, attack):
        self.attacks.append(attack)

    def get_attacks(self):
        return self.attacks



