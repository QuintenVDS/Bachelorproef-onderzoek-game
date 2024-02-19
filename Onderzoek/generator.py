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
    aantalVariabelen = random.randint(3, 5)
    randomGrens = random.randint(1, 2 ** aantalVariabelen)
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
        writer.writerow(["#PtermsStart", "VarCount", "MaxPterms", "#ResTerms", "AvgVar/Term", "Time"])
        i = 0
        while i < 10:
            Expression = generator()
            startPterms = Expression.countPterms()
            varCount = Expression.countVariables()
            maxPterms = 2**varCount
            startTime = time.time()
            vereenvoudigd = mcCluskey(Expression)
            endTime = time.time()
            elapsedTime = endTime - startTime
            endPterms = vereenvoudigd.countPterms()
            avgVarPerTerm = vereenvoudigd.averageVarPerTerm()
            print("#Ptermen: {}, #variabelen: {}, Max termen: {}, #ResPtermen: {}, AvgVar/ResPterm: {}, tijd: {}".format(startPterms, varCount, maxPterms, endPterms, avgVarPerTerm, elapsedTime))
            record = [startPterms, varCount, maxPterms, endPterms, avgVarPerTerm, elapsedTime]
            writer.writerow(record)
            i += 1

main()
