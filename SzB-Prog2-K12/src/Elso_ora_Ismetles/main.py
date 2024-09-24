import sys
from typing import NamedTuple
class Rollercoaster(NamedTuple):
    name: str
    world: str
    height: int
    time: int
def from_line(line:str)->Rollercoaster:
    tokens = line.strip('\n').split(';')
    return Rollercoaster(tokens[0],tokens[1],tokens[2],tokens[3])
def to_line(coaster:Rollercoaster)->str:
    return f"{coaster.name} ({coaster.world}):{coaster.time} "
def order(coasters:list[Rollercoaster])->dict[str:int]:
    mydict = {}
    for c in coasters:
        pass
def main()->None:
    while True:
        try:
            ls = []
            file=open(sys.argv[1])
            for line in file:
                ls.append(from_line(line))
            for l in ls:
                print(to_line(l))

            raise Exception
        except Exception:
            break
if __name__ == '__main__':
    main()