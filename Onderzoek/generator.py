#################
#   generator   #
#################
import random
from Onderzoek.McCLUSKEY import *

PVAR = [-1, 0, 1]


def generator():  # returnt een random LExp met random grootte
    res = LExp([])
    aantalVariabelen = random.randint(1, 3)
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
    Expression = generator()
    vereenvoudigd = mcCluskey(Expression)
    print("Originele expressie: {} \nVereenvoudigde expressie: {}".format(Expression, vereenvoudigd))


main()
