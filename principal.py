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

    kanto = nx.Graph()
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
    kanto.add_edge("Ciudad Celeste","Monte Luna",weight=4)
    kanto.add_edge("Ciudad Celeste","Ciudad Azafran",weight=3)
    kanto.add_edge("Ciudad Celeste","Tunel Roca",weight=4)
    kanto.add_edge("Ciudad Azulona","Ciudad Azafran",weight=4)
    kanto.add_edge("Central Energía","Tunel Roca",weight=3)
    kanto.add_edge("Central Energía","Pueblo Lavanda",weight=4)
    kanto.add_edge("Pueblo Lavanda","Ciudad Azafran",weight=7)
    kanto.add_edge("Ciudad Azafran","Ciudad Carmin",weight=1)
    kanto.add_edge("Ciudad Fucsia","Ciudad Carmin",weight=3)
    kanto.add_edge("Ciudad Fucsia","Ciudad Azulona",weight=6)
    kanto.add_edge("Ciudad Fucsia","Pueblo Lavanda",weight=7)
    kanto.add_edge("Ciudad Fucsia","Islas Espuma",weight=8)
    kanto.add_edge("Isla Canela","Islas Espuma",weight=7)
    kanto.add_edge("Isla Canela","Pueblo Paleta",weight=5)

    AD1=nx.dijkstra_path(kanto, 'Pueblo Paleta', 'Ciudad Plateada')
    AD2=nx.dijkstra_path(kanto,'Ciudad Plateada','Ciudad Celeste')
    AD3=nx.dijkstra_path(kanto,'Ciudad Celeste','Ciudad Carmin')
    AD4=nx.dijkstra_path(kanto,'Ciudad Carmin','Ciudad Azulona')
    AD5=nx.dijkstra_path(kanto,'Ciudad Azulona','Ciudad Fucsia')
    AD6=nx.dijkstra_path(kanto,'Ciudad Fucsia','Ciudad Azafran')
    AD7=nx.dijkstra_path(kanto,'Ciudad Azafran','Isla Canela')
    AD8=nx.dijkstra_path(kanto,'Isla Canela','Ciudad Verde')
    print(AD1)
    print(AD2)
    print(AD3)
    print(AD4)
    print(AD5)
    print(AD6)
    print(AD7)
    print(AD8)


    nodesP = ["Meseta Añil","Calle Victoria","Isla Canela","Pueblo Paleta","Ciudad Verde","Bosque Verde","Cueva Diglet","Ciudad Plateada","Monte Luna","Ciudad Azulona","Islas Espuma","Ciudad Celeste","Ciudad Azafran","Ciudad Carmin","Ciudad Fucsia","Tunel Roca","Central Energía","Pueblo Lavanda"]
    nodesGym=["Isla Canela","Ciudad Verde","Ciudad Plateada","Ciudad Azulona","Ciudad Celeste","Ciudad Azafran","Ciudad Carmin","Ciudad Fucsia"]
    color_map=[]
    for node in nodesP:
        if node in nodesGym:
            color_map.append('#CCFF99')
        elif node=="Pueblo Paleta":
            color_map.append('#DEB887')
        else:
            color_map.append('#AED6F1')
    colore=['#F1948A']
    pos1 = nx.get_node_attributes(kanto, 'pos')
    weight1=nx.get_edge_attributes(kanto,'weight')
#graficamente

    nx.draw_networkx(kanto,pos1,node_list = nodesP,node_color = color_map,edge_color=colore)
    nx.draw_networkx_edge_labels(kanto,pos1,edge_labels = weight1)
    plt.show()
    fig.savefig("principal"+ ".png")


grafo()
