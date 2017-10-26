#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-10-26 10:46
# Last Modified:  2017-10-26 14:54
# Filename:       exercise_a.py
# ==========================================================================
# Graph: [[number,weight,[edges]],[number,weight,[edges]]i,.....]
nPoints = int(raw_input())
Graph = []
weight = [i for i in map(int, raw_input().split())]
for i in range(0, nPoints):
    Graph.append([i, weight[i], map(int, raw_input().split())])
# print(Graph)
I = []

while len(Graph) > 0:
    # select v from G
    maxVal = 0
    for idx, v in enumerate(Graph):
        # print(idx)
        tmp = float(v[1])/float(v[2].count(1)+1)
        # print(tmp)
        if tmp > maxVal:
            maxVal = tmp
            maxIdx = idx
    # Add v to I
    I.append(Graph[maxIdx][0])
    listIdxDel = [maxIdx]
    for idx, val in enumerate(Graph[maxIdx][2]):
        if val == 1:
            listIdxDel.append(idx)
    # Remove Edeges
    for v in Graph:
        for idx in sorted(listIdxDel, reverse=True):
            del v[2][idx]
    # Remove Vertices
    for idx in sorted(listIdxDel, reverse=True):
        del Graph[idx]
print(sorted(I))
