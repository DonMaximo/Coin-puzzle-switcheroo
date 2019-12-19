class AdjacencySetGraph:
    def __init__(self, V, E):
        self._V = set()
        self._nbrs = {}
        for v in V: self.addvertex(v)
        for u,v in E: self.addedge(u,v)
    def vertices(self):
        return iter(self._V)
    def edges(self):
        for u in self._V:
            for v in self.nbrs(u):
                yield (u,v)
    def addvertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()
    def addedge(self, u, v):
        self._nbrs[u].add(v)
    def nbrs(self, v):
        return iter(self._nbrs[v])
