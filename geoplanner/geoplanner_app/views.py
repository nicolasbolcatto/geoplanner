from django.shortcuts import render
import orjson as json
from django.http import JsonResponse
import shapely.geometry as shp
import matplotlib.pyplot
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
from io import BytesIO
import base64, urllib

#create random polygon
from . import random_polygon

vertices = random_polygon.vertices



def index(request):

    return render(
        request,"geoplanner_app/index.html", {
            "test": "test",
        })

def calculate(request):
    post_data = json.loads(request.body.decode("utf-8"))
    coordinates = post_data['coordinates']


    # obtain polygon bounds

    polygon = shp.Polygon(coordinates)
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

    print(valid_points)

    x,y = polygon.exterior.xy
    plt.clf() 
    plt.plot(x,y)
    xs = [point.x for point in valid_points]
    ys = [point.y for point in valid_points]
    plt.scatter(xs, ys)

    buffer_display = BytesIO()
    plt.savefig(buffer_display, format='png')
    buffer_display.seek(0)
    graphic_display = base64.b64encode(buffer_display.read())
    json_display = urllib.parse.quote(graphic_display)


    result1 = 'result1'
    result2 = 'result1'
    result3 = 'result1'
    result4 = 'result1'


    return JsonResponse({
        'json_display':json_display,
        'result1':result1,
        'result2':result2,
        'result3':result3,
        'result4':result4,
        }, safe=False)






