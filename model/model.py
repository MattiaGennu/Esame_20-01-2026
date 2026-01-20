import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._idMap = {}


    def load_artists_with_min_albums(self, min_albums):
        pass

    def build_graph(self,n_alb):
        self._graph.clear()
        self._nodes = DAO.get_all_nodes(n_alb)
        self._idMap = {n.id: n for n in self._nodes}
        self._graph.add_nodes_from(self._nodes)

        mappa_connessioni = DAO.get_mappa_collegamenti()

        for u in self._nodes:
            for v in self._nodes:

                if u.id < v.id:
                    set_u = mappa_connessioni.get(u.id, set())
                    set_v = mappa_connessioni.get(v.id, set())
                    intersezione = set_u.intersection(set_v)

                    if len(intersezione) > 0:
                        self._graph.add_edge(u, v, weight=len(intersezione))

    def get_componente_connessa(self, node_obj):

        if node_obj not in self._graph:
            return 0

        if self._graph.is_directed():

            comps = nx.weakly_connected_components(self._graph)
            for c in comps:
                if node_obj in c:
                    return len(c)
            else:

                return len(nx.node_connected_component(self._graph, node_obj))
        return 0

    def get_graph_details(self):
        return len(self._graph.nodes), len(self._graph.edges)


