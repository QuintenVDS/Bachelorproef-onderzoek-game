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
    def __init__(self, varlist):  # GETEST
        for i in varlist:
            if i not in PVAR:
                print("exception")
                return 0
        self.term = varlist
        self.length = len(varlist)

    def setVar(self, i, ni):  # GETEST
        if ni not in PVAR or i >= self.length:
            print("exception")
            return 0
        else:
            self.term[i] = ni

    def equal(self, pother):  # GETEST
        return self.term == pother.term

    def differAt(self, term2):  # GETEST
        if self.length != term2.length:
            print("exception")
            return 0
        res = []
        for i in range(self.length):
            if self.term[i] != term2.term[i]:
                res.append(i)
        return res

    def countOnes(self):  # GETEST
        counter = 0
        for i in self.term:
            if i == 1:
                counter += 1
        return counter

    def __copy__(self):  # GETEST
        return Pterm(self.term.copy())

    def __str__(self):  # GETEST
        res = ""
        for i in range(self.length):
            if self.term[i] == 1:
                res += "x{} ".format(str(i + 1))
            elif self.term[i] == 0:
                res += "x{}' ".format(str(i + 1))
        return res


#########################
#   Logic expressions   #
#########################

class LExp:
    def __init__(self, PTerms):  # GETEST
        for pterm in PTerms:
            assert type(pterm) == Pterm
        self.terms = PTerms
        self.varCount = PTerms[0].length

    def changeTerm(self, term, i, ni):
        self.removeTerm(term)
        term.setVar(i, ni)
        self.appendTerm(term)

    def setTerms(self, nterms):  # GETEST
        self.terms = nterms

    def removeTerm(self, term):  # GETEST
        for origterm in self.terms:
            if origterm.equal(term):
                self.terms.remove(origterm)

    def appendTerm(self, term):  # GETEST
        self.terms.append(term)

    def containsTerm(self, term):
        found = False
        for origterm in self.terms:
            if origterm.equal(term):
                found = True
                break
        return found

    def equal(self, other):  # GETEST
        if type(other) != LExp:
            return False
        if len(self.terms) != len(other.terms):
            return False
        for i in self.terms:
            found = False
            for j in other.terms:
                if i.equal(j):
                    found = True
            if found == False:
                return False
        return True

    def deepcopyExp(self):  # GETEST
        res = []
        for i in self.terms:
            newTerm = i.__copy__()
            res.append(newTerm)
        return LExp(res)

    def __str__(self):  # GETEST
        res = ""
        for i in range(len(self.terms)):
            if i != len(self.terms) - 1:
                res += "{}+ ".format(self.terms[i])
            else:
                res += "{}".format(self.terms[i])
        return res


#################
#   Algoritme   #
#################

def mcCluskey(canExp):
    newIter = True
    while newIter:
        table = makeTable(canExp.terms)  # Sorteer elementen op het aantal eentjes
        newTerms = canExp.deepcopyExp()
        for i in table:
            for term1 in table[i]:
                if i+1 in table:
                    for term2 in table[i + 1]:
                        differ = term1.differAt(term2)
                        if len(differ) == 1:
                            term12 = reduce(term1, term2, differ[0])
                            newTerms.removeTerm(term1)
                            newTerms.removeTerm(term2)
                            if not newTerms.containsTerm(term12):
                                newTerms.appendTerm(term12)
        if newTerms.equal(canExp):
            newIter = False
        else:
            canExp = newTerms
    return canExp


def makeTable(canExp):  # GETEST
    res = dict()
    for i in canExp:
        counti = i.countOnes()
        if counti not in res:
            res[counti] = [i]
        else:
            res[counti].append(i)
    return dict(sorted(res.items()))


def reduce(term1, term2, i):  # GETEST
    if term1.length != term2.length:
        print("exception")
        return 0
    varlist = []
    for j in range(term1.length):
        if j == i:
            varlist.append(-1)
        else:
            varlist.append(term1.term[j])
    return Pterm(varlist)


#################
#   Testcases   #
#################

def test():
    # class Pterm
    p1 = Pterm([1, 0, -1, 1, 0, 0])
    p2 = Pterm([1, 0, -1, 1, 0, 1])
    p3 = Pterm([1, 0, 1, 0, -1, 0])
    assert p1.length == 6
    assert p1.countOnes() == 2
    assert p2.countOnes() == 3
    assert p3.countOnes() == 2
    assert p1.differAt(p2) == [5]
    p1.setVar(5, 1)
    assert p1.equal(p2)
    assert p1.setVar(4, 3) == 0
    assert p1.setVar(6, 1) == 0
    p1c = p1.__copy__()
    assert p1c != p1
    assert p1c.equal(p1)
    assert p1.differAt(p1c) == []
    assert p1.differAt(p3) == [2, 3, 4, 5]
    # class LExp
    exp1 = LExp([Pterm([1, 0]), Pterm([1, 1])])
    exp2 = LExp([Pterm([1, -1]), Pterm([1, 0])])
    exp3 = LExp([Pterm([1, 1]), Pterm([1, 0])])
    exp1c = exp1.deepcopyExp()
    assert exp1 != exp1c
    assert exp1.terms != exp1c.terms
    assert exp1.equal(exp3)
    assert exp1.equal(exp1c)
    assert not exp1.equal(exp2)
    exp4 = LExp([Pterm([1, 0]), Pterm([1, 1]), Pterm([1, -1])])
    exp1.appendTerm((Pterm([1, -1])))
    assert exp4.equal(exp1)
    exp1.removeTerm(Pterm([1, 1]))
    assert exp2.equal(exp1)
    exp4.changeTerm(Pterm([1, -1]), 0, 0)
    exp5 = LExp([Pterm([1, 0]), Pterm([1, 1]), Pterm([0, -1])])
    assert exp4.equal(exp5)
    # Algoritme
    p12 = reduce(p1, p2, 5)
    assert p12.equal(Pterm([1, 0, -1, 1, 0, -1]))
    dict = makeTable(exp4.terms)
    assert dict[0][0].equal(Pterm([0, -1]))
    assert dict[1][0].equal(Pterm([1, 0]))
    assert dict[2][0].equal(Pterm([1, 1]))
    expTest1 = LExp([Pterm([1,1]), Pterm([1,0])])
    assert mcCluskey(expTest1).equal(LExp([Pterm([1,-1])]))
    expTest2 = LExp([Pterm([0,1,0]), Pterm([1,1,1]), Pterm([1,1,0]), Pterm([0,1,1]), Pterm([1,0,0])])
    print("McCLUSKEY op het voorbeeld dat wij altijd hebben gebruikt: \n {}".format(mcCluskey(expTest2)))
def main():
    test()


main()
