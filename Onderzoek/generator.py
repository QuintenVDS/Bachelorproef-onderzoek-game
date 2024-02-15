#################
#   generator   #
#################
import random
from Onderzoek.McCLUSKEY import *

PVAR = [-1, 0, 1]

def generator():           # returnt een random LExp met random grootte
    Pterms = []
    randomGrens = random.randint(1, 100)
    aantalVariabelen = random.randint(1, 100)
    for i in range(0, randomGrens):
        Pterms.append(make_pterm(aantalVariabelen))
    return LExp(Pterms)
  

def make_pterm(aantalVariabelen): # make a random pterm
    pterm = []
    randomIndex = random.randint(0, 2)
    for i in range(0, aantalVariabelen):
        randomIndex = random.randint(0, 2)
        pterm.append(PVAR[randomIndex])
    return Pterm(pterm)
   
def main():
    Expression = generator()
    vereenvoudigd = mcCluskey(Expression)
    print(Expression, vereenvoudigd)
    


main()
