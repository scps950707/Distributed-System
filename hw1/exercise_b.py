#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-10-26 15:13
# Last Modified:  2017-10-27 12:55
# Filename:       exercise_b.py
# ==========================================================================
nPoints = int(raw_input())
Graph = []
weight = [i for i in map(int, raw_input().split())]
for i in range(0, nPoints):
    Graph.append({'id': i,
                  'weight': weight[i],
                  'edge': map(int, raw_input().split())})

I = []
while True:
    for i in range(0, nPoints):
        totalNeighbors = 0
        if Graph[i]['weight'] < 0 or i in I:
            continue
        neighbors = [idx for idx, val in enumerate(Graph[i]['edge'])
                     if val == 1]
        totalNeighbors += len(neighbors)
        isMax = True
        for n in neighbors:
            tn = float(Graph[n]['weight'])/float(Graph[n]['edge'].count(1)+1)
            ti = float(Graph[i]['weight'])/float(Graph[i]['edge'].count(1)+1)
            if tn > ti:
                isMax = False
        if isMax:
            I.append(Graph[i]['id'])
            for n in neighbors:
                Graph[n]['weight'] = -1
                Graph[n]['edge'][i] = 0
                Graph[i]['edge'][n] = 0
    if totalNeighbors == 0:
        for i in range(0, nPoints):
            if i not in I and Graph[i]['weight'] > 0:
                I.append(i)
        break
# print(Graph)
print(sorted(I))
