from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from django.http import JsonResponse
import shapely.geometry as shp
import matplotlib.pyplot
from sqlalchemy import case
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
from io import BytesIO
import base64, urllib

#create random polygon
from . import random_polygon

vertices = random_polygon.vertices

@csrf_exempt

def index(request):

    return render(
        request,"geoplanner_app/index.html", {
            "test": "test",
        })

@csrf_exempt
def calculate(request):
    post_data = json.loads(request.body.decode("utf-8"))
    coordinates = post_data['coordinates']

    # NICO HERE ARE THE INPUTS FOR PROJECT CLASS AND SOIL CLASS FROM THE FRONT END
    project_class = post_data['project_class']
    soil_class = post_data['soil_class']
    print(project_class)
    print(soil_class)

    # obtain polygon bounds
    polygon = shp.Polygon(coordinates)
    latmin, lonmin, latmax, lonmax = polygon.bounds


    #set resolution for sampling
    from . import data

    def define_project_class(project_class):
        if project_class == "C1":
            return data.construction_classes[0]['distance_coefficient']
        elif project_class == "C2":
            return data.construction_classes[1]['distance_coefficient']
        elif project_class == "C3":
            return data.construction_classes[2]['distance_coefficient']
        elif project_class == "C4":
            return data.construction_classes[3]['distance_coefficient']
        elif project_class == "C5":
            return data.construction_classes[4]['distance_coefficient']
        elif project_class == "C6":
            return data.construction_classes[5]['distance_coefficient']
        elif project_class == "C7":
            return data.construction_classes[6]['distance_coefficient']
        elif project_class == "C8":
            return data.construction_classes[7]['distance_coefficient']
        else:
            return "Error"
    
    def define_variability(soil_type):
        if soil_type == "Low variability":
            return data.variability_types[0]['distance']
        elif soil_type == "Medium variability":
            return data.variability_types[1]['distance']
        elif soil_type == "High variability":
            return data.variability_types[2]['distance']
    
    #The project class should be taken from the user input
    
    resolution = define_project_class("C5") * define_variability("High variability")

    # construct a rectangular mesh

    points = []
    for lat in np.arange(latmin, latmax, resolution):
        for lon in np.arange(lonmin, lonmax, resolution):
            points.append(shp.Point((round(lat,4), round(lon,4))))

    #define buffered polygon

    buffered_polygon = polygon.buffer(-2)

    # validate if each point falls inside polygon

    i = 0
    valid_points = []
    while i < len(points):
        valid = points[i].within(buffered_polygon)
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
        'xs':xs,        
        'ys':ys,
        'result1':result1,
        'result2':result2,
        'result3':result3,
        'result4':result4,
        }, safe=False)






