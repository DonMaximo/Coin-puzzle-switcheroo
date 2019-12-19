from configuration import *
from queue import *
from graph import *
class CoinPuzzle:
    def __init__(self, pennies, dimes):
        self.configurations = Configuration.configs(pennies,dimes)
        self.moves= set()
        for c in self.configurations:
            for m in c.moves():
                self.moves.add((c,m))
        self.graph = AdjacencySetGraph(self.configurations,self.moves)

    def solve(self,a,b):
        path = []
        tree = {}
        tovisit= Queue()
        tovisit.enqueue((None,a))
        while tovisit:
            u,v = tovisit.dequeue()
            if u == b:
                break
            if v not in tree:
                tree[v] = u

                for n in self.graph.nbrs(v):
                    tovisit.enqueue((v,n))
        while b is not a:
            path.insert(0,b)
            b = tree[b]
        path.insert(0,a)
        return path
