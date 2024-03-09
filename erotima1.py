import statistics
import utils
# from itertools import combinations as comb


n_pts = 100
points = []
areas = []
for i in range(n_pts):
    points.append(utils.rnd_point())

#  for point in comb(points, 3):
#      print(point)

for i in range(n_pts):
    for j in range(i+1, n_pts):
        for k in range(j+1, n_pts):
            side_a = utils.calc_distance(points[i], points[j])
            side_b = utils.calc_distance(points[j], points[k])
            side_c = utils.calc_distance(points[k], points[i])
            tmp = utils.area_triangle(side_a, side_b, side_c)
            if  tmp != 0:
                areas.append(tmp)
print("---------------------------------------------")
print(f'Valid triangles: {len(areas)}')
print("---------------------------------------------")
print("Statistics module")
print(f'Mean: {statistics.mean(areas)}')
print(f'Median: {statistics.median(areas)}')
print(f'Standard deviation: {statistics.stdev(areas)}')
print("---------------------------------------------")
print("Utils module")
print(f'Mean: {utils.avg_from_list(areas)}')
print(f'Median: {utils.median_from_list(areas)}')
print(f'Standard deviation: {utils.standard_deviation_from_list(areas)}')
print("---------------------------------------------")

