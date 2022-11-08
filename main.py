class Qestion1:
    """Решение задания 1"""

    def __init__(self, message):
        data = input(message)
        data = data.split()
        if not data:
            raise Exception("Отсутствует ввод")
        self.name = data[0]
        self.surname = data[1] if len(data) > 1 else ''

    def __str__(self):
        return f" Hello {self.name} {self.surname}! You just delved into Python. Great start!"


def qestion2() -> str:
    """Решение задания 2"""
    thickness = 5
    c = 'H'

    for i in range(thickness):
        yield (c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1)

    for i in range(thickness+1):
        yield (c*thickness).center(thickness*2) + (c*thickness).center(thickness*6)

    for i in range((thickness+1)//2):
        yield (c*thickness*5).center(thickness*6)

    for i in range(thickness+1):
        yield (c*thickness).center(thickness*2) + (c*thickness).center(thickness*6)

    for i in range(thickness):
        yield ((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)


def qestion3(text: str) -> str:
    """Решение задания 3"""
    return text.title()


def qestion4(amount: float) -> str:
    """Решение задания 4"""
    if (amount > 0):
        return '{:000,.2f}'.format(amount)


def qestion5(height: int, text: str) -> str:
    """Решение задания 5"""
    width = height * 3
    data = list()

    for i in range(1, height, 2):
        data.append(('.|.' * i).center(width, '-'))

    data.append(text.center(width, '-'))

    for i in range(height-2, 0, -2):
        data.append(('.|.' * i).center(width, '-'))

    return '\n'.join(data)


def qestion6(arg: str) -> int:
    """Решение задания 6"""
    n = 1
    for el in map(int, filter(lambda x: x.isdigit(), tuple(arg))):
        if el: n *= el
    return n


if __name__ == '__main__':

    print('\n Задание 1', Qestion1('Введите имя и фамилию: '), sep='\n')
    print('\n Задание 2', *qestion2(), sep='\n')
    print('\n Задание 3', qestion3('hello world'), sep='\n')
    print('\n Задание 4', qestion4(1205760.23), sep='\n')
    print('\n Задание 5', qestion5(14, 'WELCOME'), sep='\n')
    print('\n Задание 6', qestion6('123405'), sep='\n')
