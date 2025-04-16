


import sys
from collections import defaultdict

def solve():  
    graph = defaultdict(list)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 3:
            continue
        start_id = int(parts[0].strip())
        end_id = int(parts[1].strip())
        distance = float(parts[2].strip())
        graph[start_id].append((end_id, distance))
    
    longest_path = []
    max_distance = 0
    
    def dfs(current_station, visited, path, current_dist):
        nonlocal longest_path, max_distance
        
        visited.add(current_station)
        path.append(current_station) 

        if current_dist > max_distance:
            max_distance = current_dist
            longest_path = path.copy()
        
        for (next_station, dist) in graph[current_station]:
            if next_station not in visited:
                dfs(
                    next_station,
                    visited,
                    path,
                    current_dist + dist
                )
        
        visited.remove(current_station)
        path.pop()
    
    for station_id in graph.keys():
        dfs(station_id, set(), [], 0)
    
    for station_id in longest_path:
        print(station_id)

if __name__ == "__main__":
    solve()

