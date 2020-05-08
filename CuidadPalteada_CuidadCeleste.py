import networkx as nx
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox


def grafo():
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    #creacion de grafo que representa el mapa

    kanto = nx.DiGraph()
    #insercion de los vertices
    kanto.add_node("Meseta Añil",pos=(15,95))#
    kanto.add_node("Calle Victoria",pos=(15,75))#
    kanto.add_node("Isla Canela",pos=(25,5))#
    kanto.add_node("Pueblo Paleta",pos=(25,50))#
    kanto.add_node("Ciudad Verde",pos=(25,70))#
    kanto.add_node("Bosque Verde",pos=(25,85))#
    kanto.add_node("Cueva Diglet",pos=(25,95))#
    kanto.add_node("Ciudad Plateada",pos=(40,110))
    kanto.add_node("Monte Luna",pos=(55,110))#
    kanto.add_node("Ciudad Azulona",pos=(51,90))#
    kanto.add_node("Islas Espuma",pos=(47,5))#
    kanto.add_node("Ciudad Celeste",pos=(70,110))##
    kanto.add_node("Ciudad Azafran",pos=(67,90))#
    kanto.add_node("Ciudad Carmin",pos=(63,77))#
    kanto.add_node("Ciudad Fucsia",pos=(62,50))#
    kanto.add_node("Tunel Roca",pos=(85,110))#
    kanto.add_node("Central Energía",pos=(85,90))#
    kanto.add_node("Pueblo Lavanda",pos=(85,60))#


    #union de vertices

    kanto.add_edge("Meseta Añil","Calle Victoria",weight=3)
    kanto.add_edge("Calle Victoria","Ciudad Verde",weight=4)
    kanto.add_edge("Pueblo Paleta","Ciudad Verde",weight=3)
    kanto.add_edge("Ciudad Verde","Bosque Verde",weight=2)
    kanto.add_edge("Bosque Verde","Cueva Diglet",weight=1)
    kanto.add_edge("Cueva Diglet","Ciudad Plateada",weight=5)
    kanto.add_edge("Ciudad Plateada","Monte Luna",weight=4)
    kanto.add_edge("Monte Luna","Ciudad Celeste",weight=4)
    kanto.add_edge("Ciudad Celeste","Ciudad Azafran",weight=3)
    kanto.add_edge("Ciudad Celeste","Tunel Roca",weight=4)
    kanto.add_edge("Ciudad Azulona","Ciudad Azafran",weight=4)
    kanto.add_edge("Central Energía","Tunel Roca",weight=3)
    kanto.add_edge("Central Energía","Pueblo Lavanda",weight=4)
    kanto.add_edge("Pueblo Lavanda","Ciudad Azafran",weight=7)
    kanto.add_edge("Ciudad Azafran","Ciudad Carmin",weight=1)
    kanto.add_edge("Ciudad Carmin","Ciudad Fucsia",weight=3)
    kanto.add_edge("Ciudad Fucsia","Ciudad Azulona",weight=6)
    kanto.add_edge("Ciudad Fucsia","Pueblo Lavanda",weight=7)
    kanto.add_edge("Ciudad Fucsia","Islas Espuma",weight=8)
    kanto.add_edge("Islas Espuma","Isla Canela",weight=7)
    kanto.add_edge("Isla Canela","Pueblo Paleta",weight=5)

    nodesP = ["Ciudad Plateada","Monte Luna","Ciudad Celeste"]
    nodesGym=["Isla Canela","Ciudad Verde","Ciudad Plateada","Ciudad Azulona","Ciudad Celeste","Ciudad Azafran","Ciudad Carmin","Ciudad Fucsia"]
    color=['#CCFF99']

    colore=['#F1948A']

    AD2=nx.dijkstra_path(kanto,'Ciudad Plateada','Ciudad Celeste')
    print("Ruta mas corta usando el algoritmo de Dijkstra entre Ciudad Plateada y Ciudad Celeste: ",AD2)
    g=kanto.subgraph(AD2)

    pos1 = nx.get_node_attributes(kanto, 'pos')
    weight1=nx.get_edge_attributes(kanto,'weight')

    nx.draw_networkx(g,pos1,node_color = color,edge_color=colore)
    nx.draw_networkx_edge_labels(kanto,pos1,edge_labels = weight1)
    plt.show()
    fig.savefig("CuidadPalteada_CuidadCeleste.png")


grafo()
