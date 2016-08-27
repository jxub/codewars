from functools import reduce

#functional programming with reduce() is the way!
def average(array):
    return round((reduce((lambda x, y: x + y), array)) / len(array))
