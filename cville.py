# This file is to model the bus system for Charlottesville, or more specifically UVA.
# I am starting by just trying to set up the map.

# Temp dummy weight
weight = 0

#hard code weights
#bus stop looks like ("Main", "Bus Stop", "E")


intersections = {
    ("Main", "10th", "E"):[("Main", "JPA", "E", weight), ("JPA", "Main", "S", weight)],
    ("Main", "JPA", "E"):[("Main", "14th", "E", weight), ("14th", "Main", "N", weight)],
    ("Main", "14th", "E"):[("Main", "Rugby", "E", weight), ("Rugby", "Main", "N", weight)],
    ("Main", "Rugby", "E"):[("Main", "Emmet", "E", weight), ("Emmet", "Main", "S", weight), ("Emmet", "Main", "N", weight)]
    
}

