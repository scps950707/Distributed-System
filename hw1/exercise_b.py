#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-10-26 15:13
# Last Modified:  2017-11-11 20:57
# Filename:       exercise_b.py
# ==========================================================================
from enum import Enum


class CHO(Enum):
    nDecided = -1
    njoin = 0
    join = 1


nPoints = int(raw_input())
Graph = []
weight = [i for i in map(int, raw_input().split())]
for i in range(0, nPoints):
    Graph.append({'id': i,
                  'weight': weight[i],
                  'edge': map(int, raw_input().split())})

prev_round = [CHO.nDecided] * nPoints
curr_round = [CHO.nDecided] * nPoints

while True:
    for i in range(0, nPoints):
        # already decided
        if prev_round[i] == CHO.join or prev_round[i] == CHO.njoin:
            continue

        neighbors = [idx for idx, val in enumerate(Graph[i]['edge'])
                     if val == 1]
        neiPrevState = [prev_round[n] for n in neighbors]

        # All neighbors not join MWIS
        if len(neiPrevState) == neiPrevState.count(CHO.njoin):
            curr_round[i] = CHO.join
            continue
        # One of neighbors join MWIS so not join MWIS
        if CHO.join in neiPrevState:
            curr_round[i] = CHO.njoin
            continue
        # Compare with neighbors to decide join or not
        isMax = True
        ti = float(Graph[i]['weight'])/float(Graph[i]['edge'].count(1)+1)
        for n in neighbors:
            tn = float(Graph[n]['weight'])/float(Graph[n]['edge'].count(1)+1)
            if tn > ti or (tn == ti and i > n):
                isMax = False
        if isMax:
            curr_round[i] = CHO.join
    # Compare curr and prev and also copy curr result to prev
    end = True
    for i in range(0, nPoints):
        if prev_round[i] != curr_round[i]:
            end = False
            prev_round[i] = curr_round[i]
    if end:
        break
print([i for i, v in enumerate(curr_round) if v == CHO.join])
