from model.model import Model

if __name__ == "__main__":

    print("--- 1. CREAZIONE GRAFO ---")
    m = Model()


    input_di_prova = 5

    try:
        m.build_graph(input_di_prova)
        print(f"-> Grafo creato con input: {input_di_prova}")
    except Exception as e:
        print(f"ERRORE CRITICO in build_graph: {e}")
        exit()


    n_nodi = len(m._graph.nodes)
    n_archi = len(m._graph.edges)
    print(f"-> Nodi: {n_nodi}")
    print(f"-> Archi: {n_archi}")

    if n_nodi == 0:
        print("GRAFO VUOTO! Controlla il DAO o i filtri.")
    exit()



