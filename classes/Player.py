'''
Defines a player, that can be controlled by either a real user or AI.
'''
class Player:

    ai_controlled = False
    hp = None
    mana = None

    def __init__(self, ai_controlled, hp, mana):
        self.ai_controlled = ai_controlled
        self.hp = hp
        self.mana = mana
