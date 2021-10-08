from random import randint


def randomNC(count=10):
    min = pow(10, count - 1)
    max = pow(10, count) - 1
    # return list(map(int, str('0927236437')))
    return list(map(int, str(randint(min, max))))
