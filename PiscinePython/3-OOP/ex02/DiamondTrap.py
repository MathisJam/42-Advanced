from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Subclasse King : from Baratheon, Lannister'''
    def __init__(self, first_name, is_alive=True):
        '''Subclasse King : Constructeur'''
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        '''Change la variable eyes de l'instance'''
        self.eyes = color

    def set_hairs(self, hairColor):
        '''Change la variable hairs de l'instance'''
        self.hairs = hairColor

    def get_eyes(self):
        '''Retourne la variable eyes de l'instance'''
        return self.eyes

    def get_hairs(self):
        '''Retourne la variable hairs de l'instance'''
        return self.hairs

#  ======== TESTTTTTTTTTTTTTTTTS =========
# def main():
#     Joffrey = King("Joffrey")
#     print(Joffrey.__dict__)
#     Joffrey.set_eyes("blue")
#     Joffrey.set_hairs("light")
#     print(Joffrey.get_eyes())
#     print(Joffrey.get_hairs())
#     print(Joffrey.__dict__)


# if __name__ == "__main__":
#     main()
