'''import networkx as nx
import matplotlib.pyplot as plt

def create_graph(cities):
  """
  Creates a graph representing connections between cities.

  Args:
      cities: A list of cities and their connections (e.g.,
              [('A', 'B', 10), ('A', 'C', 5), ('B', 'C', 3), ...]).

  Returns:
      A NetworkX graph object.
  """
  G = nx.Graph()
  for city1, city2, distance in cities:
    G.add_edge(city1, city2, weight=distance)
  return G

def find_shortest_path(graph, start, end):
  """
  Finds the shortest path between two cities using Dijkstra's algorithm.

  Args:
      graph: A NetworkX graph object.
      start: The starting city.
      end: The destination city.

  Returns:
      A list of cities representing the shortest path,
      or None if no path exists.
  """
  try:
    path = nx.shortest_path(graph, source=start, target=end, weight='weight')
    # Fix the typo here (change '!' to ':' after f-string)
    print(f"Shortest path from {start} to {end}: {path}")
    return path
  except nx.NetworkXNoPath:
    return None

def visualize_graph(graph, path=None):
  """
  Visualizes the graph with optional highlighting of the shortest path.

  Args:
      graph: A NetworkX graph object.
      path: A list of cities representing the shortest path.
  """
  pos = nx.spring_layout(graph)  # Position nodes for better visualization
  nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500)
  if path:
    path_edges = zip(path, path[1:])
    nx.draw_networkx_edges(graph, pos, edgelist=list(path_edges), edge_color='red', width=2)
  plt.show()

if __name__ == "__main__":
  # Define cities and their connections (distances in arbitrary units)
  cities = [
      ('A', 'B', 10),
      ('A', 'C', 5),
      ('B', 'C', 3),
      ('B', 'D', 7),
      ('C', 'D', 2),
      ('D', 'E', 4)
  ]

  # Create the graph
  graph = create_graph(cities)

  # Find the shortest path from A to E
  start_city = 'A'
  end_city = 'E'
  shortest_path = find_shortest_path(graph, start_city, end_city)

  if shortest_path:
    print(f"Shortest path from {start_city} to {end_city}: {shortest_path}")
    visualize_graph(graph, shortest_path)
  else:
    print(f"No path found from {start_city} to {end_city}")
    '''
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(cities):
  """
  Creates a graph representing connections between cities.

  Args:
      cities: A list of cities and their connections (e.g.,
              [('A', 'B', 10), ('A', 'C', 5), ('B', 'C', 3), ...]).

  Returns:
      A NetworkX graph object.
  """
  G = nx.Graph()
  for city1, city2, distance in cities:
    G.add_edge(city1, city2, weight=distance)
  return G

def find_shortest_path(graph, start, end):
  """
  Finds the shortest path between two cities using Dijkstra's algorithm.

  Args:
      graph: A NetworkX graph object.
      start: The starting city.
      end: The destination city.

  Returns:
      A list of cities representing the shortest path,
      or None if no path exists.
  """
  try:
    path = nx.shortest_path(graph, source=start, target=end, weight='weight')
    print(f"Shortest path from {start} to {end}: {path}")
    return path
  except nx.NetworkXNoPath:
    return None

def visualize_graph(graph, path=None):
  """
  Visualizes the graph with optional highlighting of the shortest path.

  Args:
      graph: A NetworkX graph object.
      path: A list of cities representing the shortest path.
  """
  pos = nx.spring_layout(graph)  # Position nodes for better visualization
  nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500)
  if path:
    path_edges = zip(path, path[1:])
    nx.draw_networkx_edges(graph, pos, edgelist=list(path_edges), edge_color='red', width=2)
  plt.show()

if __name__ == "__main__":
  num_cities = int(input("How many cities do you want to visit? "))

  cities = []
  for _ in range(num_cities):
    city_name = input(f"Enter the name of city {_+1}: ")
    connections = int(input(f"How many connections does {city_name} have? "))
    for _ in range(connections):
      connected_city = input(f"Enter the name of a city connected to {city_name}: ")
      distance = int(input(f"Enter the distance between {city_name} and {connected_city}: "))
      cities.append((city_name, connected_city, distance))

  # Create the graph
  graph = create_graph(cities)

  # Get user input for start and end cities
  start_city = input("Enter the starting city: ")
  end_city = input("Enter the destination city: ")

  # Find the shortest path
  shortest_path = find_shortest_path(graph, start_city, end_city)

  if shortest_path:
    visualize_graph(graph, shortest_path)
  else:
    print(f"No path found from {start_city} to {end_city}")