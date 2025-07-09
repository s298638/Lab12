import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view , model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.naz=None
        self.anno=None

        self._listYear = []
        self._listCountry = []

    def metti_opzioni(self):
        lista=[]
        for i in self._model.dammi_lista_nazioni():
            lista.append(ft.dropdown.Option(key=i,data=i,on_click=self.read_nazione))
        return lista
    def read_nazione(self,e):
        self.naz=e.control.data
        self._model.country=self.naz

    def metti_opzioni_year(self):
        lista = []
        for i in self._model.dammi_lista_anni():
            lista.append(ft.dropdown.Option(key=i, data=i, on_click=self.read_anno))
        return lista

    def read_anno(self, e):
        self.anno = e.control.data
        self._model.anno=self.anno


    def fillDD(self):
        pass


    def handle_graph(self, e):
        self._model.grafo=nx.Graph()
        num_nodi=self._model.get_nodi()
        num_archi=self._model.get_costruisci_grafo()
        self._view.txt_result.controls.append(ft.Text(f"GRAFO CREATO"))
        self._view.txt_result.controls.append(ft.Text(f"num nodi----{num_nodi}"))
        self._view.update_page()
        self._view.txt_result.controls.append(ft.Text(f"num archi----{num_archi}"))
        self._view.btn_volume.disabled = False
        self._view.update_page()


    def handle_volume(self, e):
        lista=self._model.vicini()
        for l in lista:
            self._view.txtOut2.controls.append(ft.Text(f"{l[0]}------->{l[1]}"))
            self._view.update_page()



    def handle_path(self, e):
        pass
