import random
import math
import statistics

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
    return math.sqrt(
        semiperimeter
        * (semiperimeter - side_1)
        * (semiperimeter - side_2)
        * (semiperimeter - side_3)
    )


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


def get_list_val_range(lst: list, sorted: bool = False):
    if not sorted:
        lst.sort()
    return lst[len(lst) - 1] - lst[0]


def get_standard_deviation(lst: list):
    ...

#  points = []
#  for i in range(500):
#      points.append(rnd_point())
#      print(f'{points[i]}: {points[i][0]}, {points[i][1]}')

#  for i in range(4):
#      for j in range(i+1, 4):
#          for k in range(j+1, 4):
#              print(f'{i}, {j}, {k}')
