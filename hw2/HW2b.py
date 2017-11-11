#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-11-12 01:40
# Last Modified:  2017-11-12 02:30
# Filename:       HW2b.py
# ==========================================================================
from enum import Enum
import random


class CHO(Enum):
    njoin = 0
    join = 1


nPoints = int(raw_input())
Graph = []
weight = [i for i in map(int, raw_input().split())]
for i in range(0, nPoints):
    Graph.append({'id': i,
                  'weight': weight[i],
                  'edge': map(int, raw_input().split())})

# prev_round = [CHO.njoin] * nPoints
prev_round = [None] * nPoints
for i in range(0, nPoints):
    prev_round[i] = random.choice([CHO.join, CHO.njoin])
curr_round = [CHO.njoin] * nPoints


# init
for i in range(0, nPoints):
    neighbors = [idx for idx, val in enumerate(Graph[i]['edge'])
                 if val == 1]
    neiPrevState = [prev_round[n] for n in neighbors]
    # Compare with neighbors to decide join or not
    joinMWIS = True
    ti = float(Graph[i]['weight'])/float(Graph[i]['edge'].count(1)+1)
    for n in neighbors:
        tn = float(Graph[n]['weight'])/float(Graph[n]['edge'].count(1)+1)
        if tn >= ti and prev_round[n] == CHO.join:
            joinMWIS = False
            break
    curr_round[i] = CHO.join if joinMWIS else CHO.njoin
print("random input:")
print([i.value for i in curr_round])


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
        joinMWIS = True
        ti = float(Graph[i]['weight'])/float(Graph[i]['edge'].count(1)+1)
        for n in neighbors:
            tn = float(Graph[n]['weight'])/float(Graph[n]['edge'].count(1)+1)
            if tn >= ti and prev_round[n] == CHO.join:
                joinMWIS = False
                break
        curr_round[i] = CHO.join if joinMWIS else CHO.njoin
print([i for i, v in enumerate(curr_round) if v == CHO.join])
