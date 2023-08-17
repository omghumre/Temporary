# -*- coding: utf-8 -*-
"""AI-lab6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XBY9eMy73hm7VBWI_oDzZRJahHe8ouby

Roll No.: 40

Name: Jasmitsingh Saggu

Sem: 4th

Batch: E3

Lab-6

Aim:- Apply depth first and depth-limited search on Romania Map
"""

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Giurgiu': {'Bucharest': 90}, 'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Neamt' : {'Iasi':87}
}

def dfs(graph, start, goal, path=None, path_limit=None):
    if path is None:
        path = []
    path = path + [start]

    if start == goal:
        return [path]

    if start not in graph:
        return []

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path, path_limit)
            if new_path:  # If a path is found, return it
                return new_path

    return []  # If no path is found

start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")

choice = input("Enter 1 for DFS or 2 for DFS with limitation: ")

if choice == "1":
    # Perform DFS
    path = dfs(graph, start_city, goal_city)
    if path:
        print(f"Path from {start_city} to {goal_city}:")
        print(' -> '.join(path[0]))  # Join the cities of the first path
    else:
        print(f"No path found from {start_city} to {goal_city}.")

elif choice == "2":
    path_limit = int(input("Enter the maximum number of paths to display (Enter 0 for unlimited paths): "))

    # Perform DFS with limitation
    paths = dfs(graph, start_city, goal_city, path_limit=path_limit)
    if paths:
        print(f"Path from {start_city} to {goal_city}:")
        print(' 👉 '.join(paths[0]))  # Join the cities of the first path found
        if path_limit and len(paths) > 1:
            print(f"Note: {len(paths)-1} more path(s) found.")
    else:
        print(f"No path found from {start_city} to {goal_city}.")

else:
    print("Invalid choice. Please enter 1 or 2.")
