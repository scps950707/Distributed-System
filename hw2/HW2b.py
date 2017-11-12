#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-11-12 01:40
# Last Modified:  2017-11-12 16:21
# Filename:       HW2b.py
# ==========================================================================
from enum import Enum
import itertools


class CHO(Enum):
    njoin = 0
    join = 1


def comparePriority(i, neighbors):
    ti = float(Graph[i]['weight'])/float(Graph[i]['edge'].count(1)+1)
    for n in neighbors:
        tn = float(Graph[n]['weight'])/float(Graph[n]['edge'].count(1)+1)
        if tn >= ti and prev_round[n] == CHO.join:
            return CHO.njoin
    return CHO.join


def MWIS(prev_round, curr_round):
    # init
    for i in range(0, nPoints):
        neighbors = [idx for idx, val in enumerate(Graph[i]['edge'])
                     if val == 1]
        # Compare with neighbors to decide join or not
        curr_round[i] = comparePriority(i, neighbors)

    loops = 1
    notStop = False
    while True:
        if loops > 20:
            print("not stop")
            notStop = True
            break
        loops += 1
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
    if not notStop:
        print([i for i, v in enumerate(curr_round) if v == CHO.join])


if __name__ == "__main__":
    nPoints = int(raw_input())
    Graph = []
    weight = [i for i in map(int, raw_input().split())]
    for i in range(0, nPoints):
        Graph.append({'id': i,
                      'weight': weight[i],
                      'edge': map(int, raw_input().split())})
    for seq in itertools.product([CHO.njoin, CHO.join], repeat=nPoints):
        prev_round = list(seq)
        curr_round = [CHO.njoin] * nPoints
        MWIS(prev_round, curr_round)
