import utils
import environment

#Breadth-First Search (BFS)
def breadthFirstSearch(grid, startNode, goalNode):
    """
    Perform Breadth-First Search on the grid.
    Returns the path found and the number of nodes expanded.
    """
    #Queue storing tuples of (currentNode, pathTaken)
    queue = [(startNode, [startNode])]
    visitedNodes = {startNode}
    nodesExpanded = 0

    while len(queue) > 0:
        nodesExpanded += 1
        currentPosition, path = queue.pop(0)

        #If goal is reached return path
        if currentPosition == goalNode:
            return path, nodesExpanded

        #Explore neighbors
        for neighbor in environment.get_neighbors(currentPosition):
            if environment.is_valid_move(grid, neighbor) and neighbor not in visitedNodes:
                visitedNodes.add(neighbor)
                newPath = list(path)
                newPath.append(neighbor)
                queue.append((neighbor, newPath))

    #If no path found
    return None, nodesExpanded


#Uniform-Cost Search (UCS)
def uniformCostSearch(grid, startNode, goalNode):
    """
    Perform Uniform-Cost Search on the grid.
    Returns the path, total cost, and number of nodes expanded.
    """
    #Priority queue (list sorted by cost)
    frontier = [(0, startNode, [startNode])]
    visitedNodes = set()
    nodesExpanded = 0

    while len(frontier) > 0:
        #Expand the node with the smallest cost
        frontier.sort()
        currentCost, currentPosition, path = frontier.pop(0)
        nodesExpanded += 1

        if currentPosition in visitedNodes:
            continue

        visitedNodes.add(currentPosition)

        #Goal check
        if currentPosition == goalNode:
            return path, currentCost, nodesExpanded

        #Expand neighbors
        for neighbor in environment.get_neighbors(currentPosition):
            if environment.is_valid_move(grid, neighbor) and neighbor not in visitedNodes:
                moveCost = environment.get_terrain_cost(grid, neighbor)
                newCost = currentCost + moveCost
                newPath = list(path)
                newPath.append(neighbor)
                frontier.append((newCost, neighbor, newPath))

    #If no path found
    return None, 0, nodesExpanded

#A* Search (AStar)
def aStarSearch(grid, startNode, goalNode, dynamicObstacle, timeOffset=0):
    """
    Perform A* Search on the grid.
    Considers dynamic obstacles with timeOffset for obstacle movements.
    Returns the path, total cost, and number of nodes expanded.
    """
    costFromStart = 0
    heuristic = utils.manhattan_distance(startNode, goalNode)
    totalCost = costFromStart + heuristic

    frontier = [(totalCost, costFromStart, startNode, [startNode])]
    visitedNodes = set()
    nodesExpanded = 0

    while len(frontier) > 0:
        frontier.sort()
        _, currentCost, currentPosition, path = frontier.pop(0)
        nodesExpanded += 1

        if currentPosition in visitedNodes:
            continue

        visitedNodes.add(currentPosition)

        #Goal check
        if currentPosition == goalNode:
            return path, currentCost, nodesExpanded

        #Current time based on path length + offset
        currentTime = len(path) - 1 + timeOffset

        #Explore neighbors
        for neighbor in environment.get_neighbors(currentPosition):
            isSafe = environment.is_safe_at_time(neighbor, currentTime + 1, dynamicObstacle)

            if environment.is_valid_move(grid, neighbor) and neighbor not in visitedNodes and isSafe:
                moveCost = environment.get_terrain_cost(grid, neighbor)
                newCostFromStart = currentCost + moveCost
                newHeuristic = utils.manhattan_distance(neighbor, goalNode)
                newTotalCostEstimated = newCostFromStart + newHeuristic

                newPath = list(path)
                newPath.append(neighbor)
                frontier.append((newTotalCostEstimated, newCostFromStart, neighbor, newPath))

    #If no path found
    return None, 0, nodesExpanded


# Dynamic Simulation
def runDynamicSimulation(grid, startNode, goalNode, dynamicObstacle):
    """
    Runs a simulation in a dynamic environment.
    The agent replans at each time step using A*.
    Handles waiting if an obstacle blocks the next step.
    """
    agent = startNode
    fullPath = [startNode]
    totalCostAccumulated = 0
    nodesExpanded = 0
    timeStep = 0

    print("\nStarting dynamic simulation...")

    while agent != goalNode:
        #Plan a path at the current time step
        pathSegment, costSegment, expandedNow = aStarSearch(grid, agent, goalNode, dynamicObstacle, timeOffset=timeStep)
        nodesExpanded += expandedNow

        if not pathSegment:
            print(f"time {timeStep:02d} | no path found from {agent}, agent is stuck.")
            return None, totalCostAccumulated, nodesExpanded

        #Next move in the path
        nextStep = pathSegment[1]

        if not environment.is_safe_at_time(nextStep, timeStep + 1, dynamicObstacle):
            print(f"time {timeStep:02d} | obstacle detected at {nextStep}, agent waits at {agent}.")
            timeStep += 1
            continue

        #Move agent forward
        timeStep += 1
        moveCost = environment.get_terrain_cost(grid, nextStep)
        totalCostAccumulated += moveCost
        agent = nextStep
        fullPath.append(agent)

        print(f"time {timeStep:02d} | agent moved to {agent}. total Cost: {totalCostAccumulated}")

    print("\nGoal reached!")
    return fullPath, totalCostAccumulated, nodesExpanded
