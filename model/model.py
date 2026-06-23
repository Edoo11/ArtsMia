from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._graph=nx.Graph()
        self._idMap={}
        for o in DAO.getNodes():
            self._idMap[o.opera_id]=o

    def creaGrafo(self):

        nodi=DAO.getNodes()
        self._graph.add_nodes_from(nodi)
        print(len(self._graph.nodes))

        edges=DAO.getEdges()
        for e in edges:
            o1=self._idMap[e[0]]
            o2=self._idMap[e[1]]
            peso=int(e[2])

            self._graph.add_edge(o1,o2,weight=peso)

        print(len(self._graph.edges))


    def handleCompConnessaModel(self,id):

        if id in self._idMap:
            o1=self._idMap[id]
            compConn=nx.node_connected_component(self._graph,o1)
            return compConn

        else:
            return None

