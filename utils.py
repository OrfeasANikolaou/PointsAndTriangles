import random
import math


# generates a point in a cartesian map as a tuple, with only integer values
def rnd_point(start: int = -100, end: int = 100):
    return (random.randint(start, end), random.randint(start, end))


# calcualtes distance between two points in a cartesian map
def calc_distance(p1: tuple[int, int], p2: tuple[int, int]):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


# given 3 sides, calculates area of a triangle using Heron's formula
# user must check if returned value is non-valid
def area_triangle(side_1: float, side_2: float, side_3: float):
    semiperimeter = (side_1 + side_2 + side_3) / 2
    tmp = (
        semiperimeter
        * (semiperimeter - side_1)
        * (semiperimeter - side_2)
        * (semiperimeter - side_3)
    )
    if tmp > 0.000001:
        return math.sqrt(tmp)
    return 0


# returns average from a list, None if list empty
def avg_from_list(lst: list):
    if len(lst) == 0:
        return None
    sum_ = 0
    for obj in lst:
        sum_ += obj
    return round(sum_ / len(lst), 2)


# returns median from a list (sorts it first if flag false), None if list empty
def median_from_list(lst: list, sorted: bool = False):
    if len(lst) == 0:
        return None
    if not sorted:
        lst.sort()
    sz = len(lst)
    if sz % 2:
        return round(lst[sz // 2], 2)
    return round((lst[sz // 2] + lst[(sz // 2) + 1]) / 2, 2)


# returns range between min and max values in a list, None if list empty
def get_list_val_range(lst: list, sorted: bool = False):
    if len(lst) == 0:
        return None
    if not sorted:
        lst.sort()
    return round(lst[len(lst) - 1] - lst[0], 2)


# returns standard deviation, None if list empty
def standard_deviation_from_list(lst: list):
    if len(lst) == 0:
        return None
    # https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step
    mean = avg_from_list(lst)
    summation = 0
    for obj in lst:
        summation += (obj - mean) ** 2
    # return round(math.sqrt(summation / (len(lst) - 1)), 2)
    return round(math.sqrt(summation / (len(lst))), 2)


# returns list of valid areas of triangles that can be made by a list of points
def area_list_maker(points: list[tuple[int, int]]):
    areas = []
    sz = len(points)
    for i in range(sz):
        for j in range(i + 1, sz):
            for k in range(j + 1, sz):
                side_a = calc_distance(points[i], points[j])
                side_b = calc_distance(points[i], points[k])
                side_c = calc_distance(points[k], points[j])
                tmp = area_triangle(side_a, side_b, side_c)
                if tmp != 0:
                    areas.append(tmp)
    return areas
