# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:51:35 2019

@author: Sandi Šegota
"""

###IMPORTS
import numpy as np
import operator
import matplotlib.pyplot as plt
###
MUTATION_CHANCE=100 #Lower the value higher chance of random mutation

#CLASSES
class gene(object):
    def __init__(self, fitness, moves):
        #Fitness of the gene
        self.fitness = fitness
        #moves - queens positions making up the gene
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

#crosses the genes
def crossGenes(gene1, gene2):
    startFit=0
    moves = []
    for i in range(8):
        #Random mutation probability 1/MUTATION_CHANCE
        
        if np.random.randint(MUTATION_CHANCE) == 0:
            #print("assign a random value to the moves")
            moves.append([np.random.randint(0, 8), np.random.randint(0, 8)])
            continue
        
        #IF one is (0,0) 
        if (gene1.moves[i][0] == 8 and gene1.moves[i][1] == 8) and ((gene2.moves[i][0] != 8 or gene2.moves[i][1] != 8)):
            #print("Use move from 2")
            moves.append(gene2.moves[i])
            continue
        if (gene2.moves[i][0] == 8 and gene2.moves[i][1] == 8) and ((gene1.moves[i][0] != 8 or gene1.moves[i][1] != 8)):
            #print("Use move from 1")
            moves.append(gene1.moves[i])
            continue
        
        #If both are zero append a random solution
        if (gene2.moves[i][0] == 8 and gene2.moves[i][1] == 8) and ((gene1.moves[i][0] == 8 and gene1.moves[i][1] == 8)):
                #print("Use move from 1")
            moves.append([np.random.randint(0, 8), np.random.randint(0, 8)])
            continue
        
        
        ###Choose a random gene
        #otherwise toss a coin to pick between the two
        if np.random.randint(2)==0:
            #print("Choose gene 1")
            moves.append(gene1.moves[i])
            continue
        else:
            #print("Choose gene 2")
            moves.append(gene2.moves[i])
            continue
                
        #print(gene1.moves[i])
        #print(gene2.moves[i])
        
    #print("MOVES", moves)
    return(moves)

def calculateFitness(moves, printBoard=False):
    b = np.full((8, 8), 8)
    fit=0
    while True:
        if fit==8:
            break
        if moves[fit][1]==8 or moves[fit][0]==8:
            break
        x = moves[fit][1]
        y = moves[fit][0]
        if b[y][x] == 1 or b[y][x] == 2:
            break
        b = fillBoard(b,x,y)
        b[y][x]=2
        fit+=1
    
    if printBoard:
        showBoard(b)
    return fit

def showBoard(b):
    print("Board:")
    print("\n")
    for i in range(8):
        for j in range(8):
            if b[i][j]==8 or b[i][j]==1:
                print(".", end='')
            else:
                print("Q", end='')
        print("\n")


###PROGRAM START

#GENERATE STARTING POPULATION
population = []
for i in range(1000):
    #Fill with a board and empty moveset with 8
    #8 represents an empty field
    b = np.full((8,8),8)
    moves=np.full((8,2),8)

    for i in range(8):
        #play a random move
        x=np.random.randint(0,8)
        y=np.random.randint(0,8)
        #if that position is filled, or under attack by a queen stop playing
        if b[y][x]==1:
            break
        #memorize the move
        moves[i][0]=y
        moves[i][1]=x
        #update the board with both the queen and new positions it attacks
        b = fillBoard(b, x, y)

    #create a gene with new random values
    unit = gene(i,moves)
    #place gene in population
    population.append(unit)

#sort the population
sorted_pop = sorted(population, key=operator.attrgetter('fitness'))


#START CROSSING

#For a number(ne population)
#randomly pick two genes
#cross them

generation_past = sorted_pop
generationCount = 0
fitness_per_gen = []

while True:
    #start a new generation
    generationCount+=1
    population_next = []

    for i in range(1000):
        #generate a new gene
        new_gene = gene(0, [])
        #b = np.zeros((8, 8))
        #pick genes for recombination, but weighted towards genes with a better fitness
        #As per:
        arr = np.arange(0,1000)
        prob = np.exp(arr/1000)
        rand_draw1 = np.random.choice(arr, 1, p=prob/sum(prob))
        rand_draw2 = np.random.choice(arr, 1, p=prob/sum(prob))
        #cross the randomly picked genes
        new_gene.moves = crossGenes(generation_past[rand_draw1[0]], generation_past[rand_draw2[0]])
        new_gene.fitness=calculateFitness(new_gene.moves)
        #add newly created gene in current population
        population_next.append(new_gene)
    #sort the new population
    population_next = sorted(population_next, key=operator.attrgetter('fitness'))
    #Add the best fitness to the array for plotting
    fitness_per_gen.append(population_next[999].fitness)
    #new generation becomes old
    generation_past=population_next
    #print current generation and best fitness in it
    print(generationCount, population_next[999].fitness)
    #if solution is found
    if population_next[999].fitness==8:
        #print the position of queens and show the board
        print("Positions of Queens:", population_next[999].moves)
        calculateFitness(population_next[999].moves, True)
        #exit the loop
        break

###GRAPH
#print the graph showing the fitness through generations
x = np.arange(0,len(fitness_per_gen),1)

plt.plot(x, fitness_per_gen)
plt.title("Fitness function for a \"8 Queen\" problem solved with an evolutionary algorithm")
plt.xlabel("Number of Generations")
plt.ylabel("Number of Queens placed on board")
plt.legend(["Fitness"])
plt.show()
