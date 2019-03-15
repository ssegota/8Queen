# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:51:35 2019

@author: Student
"""

import numpy as np
import operator
import matplotlib.pyplot as plt


class gene(object):
    def __init__(self, fitness, moves):
        self.fitness = fitness
        self.moves = moves

#Fills the axes and diagonals of position (x,y) on board b with ones
def fillBoard(b, x, y):
    #fill axes
    b[:, x] = 1
    b[y, :] = 1
    #copy x,y values
    newx = x
    newy = y

    #Fill diagonals
    i = 0
    while newy-i > 0 and newx-i > 0:
        i += 1
        b[newy-i][newx-i] = 1
    i = 0
    while newy+i < 7 and newx-i > 0:
        i += 1
        b[newy+i][newx-i] = 1
    i = 0
    while newy+i < 7 and newx+i < 7:
        i += 1
        b[newy+i][newx+i] = 1
    i = 0
    while newy-i > 0 and newx+i < 7:
        i += 1
        b[newy-i][newx+i] = 1
    return b

def crossGenes(gene1, gene2):
    startFit=0
    moves = []
    for i in range(8):
        #Random mutation probability 1/1000
        
        if np.random.randint(1000) == 0:
            #print("assign a random value to the moves")
            moves.append([np.random.randint(0, 8), np.random.randint(0, 8)])
            continue
        
        #IF one is (0,0) 
        if (gene1.moves[i][0] == 0 and gene1.moves[i][1] == 0) and ((gene2.moves[i][0] != 0 or gene2.moves[i][1] != 0)):
            #print("Use move from 2")
            moves.append(gene2.moves[i])
            continue
        if (gene2.moves[i][0] == 0 and gene2.moves[i][1] == 0) and ((gene1.moves[i][0] != 0 or gene1.moves[i][1] != 0)):
            #print("Use move from 1")
            moves.append(gene1.moves[i])
            continue
        #otherwise toss a coin to pick between the two
        if np.random.randint(2)==0:
            #print("Choose gene 1")
            moves.append(gene1.moves[i])
            continue
        else:
            #print("Choose gene 2")
            moves.append(gene2.moves[i])
            continue

        

        
        print(gene1.moves[i])
        print(gene2.moves[i])
        
    #print("MOVES", moves)

#GENERATE STARTING POPULATION
population = []
for i in range(1000):
    b = np.zeros((8,8))

    moves=np.zeros(shape=(8,2))

    for i in range(8):
        
        x=np.random.randint(0,8)
        y=np.random.randint(0,8)
        if b[x][y]==1:
            break
        moves[i][0]=y
        moves[i][1]=x
        b = fillBoard(b, x, y)
    #print(i)

    unit = gene(i,moves)
    #print(b)
    #print("Fitness:", unit.fitness)
    #print("Moveset:\n", unit.moves)
    population.append(unit)

for i in population:
    if i.fitness==7:
        print("Fitness:", i.fitness)
        print("Moveset:\n", i.moves)

print("-----")

sorted_pop = sorted(population, key=operator.attrgetter('fitness'))

for i in sorted_pop:
    print("Fitness:", i.fitness)
    print("Moveset:\n", i.moves)

#START CROSSING

#For a number(ne population)
#randomly pick two genes
#cross them
arr = np.arange(0,1001)
prob = np.exp(arr/1000)
rand_draw1 = np.random.choice(arr, 1, p=prob/sum(prob))
rand_draw2 = np.random.choice(arr, 1, p=prob/sum(prob))

print(rand_draw1, rand_draw2)
crossGenes(population[12], population[36])
