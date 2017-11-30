#!/usr/bin/env python
# ==========================================================================
# Author:         scps950707
# Email:          scps950707@gmail.com
# Created:        2017-11-29 17:32
# Last Modified:  2017-11-30 14:55
# Filename:       HW3c.py
# ==========================================================================
from enum import Enum
import random
from matplotlib import pyplot as plt


class CHO(Enum):
    njoin = 0
    join = 1


def comparePriority(i, neighbors, curr_round):
    ti = float(Graph[i]['weight']) / float(Graph[i]['edge'].count(1) + 1)
    for n in neighbors:
        tn = float(Graph[n]['weight']) / float(Graph[n]['edge'].count(1) + 1)
        if tn >= ti and curr_round[n] == CHO.join:
            return CHO.njoin
    return CHO.join


def MWIS(curr_round, p):
    checker = [False] * nPoints
    prev_sync_round = [CHO.njoin] * nPoints
    rounds = 0
    while True:
        rounds += 1
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
            end = True
            for i in range(0, nPoints):
                if curr_round[i] != prev_sync_round[i]:
                    prev_sync_round[i] = curr_round[i]
                    end = False
            if end:
                break
            else:
                checker = [False] * nPoints
    # print([idx for idx, v in enumerate(curr_round) if v == CHO.join])
    mwis = [idx for idx, v in enumerate(curr_round) if v == CHO.join]
    # print(mwis)
    totalW = sum([Graph[i]['weight'] for i in mwis])
    return rounds, totalW


if __name__ == "__main__":
    nPoints = int(raw_input())
    Graph = []
    weight = [i for i in map(int, raw_input().split())]
    for i in range(0, nPoints):
        Graph.append({'id': i,
                      'weight': weight[i],
                      'edge': map(int, raw_input().split())})
    testTimes = 1000
    pointsX = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    arrR = []
    arrW = []
    for p in range(1, 10):
        totalRounds = 0
        totalWeights = 0
        for i in range(0, testTimes):
            curr_round = []
            for j in range(0, nPoints):
                curr_round.append(random.choice([CHO.join, CHO.njoin]))
            r, w = MWIS(curr_round, p)
            totalRounds += r
            totalWeights += w
        averRounds = float(totalRounds) / float(testTimes)
        arrR.append(averRounds)
        averWeight = float(totalWeights) / float(testTimes)
        arrW.append(averWeight)
        print("p:0." + str(p))
        print("average rounds:" + str(averRounds))
        print("average weight:" + str(averWeight))
    plt.figure(1)
    plt.plot(pointsX, arrR)
    plt.grid(b=True, which='major', color='k', linestyle='--')
    plt.figure(2)
    plt.plot(pointsX, arrW)
    plt.grid(b=True, which='major', color='k', linestyle='--')
    plt.show()
