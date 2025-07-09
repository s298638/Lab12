from model.model import Model
from database.DAO import DAO
modello=Model()
modello.anno=2015
modello.country="France"
print(modello.get_nodi())
print(modello.get_costruisci_grafo())