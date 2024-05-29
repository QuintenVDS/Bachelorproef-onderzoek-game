#################
#   generator   #
#################

import random
import time
import csv

from Onderzoek.McCLUSKEY import *

#   De waarde die de variabelen van een pterm kunnen aannemen
PVAR = [-1, 0, 1]

#   Het aantal variabelen waarmee expressies worden gegenereed
VARCOUNT = 8

#   De kans dat een variabele in de gegenereerde pterm op false (= 0) wordt gezet
CHANCE_FALSE = 0.5


#   Geeft een random expressie terug met een willekeurig aantal ptermen (tussen 1 en 2 ^ VARCOUNT)
def generator():
    res = LExp([])
    randomGrens = random.randint(1, 2**VARCOUNT)
    while randomGrens > 0:
        newTerm = make_pterm()
        if not res.containsTerm(newTerm):
            res.appendTerm(newTerm)
            randomGrens -= 1
    return res


#   Geeft een willekeurige pterm terug
def make_pterm():  # make a random pterm
    pterm = []
    for i in range(0, VARCOUNT):
        variabele = random.random()
        if variabele >= CHANCE_FALSE:
            variabele = 1
        else:
            variabele = 0
        pterm.append(variabele)
    return Pterm(pterm)


#   Een onneindige loop die random expressies genereerd, deze oplost met mcCluskey, en resultaten
#   hiervan schrijft naar een csv file
def main():
    with open('dataOnderzoek.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["#PtermenStart", "ResPterms", "AvgVar/eindTerm", "Time"])
        i = 0
        while True:
            Expression = generator()
            startPterms = Expression.countPterms()
            startTime = time.time()
            print("Counter: {}, Start Ptermen: {}".format(i, startPterms))
            vereenvoudigd = mcCluskey(Expression)
            endTime = time.time()
            elapsedTime = endTime - startTime
            endPterms = vereenvoudigd.countPterms()
            avgVarPerTerm = vereenvoudigd.averageVarPerTerm()
            record = [startPterms, endPterms, avgVarPerTerm, elapsedTime]
            writer.writerow(record)
            i += 1


main()
