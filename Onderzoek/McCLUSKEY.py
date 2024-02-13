#################
#   p-termen    #
#################

#   Een p-term wordt voorgesteld door een lijst met lengte n (de variabelen). Een element in de lijst
#   mag 3 verschillende waarden hebben in de lijst: (Hiervoor globale variabele PVAR)
#       -   1  : de variabele komt voor in de p-term
#       -   0  : de negatie van de variabele komt voor in de p-term
#       -   -1 : de variabele komt niet voor in de p-term (maakt niet uit welke waarde die heeft)
#   Het eerste element in de lijst stelt variabele x_0 voor, het tweede x_1, en zo verder.

PVAR = [-1, 0, 1]
class Pterm:
    def __init__(self, varlist):
        for i in varlist:
            if i not in PVAR:
                print("exception")
                return 0
        self.term = varlist
        self.length = len(varlist)

    def set_var(self, i, ni):
        if ni not in [-1,0,1] or i >= self.length:
            print("exception")
            return 0
        else:
            self.term[i] = ni

    def equal(self, pother):
        return self.term == pother.term

    def differAt(self, term2):
        if self.length != term2.length:
            print("exception")
            return 0
        differ = []
        for i in range(self.length):
            if self.term[i] != term2.length[i]:
                differ.append[i]
        return differ

def test():
    p1 = Pterm([1,0,-1,1,0,0])
    p2 = Pterm([1,0,-1,1,0,1])
    assert p1.length == 6
    p1.set_var(5,1)
    assert p1.equal(p2)
    assert p1.set_var(4,3) == 0
    assert p1.set_var(6,1) == 0

def main():
    test()

main()
#################
#   Algoritme   #
#################

def mcCluskey(canExp):
    table = makeSortedDict(canExp)      #Sorteer elementen op het aantal eentjes
    i = 0
    while i < len(table):
        for term1 in table[i]:
            for term2 in table[i + 1]:
                differ = term1.differAt(term2)
                if len(differ) == 1:
                    term12 = reduce(term1, term2, differ[0])



def makeSortedDict(canExp):
    res = dict()
    for i in canExp:
        counti = i.countOnes()
        if counti not in res:
            dict[counti] = [i]
        else:
            dict[counti].add(i)
    return res

def reduce(term1, term2, i):
    if term1.length != term2.length:
        print("exception")
        return 0
    varlist = []
    for j in range(term1.length):
        if j == i:
            varlist.append(-1)
        else:
            varlist.append(term1.term[1])

#################
#   Testcases   #
#################