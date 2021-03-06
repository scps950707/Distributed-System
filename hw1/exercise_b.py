#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-10-26 15:13
# Last Modified:  2017-11-12 15:54
# Filename:       exercise_b.py
# ==========================================================================
from enum import Enum


class CHO(Enum):
    njoin = 0
    join = 1


def comparePriority(i, neighbors):
    ti = float(Graph[i]['weight'])/float(Graph[i]['edge'].count(1)+1)
    for n in neighbors:
        tn = float(Graph[n]['weight'])/float(Graph[n]['edge'].count(1)+1)
        if tn > ti or (tn == ti and i > n):
            return CHO.njoin
    return CHO.join


nPoints = int(raw_input())
Graph = []
weight = [i for i in map(int, raw_input().split())]
for i in range(0, nPoints):
    Graph.append({'id': i,
                  'weight': weight[i],
                  'edge': map(int, raw_input().split())})

prev_round = [CHO.njoin] * nPoints
curr_round = [CHO.njoin] * nPoints


# init
for i in range(0, nPoints):
    neighbors = [idx for idx, val in enumerate(Graph[i]['edge'])
                 if val == 1]
    neiPrevState = [prev_round[n] for n in neighbors]
    # Compare with neighbors to decide join or not
    curr_round[i] = comparePriority(i, neighbors)


while True:
    # Compare curr and prev and also copy curr result to prev
    end = True
    for i in range(0, nPoints):
        if prev_round[i] != curr_round[i]:
            end = False
            prev_round[i] = curr_round[i]
    if end:
        break
    for i in range(0, nPoints):
        neighbors = [idx for idx, val in enumerate(Graph[i]['edge'])
                     if val == 1]
        neiPrevState = [prev_round[n] for n in neighbors]

        # All neighbors not join MWIS
        if neiPrevState.count(CHO.join) == 0:
            curr_round[i] = CHO.join
            continue
        # Compare with neighbors to decide join or not
        curr_round[i] = comparePriority(i, neighbors)
print([i for i, v in enumerate(curr_round) if v == CHO.join])
