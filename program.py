import pandas as pd
import heapq

def build_graph_from_csv(filepath):
    df = pd.read_csv(filepath)
    graph = {}
    
    for index, row in df.iterrows():
        origin = str(row['Origin']).strip()
        destination = str(row['Destination']).strip()
        distance = float(row['Distance'])
        
        if origin not in graph:
            graph[origin] = {}
        if destination not in graph:
            graph[destination] = {}
            
        graph[origin][destination] = distance
        graph[destination][origin] = distance
        
    return graph

def uniform_cost_search(graph, start, target):
    if start not in graph or target not in graph:
        return float('inf'), []

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == target:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = target
    
    if distances[target] == float('inf'):
        return float('inf'), []
        
    while current is not None:
        path.append(current)
        current = previous_nodes.get(current)
        
    path.reverse()
    return distances[target], path

if __name__ == "__main__":
    csv_file_path = 'indian-cities-dataset.csv' 
    
    try:
        india_road_graph = build_graph_from_csv(csv_file_path)
        
        city_map = {city.lower(): city for city in india_road_graph.keys()}
        
        start_input = input("Enter the starting city: ").strip().lower()
        target_input = input("Enter the destination city: ").strip().lower()
        
        if start_input not in city_map:
            print(f"\nError: Could not find '{start_input}' in the dataset.")
        elif target_input not in city_map:
            print(f"\nError: Could not find '{target_input}' in the dataset.")
        else:
            start_city = city_map[start_input]
            target_city = city_map[target_input]
            
            total_distance, route = uniform_cost_search(india_road_graph, start_city, target_city)
            
            if total_distance != float('inf'):
                print(f"\nOptimal Route from {start_city} to {target_city}:")
                print(" -> ".join(route))
                print(f"Total Road Distance: {total_distance} km")
            else:
                print(f"\nNo route exists between {start_city} and {target_city}.")
                
    except FileNotFoundError:
        print(f"Error: Could not find '{csv_file_path}'.")