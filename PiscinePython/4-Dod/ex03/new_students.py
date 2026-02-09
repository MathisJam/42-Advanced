import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Classe Student comportant
    le nom, nom de famille, login
    status actif, et son id'''
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: int = field(default=generate_id(), init=False)

    def __post_init__(self):
        self.login = self.name[0].capitalize() + self.surname.lower()


# def main():
#     try:
#         student = Student(name="Edward", surname="agle")
#         print("Should work : ", student, end="\n")
#         print("------------------------")
#         # ---- SHOULD NOT WORK ----
#         student = Student(name="Edward", surname="agle", id="dsadsa")
#     except TypeError as error:
#         print(f"TypeError: {error}")
#         return


# if __name__ == "__main__":
#     main()
