#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-10-26 10:46
# Last Modified:  2017-10-26 15:23
# Filename:       exercise_a.py
# ==========================================================================
nPoints = int(raw_input())
Graph = []
weight = [i for i in map(int, raw_input().split())]
for i in range(0, nPoints):
    Graph.append({'id': i,
                  'weight': weight[i],
                  'edge': map(int, raw_input().split())})
# print(Graph)
I = []
while len(Graph) > 0:
    # select v from G
    maxIdx = Graph.index(max(Graph, key=lambda v:
                         float(v['weight'])/float(v['edge'].count(1)+1)))
    # Add v to I
    I.append(Graph[maxIdx]['id'])
    # Find neighbor
    listIdxDel = [idx for idx, val in enumerate(Graph[maxIdx]['edge'])
                  if val == 1]
    listIdxDel.append(maxIdx)
    # Remove Edeges
    for v in Graph:
        for idx in sorted(listIdxDel, reverse=True):
            del v['edge'][idx]
    # Remove Vertices
    for idx in sorted(listIdxDel, reverse=True):
        del Graph[idx]
print(sorted(I))
