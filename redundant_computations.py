import math

def calculate_areas(radii):
    areas = []
    for radius in radii:
        area = math.pi * radius * radius
        areas.append(area)
    return areas

radii = [1, 2, 3, 4, 5]
circle_areas = calculate_areas(radii)
