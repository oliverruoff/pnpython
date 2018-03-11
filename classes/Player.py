'''
Defines a player, that can be controlled by either a real user or AI.
'''
class Player:

    name = 'name'
    age = None
    profession = 'profession'
    ai_controlled = False
    hp = None
    mana = None
    luck = None
    strength = None
    dexterity = None
    constitution = None
    appearance = None
    education = None
    size = None
    intelligence = None
    movement = None
    charme = None
    intimidate = None
    encourage = None
    persuade = None
    calm_down = None
    lie = None
    lead = None
    first_aid = None
    climb = None
    craft = None
    swim = None
    lock_pick = None
    search_for_traces = None
    sneak = None
    throw = None
    nature_study = None
    perception = None
    eavesdrop = None
    scout = None
    evade = None
    hand_to_hand_fighting = None
    close_combat = None
    ranged_fight = None


    def __init__(self, name, age, profession, ai_controlled, hp, mana, luck, 
    	    strength, dexterity, constitution, appearance, education, size, 
    	    intelligence, movement, charme, intimidate, encourage, persuade, 
    	    calm_down, lie, lead, first_aid, climb, craft, swim, lock_pick, 
    	    search_for_traces, sneak, throw, nature_study, perception, eavesdrop, 
    	    scout, hand_to_hand_fighting, close_combat, ranged_fight):
        self.name = name
        self.age = age
        self.profession = profession
        self.ai_controlled = ai_controlled
        self.hp = hp
        self.mana = mana
        self.luck = luck
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.appearance = appearance
        self.education = education
        self.size = size
        self.intelligence = intelligence
        self.movement = movement
        self.charme = charme
        self.intimidate = intimidate
        self.encourage = encourage
        self.persuade = persuade
        self.calm_down = calm_down
        self.lie = lie
        self.lead = lead
        self.first_aid = first_aid
        self.climb = climb
        self.craft = craft
        self.swim = swim
        self.lock_pick = lock_pick
        self.search_for_traces = search_for_traces
        self.sneak = sneak
        self.throw = throw
        self.nature_study = nature_study
        self.perception = perception
        self.eavesdrop = eavesdrop
        self.scout = scout
        self.evade = dexterity/2
        self.hand_to_hand_fighting = hand_to_hand_fighting
        self.close_combat = close_combat
        self.ranged_fight = ranged_fight
