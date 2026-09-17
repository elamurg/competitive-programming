"""
Bellman-Ford Algorithm is a graph search algorithm that solves the single-source 
shortest path problem for a graph with negative edge weights. It works by iteratively
relaxing all the edges in the graph, updating the shortest path estimates for each vertex.
The algorithm can also detect negative weight cycles in the graph, which makes it more 
versatile than Dijkstra's Algorithm. The time complexity of the Bellman-Ford Algorithm is
O(V * E), where V is the number of vertices and E is the number of edges in the graph.
"""