from adding import add
from sub import subtract
def test():
    assert(add(3,4)) == 7
    assert(subtract(4,3)) == 1


if __name__ == "__main__":
    print(test())