#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def is_connected( vertex, edge ):
    flag = vertex in ( edge[0], edge[1] )
    return flag

def other_vertex( edge, vertex ):
    if edge[0] == vertex:
        other_vertex = edge[1]
    else:
        other_vertex = edge[0]
    return other_vertex

def MST_prim( V, E ):
    vertex = V[0] # starting vertex, can be chosen at random

    vertex_unconnected = V
    vertex_unconnected.remove(vertex)
    vertex_connected = [vertex]
    MST = []

    while len(vertex_unconnected) > 0:
        min_val = math.inf
        for vertex in vertex_connected:
            for edge in E:
                if is_connected( vertex, edge ):
                    if other_vertex( edge, vertex ) in vertex_unconnected :
                        # this is a vertex connected to the initial vertex
                        # now checking if it's minimal
                        if edge[2] < min_val: 
                            min_val = edge[2]
                            min_edge = edge
                            if edge[0] in vertex_connected:
                                min_vertex = edge[1]
                            else:
                                min_vertex = edge[0]
        
        # has looped through every vertex in MST and every available edge
        vertex_connected.append( min_vertex )

        MST.append( min_edge )
        E.remove( min_edge )
        vertex_unconnected.remove( min_vertex )
    
    return MST

if __name__ == '__main__':
    import doctest
    doctest.testmod()