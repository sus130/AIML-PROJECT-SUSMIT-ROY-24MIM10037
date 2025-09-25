# Autonomous Delivery Agent
This project implements an autonomous delivery agent that navigates a 2D grid city to deliver packages efficiently. The agent is designed to be rational, choosing actions that maximize delivery efficiency while considering constraints like time and fuel (represented as terrain costs). Artificial IntAnelligence and Machine Learning project developed by Susmit Roy.


##  Features

*  Environment Modeling: The agent can navigate environments with static obstacles, varying terrain costs, and dynamic moving obstacles.

* Pathfinding Algorithms:

    * Uninformed Search:

        * Breadth-First Search (BFS)

        * Uniform-Cost Search (UCS)

    * Informed Search:

        * A* Search with the Manhattan distance heuristic.

    * Dynamic Replanning:

        * A simulation mode where the agent uses A* to replan its path at each time step   to      avoid dynamic obstacles.

* Experimental Comparison: The project allows for comparing the performance of these algorithms based on path cost, nodes expanded, and execution time.

## 📁 Project Structure
```
├── maps/
│   ├── small.txt
│   ├── medium.txt
│   ├── large.txt
│   └── dynamic.txt
├── algorithms.py
├── environment.py
├── main.py
├── utils.py
├── README.md
└── report.md
```

## 🚀 Quick Start

### Prerequisites

* Python 3.x

### Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/autonomous-delivery-agent.git](https://github.com/your-username/autonomous-delivery-agent.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd autonomous-delivery-agent
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

Upon running the script, you will be presented with a menu to select a map and an algorithm to execute.

---
## Map File Format

The map files (`.txt`) have a simple format:

* The grid is represented by characters:
    * `S`: Start position
    * `G`: Goal position
    * `.`: Standard terrain (cost = 1)
    * `1`-`9`: Varied terrain with corresponding movement cost.
    * `X`: Static obstacle (wall).
* Dynamic obstacles are defined after a `---` separator. Each line represents an obstacle's position and the time steps at which it appears:
    * `obstacle_id,row,col,time1,time2,...`



## Demo Video

https://drive.google.com/file/d/1T4Q4pm5gpQn3UV3dMG-0g5BL5BcW2SeR/view?usp=sharing



#
