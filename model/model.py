import copy

from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._graph=nx.Graph()
        self._idMap={}
        for o in DAO.getNodes():
            self._idMap[o.opera_id]=o
        self.compConn=None
        self._optPath=[]
        self._optCost=0

    def creaGrafo(self):

        nodi=DAO.getNodes()
        self._graph.add_nodes_from(nodi)


        edges=DAO.getEdges()
        for e in edges:
            o1=self._idMap[e[0]]
            o2=self._idMap[e[1]]
            peso=int(e[2])

            self._graph.add_edge(o1,o2,weight=peso)

        return self._graph


    def handleCompConnessaModel(self,id):

        if id in self._idMap:
            o1=self._idMap[id]
            self.compConn=nx.node_connected_component(self._graph,o1)
            return self.compConn

        else:
            return None

    def handleCercaOggettiModel(self,L,idNodo):

        if L>=2 and L<=len(self.compConn):

            return self.cercaCamminoMassimo(L,idNodo)


    def cercaCamminoMassimo(self,L,idNodo):


        parziale=[n]

        for n in self._graph.neighbors(n):
            if n.classification==parziale[-1].classification:
                parziale.append(n)
                self.ricorsione(parziale,L)
                parziale.pop()

        return self._optPath,self._optCost


    def ricorsione(self,parziale,L):

        if len(parziale)==L:

            if self._costoPath(parziale)>self._optCost:
                self._optCost=self._costoPath(parziale)
                self._optPath=copy.deepcopy(parziale)
            return

        for n in self._graph.neighbors(parziale[-1]):
            if n.classification==parziale[-1].classification:
                parziale.append(n)
                self.ricorsione(parziale,L,n)
                parziale.pop()


    def _costoPath(self,parz):
        costo=0
        for i in range(0,len(parz-1)):
            costo+=self._graph[parz[i]][parz[i+1]]['weight']

        return costo
