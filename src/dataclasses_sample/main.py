import dataclasses


@dataclasses.dataclass
class Person:
    name: str
    age: int


def main1():
     print('Hello, world!')


def main2():
    p = Person('John', 30)
    print(p)


if __name__ == '__main__':
    main2()
