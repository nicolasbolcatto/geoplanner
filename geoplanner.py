
import shapely.geometry as shp
import matplotlib.pyplot as plt
import numpy as np

#create random polygon

from random_polygon import vertices

# obtain polygon bounds

polygon = shp.Polygon(vertices)
latmin, lonmin, latmax, lonmax = polygon.bounds

#set resolution for sampling

resolution = 20

# construct a rectangular mesh

points = []
for lat in np.arange(latmin, latmax, resolution):
    for lon in np.arange(lonmin, lonmax, resolution):
        points.append(shp.Point((round(lat,4), round(lon,4))))

# validate if each point falls inside polygon

i = 0
valid_points = []
while i < len(points):
    valid = points[i].within(polygon)
    if valid:
        valid_points.append(points[i])
    i += 1

# plot points and polygon

x,y = polygon.exterior.xy
plt.plot(x,y)
xs = [point.x for point in valid_points]
ys = [point.y for point in valid_points]
plt.scatter(xs, ys)
plt.show()