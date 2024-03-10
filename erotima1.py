import statistics
import utils


n_pts = 100
points = []
for i in range(n_pts):
    points.append(utils.rnd_point())

areas = utils.area_list_maker(points)

print("---------------------------------------------")
print(f"Valid triangles: {len(areas)}")
print("---------------------------------------------")
print("Statistics module")
print(f"Mean: {statistics.mean(areas):.2f}")
print(f"Median: {statistics.median(areas):.2f}")
print(f"Standard deviation: {statistics.stdev(areas):.2f}")
print("---------------------------------------------")
print("Utils module")
print(f"Mean: {utils.avg_from_list(areas)}")
print(f"Median: {utils.median_from_list(areas)}")
# auto edw bgazei diaforetikh timh apo to stdev() epeidh prepei na pernaei ta unit tests
# kai to stdev xrhshmopoiei allon tupo, (n - 1) anti gia n
print(f"Standard deviation: {utils.standard_deviation_from_list(areas)}")
print("---------------------------------------------")
