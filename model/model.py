import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo=nx.Graph()
        self.anno=None
        self.country=None
        self.map={}
        pass
    def get_nodi(self):
        lista=DAO.get_nodis(self.country)
        for l1 in lista:
            self.map[l1.cod_retailer]=l1
            self.grafo.add_node(l1.cod_retailer)
        return len(self.grafo.nodes)
    def get_costruisci_grafo(self):
        lista=DAO.get_archis(self.country,self.anno)
        for l in lista:
            self.grafo.add_edge(l[0],l[1],weight=l[2])
        return len(self.grafo.edges)
    def vicini(self):
        lista=[]
        for l in self.grafo.nodes:
            somma = 0
            for vicino in self.grafo.neighbors(l):
                if self.grafo.has_edge(l,vicino):
                    somma+=self.grafo[l][vicino]['weight']
            if somma>0:
                lista.append((self.map[l].nome_retailer,somma))
        lista1=sorted(lista, key=lambda k: k[1], reverse=True)
        return lista1
    def dammi_lista_nazioni(self):
        nazioni=[]
        lista=DAO.get_nazioni()
        for l in lista:
            nazioni.append(l)
        return nazioni
    def dammi_lista_anni(self):
        anni=[]
        lista=DAO.get_anni()
        for l in lista:
            anni.append(l)
        return anni
