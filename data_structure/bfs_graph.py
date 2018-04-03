
from collections import defaultdict

class BFS_Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):

        visited = [False] * len(self.graph)
        res, queue = [], []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            res.append(s)

            for obj in self.graph[s]:
                if visited[obj] == False:
                    queue.append(obj)
                    visited[obj] = True

        return res

if __name__ == "__main__":
    # Driver code
    # Create a graph given in the above diagram
    g = BFS_Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(g.bfs(2))
