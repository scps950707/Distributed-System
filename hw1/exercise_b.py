#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-10-26 15:13
# Last Modified:  2017-10-27 17:17
# Filename:       exercise_b.py
# ==========================================================================
nPoints = int(raw_input())
Graph = []
weight = [i for i in map(int, raw_input().split())]
for i in range(0, nPoints):
    Graph.append({'id': i,
                  'weight': weight[i],
                  'edge': map(int, raw_input().split())})

prev_round = [-1] * nPoints
curr_round = [-1] * nPoints

while True:
    for i in range(0, nPoints):
        if prev_round[i] == 1 or prev_round[i] == 0:
            continue
        neighbors = [idx for idx, val in enumerate(Graph[i]['edge'])
                     if val == 1]
        neiChoicePrev = []
        for n in neighbors:
            neiChoicePrev.append(prev_round[n])

        # Single node with no neighbor
        if len(neiChoicePrev) == neiChoicePrev.count(0):
            curr_round[i] = 1
            continue
        if 1 in neiChoicePrev:
            curr_round[i] = 0
            continue
        isMax = True
        for n in neighbors:
            tn = float(Graph[n]['weight'])/float(Graph[n]['edge'].count(1)+1)
            ti = float(Graph[i]['weight'])/float(Graph[i]['edge'].count(1)+1)
            if tn > ti or (tn == ti and i > n):
                isMax = False
        if isMax:
            curr_round[i] = 1
    resEqual = True
    for i in range(0, nPoints):
        if prev_round[i] != curr_round[i]:
            resEqual = False
            prev_round[i] = curr_round[i]
    if resEqual:
        break
print([i for i, v in enumerate(curr_round) if v == 1])
