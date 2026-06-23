import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        return self._model.creaGrafo()

    def handleCompConnessa(self,e):

        id=int(self._view._txtIdOggetto.value)

        compConn= self._model.handleCompConnessaModel(id)

        if compConn is not None:

            self._view.txt_result.controls.append(
                ft.Text(len(list(compConn)))
            )

        else:
            self._view.txt_result.controls.append(
                ft.Text("NODO INSERITO NON VALIDO" , color="RED")
            )

        self._view.update_page()