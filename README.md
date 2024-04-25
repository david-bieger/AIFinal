# AIFinal

format intersections like 

intersections = {
    (Rugby, Grady, E): [((Rugby, Culbreth, E), weight), ... ]
    (rugby, grady, W)
}

Focus on general area around red line, including red line stops.

where this means i am traveling east on rugby at the rugby grady intersection. If i go straight, i end up traveling east on rugby at the rugby/culbreth intersection. That takes weight amount of time. Do this for straight, right, and left for each intersection along our bus route. Stops will be 