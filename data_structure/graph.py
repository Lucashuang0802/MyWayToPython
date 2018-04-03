
from linked_list import *

class Graph:

    def __init__(self, vertices_count):
        self.vertices_count = vertices_count

        self.graph = []
        for _ in range(vertices_count):
            self.graph.append(LinkedList())

    def add_edge(self, src ,dest):
        if not src and not dest: return
        if src >= self.vertices_count or dest >= self.vertices_count: return
        self.graph[src].insert_at_front(dest)
        self.graph[dest].insert_at_front(src)

    def get_graph(self):
        return [ll.traverse_and_print() for ll in self.graph]

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    print(graph.get_graph())
