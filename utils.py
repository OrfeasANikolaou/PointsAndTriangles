import random
import math


# generates a point in a cartesian map as a tuple, with only integer values
def rnd_point(start: int = -100, end: int = 100):
    return (random.randint(start, end), random.randint(start, end))


# calcualtes distance between two points in a cartesian map
def calc_distance(p1: tuple, p2: tuple):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


# given 3 sides, calculates area of a triangle using Heron's formula
# user must check if returned value is non-valid
def area_triangle(side_1: float, side_2: float, side_3: float):
    semiperimeter = (side_1 + side_2 + side_3) / 2
    tmp = (semiperimeter * (semiperimeter - side_1) *  
           (semiperimeter - side_2) * (semiperimeter - side_3))
    if tmp > 0:
        return math.sqrt(tmp)
    return 0

# returns average from a list
def avg_from_list(lst: list):
    sum_ = 0
    for obj in lst:
        sum_ += obj
    return sum_ / len(lst)


# returns median from a list (sorts it first if flag false)
def median_from_list(lst: list, sorted: bool = False):
    if not sorted:
        lst.sort()
    sz = len(lst)
    if sz % 2:
        return lst[sz // 2]
    return (lst[sz // 2] + lst[(sz // 2) + 1]) / 2


# returns range between min and max values in a list
def get_list_val_range(lst: list, sorted: bool = False):
    if not sorted:
        lst.sort()
    return lst[len(lst) - 1] - lst[0]


# returns standard deviation
def standard_deviation_from_list(lst: list):
    mean = avg_from_list(lst)
    summation = 0
    for obj in lst:
        summation += (obj - mean) ** 2
    return math.sqrt(summation / (len(lst) - 1))
