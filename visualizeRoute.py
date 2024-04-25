import matplotlib.pyplot as plt

def visualize_route(path):
    fig, ax = plt.subplots(figsize=(12, 12))
    grid_size = max(max(x[0], x[1]) for x in path) + 1  
    
    
    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))
    ax.grid(True)
    
   
    last_pos = None
    last_direction = None

    for i in range(len(path) - 1):
        start = path[i]
        end = path[i + 1]
        
       
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        current_direction = None
        if dx > 0:
            current_direction = 'E'
        elif dx < 0:
            current_direction = 'W'
        elif dy > 0:
            current_direction = 'N'
        elif dy < 0:
            current_direction = 'S'

        
        ax.arrow(start[0], start[1], dx, dy, head_width=0.1, head_length=0.2, fc='blue', ec='blue')
        
       
        if last_direction and current_direction and last_direction != current_direction:
            turn_label = ""
            
            if (last_direction, current_direction) in [('N', 'E'), ('E', 'S'), ('S', 'W'), ('W', 'N')]:
                turn_label = "R" 
            elif (last_direction, current_direction) in [('N', 'W'), ('W', 'S'), ('S', 'E'), ('E', 'N')]:
                turn_label = "L"  

            if turn_label:
                ax.text(start[0], start[1], turn_label, color='darkorange', fontsize=14, ha='center', va='center', fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', pad=2))

        
        last_direction = current_direction
        last_pos = start
    
    numStop = 0
    for idx, pos in enumerate(path):
        if len(pos) == 2 or (len(pos) > 2 and pos[2] is None):  
            ax.plot(pos[0], pos[1], 'ro')  
            ax.text(pos[0], pos[1], f'Stop {numStop}', color='black', fontsize=10, ha='right', va='bottom', fontweight='bold')
            numStop += 1

    ax.set_xlim([-1, grid_size])
    ax.set_ylim([-1, grid_size])
    ax.set_aspect('equal')
    ax.set_title('Visualization of Path with Directions, Stops, and Turns')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()


