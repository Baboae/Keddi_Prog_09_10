from functools import total_ordering

@total_ordering
class Person(object):

    age_limit: int = 18
    pizzas: str = []
    neptun: str

    id = str
    __name = str
    _age = int
    male = bool
    # region class functions
    def __init__(self, id: str, name: str, age: int, male: bool, pizzas: list[str]):
        self.id = id
        self.name = name
        self.age = age
        self.male = True
        self.pizzas : list[str] = []

    def __str__(self) -> str:
        return f"{self.id}: {self.name} ({self.age}, {self.male})"

    def __repr__(self) -> str:
        return f"{self.id}, {self.name}, {self.age}, {self.male}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Person):
            return isinstance(other, Person) and self.id == other.id
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id < other.id
    def __hash__(self):
        return hash(self.id)
    def is_adult(self):
        return self.age >= self.age_limit
    @property
    def age(self) ->int:
        return self._age
    @age.setter
    def age(self, value) ->None:
        if value < 0:
            raise ValueError("Negatív értéket adtál meg kornak.")
        self._age = value
    # endregion class functions x
class Student(Person):
    neptun__: str
    def __init__(self, id: str, name: str, age: int, male: bool, neptun: str):
        super().__init__(id, name, age, male)
        self.__neptun = neptun
    @property
    def neptun(self):
        return self.__neptun
    @neptun.setter
    def neptun(self, n):
        self.__neptun = n

def main() -> None:
    p1 = Person("b0922m", "babo", 17, True, "songoku, normal")
    print(f"{p1}\n{p1.pizzas}")
if __name__ == '__main__':
    main()