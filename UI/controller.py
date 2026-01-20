import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            value = int(self._view.txtNumAlbumMin.value)
            if value < 0 :
                return self._view.show_alert("inseririre un valore accettato (maggiore di 0 e intero)")
            else:
                self._model.load_artists_with_min_albums(value)
                self._model.get_connessioni()
                self._model.build_graph()
                print(self._model._graph)
                self._view.ddArtist.options.clear()
                self._view.ddArtist.options.append(ft.dropdown.Option(y.name) for y in self._model.list_nodi)
                self._view.update_page()
        except ValueError:
            return self._view.show_alert("inseririre un valore accettato (maggiore di 0 e intero)")


    def handle_connected_artists(self, e):
        pass



