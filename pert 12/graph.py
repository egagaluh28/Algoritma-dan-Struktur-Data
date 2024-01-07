class graph:
    #membuat definisi graph
    def _init_(self, gdict=None) :
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    #Mengambil vertex dari graph
    def getVertex(self):
        return list(self.gdict.keys())
    #ketika berhasil menemukan edge dari graph
    def findEdges(self):
        edges=[]
        for v in self.gdict:
            for e in self.gdict[v]:
                if {e,v} not in edges:
                    edges.append({e,v})
        return edges
    
graph = {
    0:[1,3],
    1:[0,2,3,5],
    2:[1,3,4,5],
    3:[0,1,2,4],
    4:[2,3,6],
    5:[1,2],
    6:[1,4]
}
g=graph(grapH)
print("bagian vertex : ", g.getVertex())
print("bagian Edges :  ", g.findEdges())