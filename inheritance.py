class HumanClass:
    def __init__(self):
        print('HumanClass\'s init')
        self.hp = 100
        
class WizardClass(HumanClass):
    def __init__(self):
        super().__init__()
        self.mp = 50
        
    def output_info(self):
        print(f'Curren HP: {self.hp}, '
              f'MP: {self.mp}.')

wizard = WizardClass()
wizard.output_info()