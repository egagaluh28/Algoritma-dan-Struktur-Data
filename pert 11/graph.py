class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def findEdges(self):
        edges = []
        for v in self.gdict:
            for e in self.gdict[v]:
                if {e, v} not in edges:
                    edges.append({v, e})
        return edges


graph = {
    0: [1, 3],
    1: [0, 2, 3, 5],
    2: [1, 3, 4, 5],
    3: [0, 1, 2, 4],
    4: [2, 3, 6],
    5: [1, 2],
    6: [1, 4]
}

g = Graph(graph)
print("Bagian vertex: ", g.getVertices())
print("Bagian edges: ", g.findEdges())