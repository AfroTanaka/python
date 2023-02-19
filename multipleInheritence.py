class WizardClass:
    def __init__(self):
        self.mp = 100
        print('WizardClass\'s init')
        
    def cast_spell(self):
        print('cast a spell')

class SwordFighterClass:
    def attack_with_sword(self):
        print('Attack with the sword')

class MagicSwordFighterClass(WizardClass, SwordFighterClass):
    pass

msf = MagicSwordFighterClass()
msf.cast_spell()
msf.attack_with_sword()