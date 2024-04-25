# This file will handle the secondary agents that exist in the environment. They can be considered busses or even traffic as a whole.
# Basically, each street (vertical and horizontal) will have an agent that goes back and forth. The primary agent will avoid
# being directly behind an agent on the same street.

import random

# format of each secondary agent in the list [x_position, y_position, direction]

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
    

def incrementTraffic(current_state, grid_x, grid_y):

    for agent in current_state:
        # agent[2] = check_direction_change(agent, grid_x, grid_y)

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



agents = create_secondary_agents(5, 5)
print(agents)
incrementTraffic(agents, 5, 5)
print(agents)
incrementTraffic(agents, 5, 5)
print(agents)
