# This file is to model the bus system for Charlottesville, or more specifically UVA.
# I am starting by just trying to set up the map.

# Temp dummy weight
weight = 0
# Gonna go from 14th street to 57th street for now, because it is very regularly spaces without any diagonal streets
bus_stops = {
    "34A" : [(9, 42, weight), (9, 40, weight), (9, 34, weight), (8, 34, weight), (7, 34, weight), (6, 34, weight), 
     (5, 34, weight), (4, 34, weight), (3, 34, weight), (2, 34, weight)]
}
