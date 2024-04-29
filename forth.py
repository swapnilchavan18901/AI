from heapq import heappush, heappop
graph = {
 'A': {'B': 5, 'C': 10},
 'B': {'D': 6},
 'C': {'D': 8},
 'D': {'E': 12},
 'E': {}
}
def heuristic(node, goal):
    heuristic_values = {'A': 16, 'B': 11, 'C': 8, 'D': 4, 'E': 0}
    return heuristic_values[node]
start = 'A'
goal = 'E'
if start not in graph:
    raise ValueError("start is not in the graph")
if goal not in graph:
     raise ValueError("goal is not in the graph")
g_score = {start: 0}
f_score = {start: heuristic(start, goal)}
open_set = [(f_score[start], start)]
came_from = {}
while open_set:
    current = heappop(open_set)[1]
    if current == goal:
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        print("Shortest path:", path[::-1])
        break
    for neighbor in graph[current]:
        tentative_g_score = g_score[current] + graph[current][neighbor]
        if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
        heappush(open_set, (f_score[neighbor], neighbor))
else:
 raise ValueError("no path found")