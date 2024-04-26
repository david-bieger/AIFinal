# This file will handle the secondary agents that exist in the environment. They can be considered busses or even traffic as a whole.
# Basically, each street (vertical and horizontal) will have an agent that goes back and forth. The primary agent will avoid
# being directly behind an agent on the same street.

import random
import synthetic

# format of each secondary agent in the list [x_position, y_position, direction]
#synthetic data set for turns
import random 
from itertools import permutations
from visualizeRoute import visualize_route

#NOTE: If you want to change parameters, change them in get_cost function

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


def goal_test(cur_pos, next_stop):
    return cur_pos[0] == next_stop[0] and cur_pos[1] == next_stop[1]

def actions(pos, grid_size=15, right=1, left=3):
    # returns ((new x, new y, new direction), weight)
    straight = 1
    x, y = pos[0], pos[1]
    direction = "N"
    if len(pos) >= 3: direction = pos[2]
    #print("pos: " + str(pos))

    # List to store possible actions
    possible_actions = []

    # Handling actions for direction North (N)
    if direction == "N":
        if y > 0:  # Boundary check for moving North
            possible_actions.append(((x, y + 1, "N"), straight))
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
            possible_actions.append(((x, y - 1, "S"), straight))
        if x > 0:  # Boundary check for moving West
            possible_actions.append(((x - 1, y, "W"), right))
        if x < grid_size - 1:  # Boundary check for moving East
            possible_actions.append(((x + 1, y, "E"), left))

    return possible_actions


def add_to_priority_queue(q, priority, pos):
    q.append((priority, pos))
    q.sort()
    return q

def A_star(start, end, grid_size, right, left, traffic):
    q = []
    q = add_to_priority_queue(q, 0, start)  # Initialize the priority queue
    cost = {}
    parent = {start: None}
    steps = {start: 0}
    cost[start] = 0
    if len(start) >= 3: 
        prev_direction = start[2]  # Track previous direction
    else: 
        prev_direction = "N" #hard code a start facing north
    while len(q) > 0:
        cur_pos = q.pop(0)[1]  # Pop the item with the lowest priority
        temp_traffic = incrementTraffic[traffic, grid_size, grid_size, steps[cur_pos]]
        if goal_test(cur_pos, end):
            end = (end[0], end[1], cur_pos[2])
            break
        for action in actions(cur_pos, grid_size, right, left):
            next_pos, weight = action
            new_cost = cost[cur_pos] + weight

            # Track the previous direction when switching start and end nodes
            if next_pos[0:2] == end[0:2]:
                next_pos = (next_pos[0], next_pos[1], prev_direction)

            if next_pos not in cost:
                cost[next_pos] = new_cost
                parent[next_pos] = cur_pos
                steps[next_pos] = steps[cur_pos]+1
                priority = new_cost + h(next_pos, end, temp_traffic)
                q = add_to_priority_queue(q, priority, next_pos)  # Push tuple to priority queue
                prev_direction = next_pos[2] if len(next_pos) >= 3 else prev_direction  # Update direction
            
            if new_cost < cost[next_pos]:
                cost[next_pos] = new_cost
                priority = new_cost + h(next_pos, end, temp_traffic)
                q = add_to_priority_queue(q, priority, next_pos)  # Push tuple to priority queue
                prev_direction = next_pos[2] if len(next_pos) >= 3 else prev_direction  # Update direction
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()

    return cost[end], path



def get_optimal_route(stops, grid_size = 9, num_stops = 5, left = 3, right = 1, straight = 1):
    
    routes = get_stop_combinations(stops)
    path_taken_for_routes = []
    route_number = 0
    route_cost = []
    traffic = create_secondary_agents(9, 9)
    for route in routes:
        path_cost = 0
        full_path = []
        for i in range(len(route) - 1):
            stop = route[i]
            #print("stop" + str(stop))
            next_stop = route[i + 1]
            #print("next stop: " + str(next_stop))
            cost, path = A_star(stop, next_stop, grid_size, right, left, traffic)
            path_cost += cost
            full_path.extend(path[:-1])
            traffic = incrementTraffic(traffic, grid_size, grid_size, len(path))
        full_path.append(route[-1])
        path_taken_for_routes.append(full_path)
        route_cost.append(path_cost)
        route_number += 1
    optimal_route_index = route_cost.index(min(route_cost))
    return (routes[optimal_route_index], route_cost[optimal_route_index], path_taken_for_routes[optimal_route_index])
    

def get_costs():
    #variables that can change based on desired parameters
    
    #unweighted_cost * 3 should = right+left+straight for accurate results
    unweighted_cost = 10
    right_weight = 5
    straight_weight = 7
    left_weight = 18

    grid_size = 9
    num_stops = 5

    stops = []
    stops = get_stops(stops, grid_size, num_stops)
    #print("\nstops: " + str(stops) + "\n")

    unweighted_route, cost_of_unweighted, path_taken_for_optimal_unweighted_route = get_optimal_route(stops, grid_size, num_stops, unweighted_cost, unweighted_cost, unweighted_cost)
    weighted_route, cost_of_weighted, path_taken_for_optimal_weighted_route = get_optimal_route(stops, grid_size, num_stops, left_weight, right_weight, straight_weight)

    # print("stops:", weighted_route)
    # print( "path taken to stops:", path_taken_for_optimal_weighted_route)
    # print("path of unweighted: " + str(unweighted_route))
    # print("cost of unweighted: " + str(cost_of_unweighted) + "\n")
    # print("cost of weighted: " + str(cost_of_weighted))
    # print("path of weighted: " + str(weighted_route) + "\n")
    # print("Prioritizing right turns took " + str(0.01 * float(int(10000*float(cost_of_weighted)/float(cost_of_unweighted)))) + "% of the time of counting them the same.\n")
    return (cost_of_unweighted, path_taken_for_optimal_unweighted_route, cost_of_weighted, path_taken_for_optimal_weighted_route, weighted_route)


def loop_for_average(times = 10):
    unweighted_total, weighted_total = 0, 0
    min_weighted_cost = float('inf')
    best_weighted_path = None
    route_with_least_cost = []
    for i in range(times):
        cost_of_unweighted, unweighted_path, cost_of_weighted, weighted_path, weighted_route = get_costs()
        unweighted_total += cost_of_unweighted
        weighted_total += cost_of_weighted
    
    
        if cost_of_weighted < min_weighted_cost:
            min_weighted_cost = cost_of_weighted
            best_weighted_path = weighted_path
            route_with_least_cost = weighted_route

    weighted_avg = weighted_total / times
    unweighted_avg = unweighted_total / times

    magic_percent = 0.01 * float(int(10000*float(weighted_avg)/float(unweighted_avg))) #messed with ints and floats to round it to 2 decimal places
    
    print("\nunweighted average cost for " + str(times) + " times: " + str(unweighted_avg) + "\n")
    print("weighted average cost for " + str(times) + " times: " + str(weighted_avg) + "\n")
    print("Prioritizing right turns took " + str(magic_percent) + "% of weighing right and left turns equally.\n")
    return (best_weighted_path, route_with_least_cost)



def create_secondary_agents(x_grid, y_grid):
    secondary_agents = []

    for i in range(x_grid):
        if random.randint(0,1) == 0:
            rand_direction = "N"
        else:
            rand_direction = "S"

        new_agent = [i, random.randint(0, y_grid-1), rand_direction]

        secondary_agents.append(new_agent)
    
    for j in range(y_grid):
        if random.randint(0,1) == 0:
            rand_direction = "E"
        else:
            rand_direction = "W"

        new_agent = [random.randint(0, x_grid-1), j, rand_direction]

        secondary_agents.append(new_agent)

    for agent in secondary_agents:
        agent[2] = check_at_edge(agent, x_grid, y_grid)

    return secondary_agents

def check_at_edge(agent, grid_x, grid_y):
    direction = agent[2]

    if (direction == "N") | (direction == "S"):
        position = agent[1]
        if direction == "N":
            if position == grid_y-1:
                direction = "S"
        else:
            if position == 0:
                direction = "N"
    else:
        position = agent[0]
        if direction == "E":
            if position == grid_x-1:
                direction = "W"
        else:
            if position == 0:
                direction = "E"

    return direction
    

def incrementTraffic(current_state, grid_x, grid_y, num_steps):
    for agent in current_state:
        for i in range(num_steps):
            if (agent[2] == "N") | (agent[2] == "S"):
                if agent[2] == "N":
                    new_position = agent[1] + 1
                    agent[1] = new_position
                    if new_position == grid_y-1:
                        agent[2] = "S"
                else:
                    new_position = agent[1] - 1
                    agent[1] = new_position
                    if new_position == 0:
                        agent[2] = "N"
            else:
                if agent[2] == "E":
                    new_position = agent[0] + 1
                    agent[0] = new_position
                    if new_position == grid_x-1:
                        agent[2] = "W"
                    
                else:
                    new_position = agent[0] - 1
                    agent[0] = new_position
                    if new_position == 0:
                        agent[2] = "E"
    
    return current_state

def isTraffic(pos, traffic):
    # Check our direction
    if pos[2] == "N":
        #Check bus on our street
        bus = agents[pos[0]]
        # If bus is going same direction and is in front of us, take manhattan distance.
        if bus[2] == "N" and bus[1] >= pos[1]:
            # Negative manhattan distance for deincentivization
            return bus[1] - pos[1]
    elif pos[2] == "S":
        bus = agents[pos[0]]
        if bus[2] == "S" and bus[1] <= pos[1]:
            return pos[1] - bus[1]
    elif pos[2] == "E":
        bus = agents[pos[1] + grid_size]
        if bus[2] == "E" and bus[0] >= pos[0]:
            return bus[0] - pos[0]
    elif pos[2] == "W":
        bus = agents[pos[1]+grid_size]
        if bus[2] == "W" and bus[0] <= pos[0]:
            return pos[0] - bus[0]
    return None

grid_size = 9
def h(cur_pos, next_stop, traffic):
    #manhattan distance here
    traffic_cost = 0
    dx = abs(cur_pos[0] - next_stop[0])
    dy = abs(cur_pos[1] - next_stop[1])
    if isTraffic(cur_pos, traffic) != None:
        traffic_cost = (-isTraffic(cur_pos, traffic)+grid_size)
    return dx + dy + traffic_cost
