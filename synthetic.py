#synthetic data set for turns
import random 
import heapq
from itertools import permutations

def get_stop_combinations(stops):
    # Generate all permutations of the stops
    stop_permutations = permutations(stops)
    # Convert permutations to lists and return as a list of lists
    return [list(permutation) for permutation in stop_permutations]

def get_stops(stops, grid_size, num_stops):
    new_stop = (0, 0)
    for i in range(num_stops):
        while new_stop in stops or (new_stop[0] == 0 and new_stop[1] == 0):
            new_stop = (random.randint(1, grid_size - 1), random.randint(1, grid_size - 1))
        stops.append(new_stop)        
    return stops


def h(cur_pos, next_stop):
    #manhattan distance here
    dx = abs(cur_pos[0] - next_stop[0])
    dy = abs(cur_pos[1] - next_stop[1])
    return dx + dy

def goal_test(cur_pos, next_stop):
    return cur_pos[0] == next_stop[0] and cur_pos[1] == next_stop[1]

def actions(pos, grid_size=15, right=1, left=3):
    # returns ((new x, new y, new direction), weight)
    straight = 1
    x, y = pos[0], pos[1]
    direction = "N"
    if len(pos) >= 3: direction = pos[2]
    print("pos: " + str(pos))

    # List to store possible actions
    possible_actions = []

    # Handling actions for direction North (N)
    if direction == "N":
        if y > 0:  # Boundary check for moving North
            possible_actions.append(((x, y - 1, "N"), straight))
        if x < grid_size - 1:  # Boundary check for moving East
            possible_actions.append(((x + 1, y, "E"), right))
        if x > 0:  # Boundary check for moving West
            possible_actions.append(((x - 1, y, "W"), left))

    # Handling actions for direction East (E)
    elif direction == "E":
        if x < grid_size - 1:  # Boundary check for moving East
            possible_actions.append(((x + 1, y, "E"), straight))
        if y > 0:  # Boundary check for moving South
            possible_actions.append(((x, y - 1, "S"), right))
        if y < grid_size - 1:  # Boundary check for moving North
            possible_actions.append(((x, y + 1, "N"), left))

    # Handling actions for direction West (W)
    elif direction == "W":
        if x > 0:  # Boundary check for moving West
            possible_actions.append(((x - 1, y, "W"), straight))
        if y < grid_size - 1:  # Boundary check for moving North
            possible_actions.append(((x, y + 1, "N"), right))
        if y > 0:  # Boundary check for moving South
            possible_actions.append(((x, y - 1, "S"), left))

    # Handling actions for direction South (S)
    elif direction == "S":
        if y < grid_size - 1:  # Boundary check for moving South
            possible_actions.append(((x, y + 1, "S"), straight))
        if x > 0:  # Boundary check for moving West
            possible_actions.append(((x - 1, y, "W"), right))
        if x < grid_size - 1:  # Boundary check for moving East
            possible_actions.append(((x + 1, y, "E"), left))

    return possible_actions


def add_to_priority_queue(q, priority, pos):
    q.append((priority, pos))
    q.sort()
    return q

def A_star(start, end, grid_size, right, left):
    q = []
    q = add_to_priority_queue(q, 0, start)  # Initialize the priority queue
    cost = {}
    cost[start] = 0
    if len(start) >= 3: prev_direction = start[2]  # Track previous direction
    else: prev_direction = "N" #hard code a start facing north
    while len(q) > 0:
        cur_pos = q.pop(0)[1]  # Pop the item with the lowest priority
        if goal_test(cur_pos, end):
            break
        for action in actions(cur_pos, grid_size, right, left):
            next_pos, weight = action
            new_cost = cost[cur_pos] + weight

            # Track the previous direction when switching start and end nodes
            if next_pos[0:2] == end[0:2]:
                next_pos = (next_pos[0], next_pos[1], prev_direction)

            if next_pos not in cost or new_cost < cost[next_pos]:
                cost[next_pos] = new_cost
                priority = new_cost + h(next_pos, end)
                q = add_to_priority_queue(q, priority, next_pos)  # Push tuple to priority queue
                if len(cur_pos) >= 3: prev_direction = cur_pos[2]  # Update previous direction

    return cost[end]



def get_optimal_route():
    grid_size = 15
    num_stops = 10
    stops = []
    right = 1 #weight of a right turn
    left = 3 #weight of a left turn
    stops = get_stops(stops, grid_size, num_stops)
    print("stops: " + str(stops))
    routes = get_stop_combinations(stops)
    route_number = 0
    route_cost = []
    for route in routes:
        path_cost = 0
        for i in range(len(route) - 1):
            stop = route[i]
            next_stop = route[i + 1]
            path_cost += A_star(stop, next_stop, grid_size, right, left)
        route_cost.append(path_cost)
        route_number += 1
    optimal_route_index = route_cost.index(min(route_cost))
    return routes[optimal_route_index]
    

get_optimal_route()