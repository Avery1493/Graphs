"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # Adjacency List / empty dictionary
        # Key: Node 
        # Value: adjacent/connected node
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Add set of Nodes
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Add connection
        # if Nodes exist
        if v1 in self.vertices and v2 in self.vertices:
            # connect them 
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Sorry dude, vertex doesn't exits")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # Return the set at vertex_id
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create empty queque, enqueue starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # create set to store the visited vertices 
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if vertex has not been visited
            if v not in visited:
                # mark as visited
                visited.add(v)
                # print for debugging
                # print(v)
                # add neighbors to back of queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack, push starting vertex
        s = Stack()
        s.push(starting_vertex)
        # create set to store the visited vertices 
        visited = set()
        # while questackue is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop() 
            # if vertex has not been visited
            if v not in visited:
                # mark as visited
                visited.add(v)
                # print for debugging
                # print(v)
                # add neighbors to top of stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)
        

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # add starting vertex
        visited.add(starting_vertex)
        # go through neighbors 
        for v in self.get_neighbors(starting_vertex):
            # check if vertex has been visited
            if v not in visited:
                # run recursive call
                self.dft_recursive(v, visited)
                #print(visited)
        
            
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create empty queue
        q = Queue()
        # enqueue path to starting vertex (list)
        q.enqueue([starting_vertex])
        # create set for visited
        visited = set()
        # while queue not empty
        while q.size() > 0:
            # dequeue the first path (list)
            path = q.dequeue()
            # grab the last vertex from path
            # check if vertex has not been visited
            if path[-1] not in visited:
                # if destination
                if path[-1] == destination_vertex:
                    # return the path
                    return path
                # mark as visited
                visited.add(path[-1])
                # add path to neighbors to back of queue
                for next_vertex in self.get_neighbors(path[-1]):
                    # make copy of path
                    copy_path = list(path)
                    # append neighbor to path and enqueue path
                    copy_path.append(next_vertex)
                    q.enqueue(copy_path)
        # return None
        return None 


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create empty stack
        s = Stack()
        # push path to starting vertex (list)
        s.push([starting_vertex])
        # create set for visited
        visited = set()
        # while stack not empty
        while s.size() > 0:
            # pop the first path
            path = s.pop()
            # grab the first vertex from path
            # check if vertex has not been visited
            if path[-1] not in visited:
                # if destination
                if path[-1] == destination_vertex:
                    # return the path
                    return path
                # mark as visited
                visited.add(path[-1])
                # add path to neighbors to top of stack
                for next_vertex in self.get_neighbors(path[-1]):
                    # make copy of path
                    copy_path = list(path)
                    # append neighbor to path and push to path
                    copy_path.append(next_vertex)
                    s.push(copy_path)
        # return None
        return None 


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        # add starting vertex
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # check if destination
        if starting_vertex == destination_vertex:
            return path
        # go through neighbors 
        for v in self.get_neighbors(starting_vertex):
            # check if vertex has been visited
            if v not in visited:
                # run recursive call
                new_path = self.dfs_recursive(v, destination_vertex, visited, path)
                if new_path:
                    return new_path

        return None
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        # 1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        # 1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
