import unittest
import utils

points = []
areas = []


def f1():
    with open("points.txt", "r") as file:
        for line in file:
            x, y = line.split()
            points.append((int(x), int(y)))
    return utils.area_list_maker(points)


class TriangularTesting(unittest.TestCase):
    def test(self):
        areas = f1()
        self.assertEqual(len(areas), 161671)
        self.assertEqual(utils.avg_from_list(areas), 3206.86)
        self.assertEqual(utils.median_from_list(areas), 2392.50)
        self.assertEqual(utils.standard_deviation_from_list(areas), 2843.23)


if __name__ == "__main__":
    unittest.main()
