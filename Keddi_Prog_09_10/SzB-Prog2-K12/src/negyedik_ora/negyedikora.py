##otodik amugy, es nem ezt vettuk hanem a geometrias baszakodast
from functools import total_ordering

@total_ordering
class Person(object):

    id: str
    __name: str
    _age: int
    male: bool
    def __init__(self, id: str, name: str, age: int, male: bool = True):
        self.id = id
        self.name = name
        self.age = age
        self.male = male
    def __str__(self) -> str:
        return f"#{self.id}: {self.name} ({self.age}, is_male = {self.male})"
    def __repr__(self) -> str:
        return f"{self.id} {self.name} {self.age} {self.male}"
    def __eq__(self, other):
        if isinstance(other, Person):
            return isinstance(other, Person) and self.id == other.id
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id < other.id
    def __hash__(self):
        return  hash(self.id)
    def get_age(self) ->int:
        return self.age
    def set_age(self,value: int) -> None:
        if value < 0:
            raise ValueError("Negatív Érték.")
        self._age = value
def main() -> None:
    p1 = Person("asd123", "babo", 22, True)
    print(p1)
    print(Person.get_age(p1))
if __name__ == '__main__':
    main()
