from abc import ABC, abstractmethod


class Character(ABC):
    '''Classe abstraite comprenant
    Un first name et un status is_alive
    Le status n'est pas obligatoire'''

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Constructeur de la Classe Character'''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        '''Abstract method de Class'''
        pass


class Stark(Character):
    '''Subclasse : Herite de la methode die() mais la redefinie'''
    def __init__(self, first_name, is_alive=True):
        '''Subclasse : Constructeur'''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''Subclasse : Methode redefinie'''
        self.is_alive = False
        return


# =========== TEEEEEEESSSSSSSTTTTTTTTT ===========
# def main():
#     Ned = Stark("Ned")
#     print(Ned.__dict__)
#     print(Ned.is_alive)
#     Ned.die()
#     print(Ned.is_alive)
#     print(Ned.__doc__)
#     print(Ned.__init__.__doc__)
#     print(Ned.die.__doc__)
#     print("---")
#     Lyanna = Stark("Lyanna", False)
#     print(Lyanna.__dict__)


# if __name__ == "__main__":
#     main()
