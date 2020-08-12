
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # add vertices
    vertices = []
    for member in ancestors:
        if member[0] not in vertices:
            vertices.append(member[0])
        if member[1] not in vertices:
            vertices.append(member[1])
    for vertex in vertices:
        graph.add_vertex(vertex)
    # add connections 
    for member in ancestors:
        graph.add_edge(member[1], member[0])
    # if starting node has no neighbors 
    if len(graph.get_neighbors(starting_node)) == 0:
        # return starting node
        return -1
    else:
        #dft method
        # last node
        last_generation = graph.bft(starting_node)
        return last_generation[-1]


class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Sorry dude, vertex doesn't exits")
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        visited = [] #list
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.append(v)
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)
        return visited

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(ancestors, 8))
    # print("1", graph.get_neighbors(1))
    # print("2", graph.get_neighbors(2))
    # print("3", graph.get_neighbors(3))
    # print("4", graph.get_neighbors(4))
    # print("5", graph.get_neighbors(5))
    # print("6", graph.get_neighbors(6))
    # print("7", graph.get_neighbors(7))
    # print("8", graph.get_neighbors(8))
    # print("9", graph.get_neighbors(9))
    # print("10", graph.get_neighbors(10))
    # print("11", graph.get_neighbors(11))