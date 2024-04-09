#################
#   generator   #
#################

import random
import time
import csv

from Onderzoek.McCLUSKEY import *


PVAR = [-1, 0, 1]


def generator():  # returnt een random LExp met random grootte
    res = LExp([])
    aantalVariabelen = 8
    randomGrens = random.randint(64,127)
    while randomGrens > 0:
        newTerm = make_pterm(aantalVariabelen)
        if not res.containsTerm(newTerm):
            res.appendTerm(newTerm)
            randomGrens -= 1
    return res


def make_pterm(aantalVariabelen):  # make a random pterm
    pterm = []
    for i in range(0, aantalVariabelen):
        randomIndex = random.randint(1, 2)
        pterm.append(PVAR[randomIndex])
    return Pterm(pterm)


def main():
    with open('dataOnderzoek.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["#PtermenStart", "ResPterms", "AvgVar/eindTerm", "Time", "AvgVarTrue/StartTerm"])
        i = 0
        while True:
            Expression = generator()
            decimals = Expression.toDecimals()
            startPterms = Expression.countPterms()

            AvgVarTruePerStartTerm = Expression.averageVarTruePerStartterm()
        #    varCount = Expression.countVariables()
        #   maxPterms = 2**varCount
            startTime = time.time()
            print("Counter: {}, Start Ptermen: {}, decimalen: {} ".format(i, startPterms, decimals))
            vereenvoudigd = mcCluskey(Expression)
            endTime = time.time()
            elapsedTime = endTime - startTime
            endPterms = vereenvoudigd.countPterms()
            avgVarPerTerm = vereenvoudigd.averageVarPerTerm()
            record = [startPterms, endPterms, avgVarPerTerm, elapsedTime, AvgVarTruePerStartTerm] + decimals
            writer.writerow(record)
            i += 1


main()
