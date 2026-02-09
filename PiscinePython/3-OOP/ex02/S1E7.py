from S1E9 import Character


class Baratheon(Character):
    '''Subclasse Baratheon from Character class'''
    def __init__(self, first_name, is_alive=True,
                 family_name="Baratheon", eyes="Brown", hairs="Dark"):
        '''Subclasse Baratheon : Constructeur'''
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        '''Retourne la repr'''
        return self.__repr__

    def __repr__(self):
        '''Redefinie l'affichage de __repr__'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        '''Subclasse Baratheon : Methode redefinie'''
        self.is_alive = False
        return


class Lannister(Character):
    '''Subclass Lannister from Character class'''

    def __init__(self, first_name, is_alive=True,
                 family_name="Lannister", eyes="Blue", hairs="Light"):
        '''Subclasse Lannister : Constructeur'''
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        '''Retourne la repr'''
        return self.__repr__

    def __repr__(self):
        '''Redefinie l'affichage de __repr__'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        '''Subclasse Lannister : Methode redefinie'''
        self.is_alive = False
        return

    @classmethod
    def create_lannister(cls, name, status=True):
        '''Creer un Lannister, methode de classe'''
        return cls(name, status)


#  ======== TESTTTTTTTTTTTTTTTTS =========
# def main():
#     Robert = Baratheon("Robert")
#     print(Robert.__dict__)
#     print(Robert.__str__)
#     print(Robert.__repr__)
#     print(Robert.is_alive)
#     Robert.die()
#     print(Robert.is_alive)
#     print(Robert.__doc__)
#     print("---")
#     Cersei = Lannister("Cersei")
#     print(Cersei.__dict__)
#     print(Cersei.__str__)
#     print(Cersei.is_alive)
#     print("---")
#     Jaine = Lannister.create_lannister("Jaine", True)
#     print(f"Name : {Jaine.first_name, type(Jaine).__name__}", end="")
#     print(f" , Alive : {Jaine.is_alive}")


# if __name__ == "__main__":
#     main()
