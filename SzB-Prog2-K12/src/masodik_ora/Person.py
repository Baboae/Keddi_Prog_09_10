from functools import total_ordering


@total_ordering
class Person:
    id: str
    name: str
    _age: int
    male: bool

    def __init__(self, id: str, name: str, age: str, male: bool):
        self.id = id
        self.__name = name
        self._age = age
        self.male = male

    def __str__(self) -> str:
        return f"{self.id}, {self.__name}, {self._age}, {self.male}"

    def __repr__(self) -> str:
        return f"#{self.id}: {self.__name} ({self._age}, male={self.male})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Person) and self.id == other.id

    def __lt__(self, other):
        if not isinstance(other,Person):
            return NotImplemented
        return self.id < other.id

    def get_age(self) ->int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            raise  ValueError("Negatív Életkor")
        self._age = value

        @property
        def name(self):
            return self.__name
        @name.setter
        def namesetter(self, value: str) -> None:
            self.name = value

def main() -> None:
    a = Person("ah2snn", "baboae",  "22", True)
    print(f"reprezentáció fgv.:\n\n{repr(a)}\n")
    print(f"__str__ fgv.:\n\n{str(a)}\n")
    print(f"hivatkozás elemenként:\n\n{a.id, a._Person__name, a._age, a.male}")

if __name__ == "__main__":
    main()
