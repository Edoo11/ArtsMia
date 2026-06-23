import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        grafo= self._model.creaGrafo()
        self._view.txt_result.controls.append(
            ft.Text(f"numero di nodi:{len(grafo.nodes)}")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"numero di archi:{len(grafo.edges)}")
        )
        self._view.update_page()

    def handleCompConnessa(self,e):

        id=int(self._view._txtIdOggetto.value)

        compConn= self._model.handleCompConnessaModel(id)

        if compConn is not None:

            self._view.txt_result.controls.append(
                ft.Text(f"componente connessa:{len(list(compConn))}"))


        else:
            self._view.txt_result.controls.append(
                ft.Text("NODO INSERITO NON VALIDO" , color="RED")
            )

        self._view.update_page()

    def handleCercaOggetto(self,e):
        L = int(self._view._txtNum.value)
        idNodo = int(self._view._txtIdOggetto.value)
        optPath , optCOsto = self._model.handleCercaOggettiModel(L,idNodo)
        self._view.txt_result.controls.append(
            ft.Text(f"cammino")
        )
        for n in optPath:
            self._view.txt_result.controls.append(
                ft.Text(f"nodo:{n.__str__()}")
            )

        self._view.txt_result.controls.append(
            ft.Text(f"costo del cammino : {optCOsto}")
        )