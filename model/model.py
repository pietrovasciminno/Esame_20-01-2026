import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self._artists_map = {}
        self.load_all_artists()
        self.list_nodi = []
        self.list_edge = []

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        for artist in self._artists_list:
            self._artists_map[artist.id] = artist
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        list = DAO.get_artists_with_min_albums(min_albums)
        for l in list:
            for artist in self._artists_list:
                if l[0] == artist.id:
                    self.list_nodi.append(artist)
        return

    def get_connessioni(self):
        self.dict_c_artist = DAO.get_connessioni()
        for artist1 in self.list_nodi:
            for artist2 in self.list_nodi:
                if artist1 != artist2:
                    peso = 0
                    for l1 in self.dict_c_artist[artist1.id]['genre_id']:
                        for l2 in self.dict_c_artist[artist1.id]['genre_id']:
                            if l1 == l2:
                                peso += 1
                    self.list_edge.append((artist1, artist2, peso))
        return




    def build_graph(self):
        self._graph.add_nodes_from(self.list_nodi)
        for l in self.list_edge:
            if l[2]  != 'None':
                if l[2] > 0:
                    u_node = l[0]
                    v_node = l[1]
                    self._graph.add_edge(u_node, v_node, weight=l[2])





