import time
import environment
import algorithms
import utils

#Global variables to store current settings
mapFile = "maps/dynamic.txt"
selectedAlgorithm = "astar"

def run_algorithm():
    global mapFile, selectedAlgorithm 

    print("-" * 25)
    print(f"Map chosen: {mapFile}")

    grid, dynamicObstacle, startNode, goalNode = environment.load_map_data(mapFile)

    if not startNode or not goalNode:
        print("[!] Map file has an error (start 'S' or goal 'G' not found).")
        return

    print(f"Start: {startNode}")
    print(f"Goal Node: {goalNode}")
    print(f"Algorithm selected: {selectedAlgorithm.upper()}")
    print("*" * 25)
    startTime = time.time()

    finalPath = None
    finalCost = 0
    noOfNodesExpanded = 0

    #Setting the algorithm used
    if selectedAlgorithm == "bfs":
        finalPath, noOfNodesExpanded = algorithms.breadthFirstSearch(grid, startNode, goalNode)
        if finalPath:
            finalCost = len(finalPath) - 1
    elif selectedAlgorithm == "ucs":
        finalPath, finalCost, noOfNodesExpanded = algorithms.uniformCostSearch(grid, startNode, goalNode)
    elif selectedAlgorithm == "astar":
        finalPath, finalCost, noOfNodesExpanded = algorithms.aStarSearch(grid, startNode, goalNode, dynamicObstacle)
    elif selectedAlgorithm == "dynamic":
        if not dynamicObstacle:
            print("[!] Map has no dynamic obstacles, but proceeding with simulation.")
        finalPath, finalCost, noOfNodesExpanded = algorithms.runDynamicSimulation(grid, startNode, goalNode, dynamicObstacle)

    #Calculate execution time
    endTime = time.time()
    executionTime = endTime - startTime

    #Printing the final results
    print("\n--- Algorithm Results ---")
    if finalPath:
        print(f"Path taken: {' --> '.join(map(str, finalPath))}")
        print(f"Cost: {finalCost}")
        print(f"Nodes expanded: {noOfNodesExpanded}")
        print(f"Time taken to execute: {executionTime:.6f} seconds")
        print("\nPath on the grid:")
        utils.print_grid_with_path(grid, finalPath, startNode, goalNode)
    else:
        print("No path found.")
        print(f"Nodes expanded: {noOfNodesExpanded}")
        print(f"Time taken to complete: {executionTime:.6f} seconds")
    print("-" * 25)


def main_menu():
    print("24MIM10037 SUSMIT ROY")
    global mapFile, selectedAlgorithm 

    while True:
        print("\n" + "="*25)
        print("        MENU")
        print("="*25)
        print(f"Current Map: {mapFile}")
        print(f"Current Algorithm: {selectedAlgorithm.upper()}")
        print("-" * 25)
        print("1. Run Algorithm")
        print("2. Change Map")
        print("3. Change Algorithm")
        print("4. Exit")

        try:
            opt = input("Choose an option: ")
            if not opt: continue #if input is empty
            opt = int(opt)
        except ValueError:
            print("\n[!] Invalid input. Please enter a number (1-4).")
            continue

        if opt == 1:
            run_algorithm()
        elif opt == 2:
            print("\n+--- Select a Map ---+")
            print("1. Small")
            print("2. Medium")
            print("3. Large")
            print("4. Dynamic")
            try:
                map_choice = int(input("Enter map choice: "))
                if map_choice == 1:
                    mapFile = "maps/small.txt"
                elif map_choice == 2:
                    mapFile = "maps/medium.txt"
                elif map_choice == 3:
                    mapFile = "maps/large.txt"
                elif map_choice == 4:
                    mapFile = "maps/dynamic.txt"
                else:
                    print("[!] Invalid choice. Returning to main menu.")
            except ValueError:
                print("[!] Invalid input. Please enter a number.")
        elif opt == 3:
            print("\n+--- Select an Algorithm ---+")
            print("1. Uniform-Cost Search (UCS)")
            print("2. Breadth-First Search (BFS)")
            print("3. A* Search (AStar)")
            print("4. Dynamic Simulation")
            try:
                algo_choice = int(input("Enter algorithm choice: "))
                if algo_choice == 1:
                    selectedAlgorithm = "ucs"
                elif algo_choice == 2:
                    selectedAlgorithm = "bfs"
                elif algo_choice == 3:
                    selectedAlgorithm = "astar"
                elif algo_choice == 4:
                    selectedAlgorithm = "dynamic"
                else:
                    print("[!] Invalid choice. Returning to main menu.")
            except ValueError:
                print("[!] Invalid input. Please enter a number.")
        elif opt == 4:
            print("Exiting program.")
            break
        else:
            print("\n[!] Invalid option. Please choose a number from 1 to 4.")

#Entry point of the script
if __name__ == "__main__":
    main_menu()