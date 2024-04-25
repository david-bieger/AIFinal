# This file is to model the bus system for Charlottesville, or more specifically UVA.
# I am starting by just trying to set up the map.

# Temp dummy weight
weight = 0
# Gonna go from 14th street to 57th street for now, because it is very regularly spaces without any diagonal streets
bus_stops = {
    "34A" : [(9, 42, weight), (9, 40, weight), (9, 34, weight), (8, 34, weight), (7, 34, weight), (6, 34, weight), 
             (5, 34, weight), (4, 34, weight), (3, 34, weight), (2, 34, weight)],
    "12" : [(8, 12, weight), (8, 14, weight), (9, 14, weight), (10, 14, weight), (11, 15, weight), (11, 18, weight), 
             (11, 24, weight), (12, 27, weight), (12, 30, weight), (12, 33, weight), (12, 40, weight), (12, 43, weight), 
             (12, 46, weight), (12, 48, weight), (12, 52, weight), (12, 55, weight), (11, 57, weight), (10, 57, weight), 
             (9, 57, weight), (8, 57, weight), (7, 58, weight)],
    "57" : [(10, 72, weight), (11, 72, weight), (11, 69, weight), (11, 66, weight), (11, 64, weight), (11, 61, weight), 
            (11, 59, weight), (11, 57, weight), (10, 57, weight), (9, 57, weight), (8, 57, weight), (7, 57, weight), 
            (6, 57, weight), (5, 57, weight), (4.6, 57, weight), (3.6, 57, weight), (3, 57, weight), (2, 57, weight), 
            (1, 57, weight), (0, 57, weight), (0, 55, weight), (1, 55, weight)],
    
}
