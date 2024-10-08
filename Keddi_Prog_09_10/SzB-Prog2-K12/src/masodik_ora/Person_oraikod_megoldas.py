from functools import total_ordering


@total_ordering
class Person:
    id: str
    name: str
    _age: int
    male: bool

    def __init__(self, id: str, name: str, age: int, male: bool = True):
        self.id = id
        self.name = name
        self._age = age
        self.male = male

    def __str__(self) -> str:
        return f"#{self.id}: {self.name} ({self._age}, {self.male})"

    def __repr__(self) -> str:
        return f"{self.id}, {self.name}, {self._age}, {self.male}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Person) and self.id == other.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id < other.id

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Negatív életkor")
        self._age = value

def main() -> None:
    p1 = Person("ID1", "Aladár",
                18, True)
    # print(p1._age)
    print(p1.get_age())
    print(p1)
    p1.set_age(20)
    print(f"getage_:{Person.get_age(p1)}")



if __name__ == '__main__':
    main()