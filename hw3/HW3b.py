#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-11-29 17:27
# Last Modified:  2017-12-02 17:35
# Filename:       HW3b.py
# ==========================================================================
from enum import Enum
import random


class CHO(Enum):
    njoin = 0
    join = 1


def comparePriority(i, neighbors, curr_round):
    ti = float(Graph[i]['weight'])/float(Graph[i]['edge'].count(1)+1)
    for n in neighbors:
        tn = float(Graph[n]['weight'])/float(Graph[n]['edge'].count(1)+1)
        if tn >= ti and curr_round[n] == CHO.join:
            return CHO.njoin
    return CHO.join


def MWIS(curr_round, p):
    checker = [False] * nPoints
    prev_sync_round = [CHO.njoin] * nPoints
    dupCnt = 0
    while True:
        for i in range(0, nPoints):
            if random.randint(1, 10) > p:
                continue
            checker[i] = True
            neighbors = [idx for idx, val in enumerate(Graph[i]['edge'])
                         if val == 1]
            neiPrevState = [curr_round[n] for n in neighbors]

            # All neighbors not join MWIS
            if neiPrevState.count(CHO.join) == 0:
                curr_round[i] = CHO.join
            else:
                # Compare with neighbors to decide join or not
                curr_round[i] = comparePriority(i, neighbors, curr_round)
        if checker.count(True) == nPoints:
            dup = True
            for i in range(0, nPoints):
                if curr_round[i] != prev_sync_round[i]:
                    prev_sync_round[i] = curr_round[i]
                    dup = False
            if dup:
                dupCnt += 1
                if dupCnt > 2:
                    break
            checker = [False] * nPoints
    print([idx for idx, v in enumerate(curr_round) if v == CHO.join])


if __name__ == "__main__":
    nPoints = int(raw_input())
    Graph = []
    weight = [i for i in map(int, raw_input().split())]
    for i in range(0, nPoints):
        Graph.append({'id': i,
                      'weight': weight[i],
                      'edge': map(int, raw_input().split())})
    totalRounds = 0
    p = 5
    for i in range(0, 1000):
        curr_round = []
        for j in range(0, nPoints):
            curr_round.append(random.choice([CHO.join, CHO.njoin]))
        MWIS(curr_round, p)
