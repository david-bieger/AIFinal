# This file is to model the bus system for Charlottesville, or more specifically UVA.
# I am starting by just trying to set up the map.

# Temp dummy weight
weight = 0

intersections = {
    ("Main", "10th", "E"): [("Main", "JPA", "E", weight), ("JPA", "Main", "S", weight)],
    ("Main", "JPA", "E"): [("Main", "14th", "E", weight), ("14th", "Main", "N", weight)],
    ("Main", "14th", "E"): [("Main", "Rugby", "E", weight), ("Rugby", "Main", "N", weight)],
    ("Main", "Rugby", "E"): [("Main", "Emmet", "E", weight), ("Emmet", "Main", "S", weight), ("Emmet", "Main", "N", weight)],
    ("Main", "Emmet", "E"): [("Main", "Alderman", "E", weight), ("Alderman", "Main", "S", weight)],
    ("Alderman", "Emmet", "W"): [("Alderman", "JPA", "W", weight), ("JPA", "Alderman", "E", weight)],
    ("Alderman", "JPA", "E"): [("Alderman", "14th", "E", weight), ("14th", "Alderman", "W", weight)],
    ("14th", "Alderman", "W"): [("14th", "University", "W", weight), ("University", "14th", "E", weight)],
    ("14th", "University", "E"): [("14th", "McCormick", "E", weight), ("McCormick", "14th", "W", weight)],
    ("McCormick", "14th", "W"): [("McCormick", "JPA", "W", weight), ("JPA", "McCormick", "E", weight)],
    ("Grady", "Emmet", "E"): [("Grady", "Alderman", "E", weight), ("Alderman", "Grady", "W", weight)],
    ("Grady", "Alderman", "W"): [("Grady", "JPA", "W", weight), ("JPA", "Grady", "E", weight)],
    ("Gordon", "McCormick", "E"): [("Gordon", "Alderman", "E", weight), ("Alderman", "Gordon", "W", weight)],
    ("Gordon", "Alderman", "W"): [("Gordon", "14th", "W", weight), ("14th", "Gordon", "E", weight)],
    ("Culbreth", "University", "E"): [("Culbreth", "Alderman", "E", weight), ("Alderman", "Culbreth", "W", weight)],
    ("Culbreth", "Alderman", "W"): [("Culbreth", "Rugby", "W", weight), ("Rugby", "Culbreth", "E", weight)],
    # Add more intersections as needed
}

