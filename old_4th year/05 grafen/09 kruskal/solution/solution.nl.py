#!/usr/bin/python
# -*- coding: utf-8 -*-
def MST_kruskal( V: list, E: list ) -> list:
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    sorted_edges = sorted(E, key=lambda edge: edge[2])
    parent = {v: v for v in V}
    rank = {v: 0 for v in V}
    tree = []

    for u, v, weight in sorted_edges:
        if find(parent, u) != find(parent, v):
            tree.append((u, v, weight))
            union(parent, rank, u, v)

    return tree
