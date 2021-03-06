class Soldier:
    def __init__(self, level):
        self.level = level

    def attack(self):
        return self.level * 1

class Jedi:
    def __init__(self, level):
        self.level = level
    
    def attackWithSaber(self):
        return self.level * 100

class JediAdpter:
    def __init__(self, character):
        self.character = character
    
    def attack(self):
        return self.character.attackWithSaber()

class starWarsGame:
    def __init__(self, character):
        self.character = character
    
    def fight_enemy(self):
        print(f"You caused {self.character.attack()} of damage to the enemy")


starWarsGame(JediAdpter(Jedi(2))).fight_enemy()