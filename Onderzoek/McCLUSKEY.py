from Onderzoek.lexp import *

#################
#   Algoritme   #
#################

def mcCluskey(canExp):  # GETEST
    newIter = True
    while newIter:
        table = makeTable(canExp.terms)  # Sorteer elementen op het aantal eentjes
        newTerms = canExp.deepcopyExp()
        for i in table:
            for term1 in table[i]:
                if i + 1 in table:
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
    p1 = Pterm([1, 0, -1, 1, 0, 0])
    p2 = Pterm([1, 0, -1, 1, 0, 1])
    p3 = Pterm([1, 0, 1, 0, -1, 0])
    p1.setVar(5, 1)
    p1c = p1.__copy__()
    exp1 = LExp([Pterm([1, 0]), Pterm([1, 1])])
    exp2 = LExp([Pterm([1, -1]), Pterm([1, 0])])
    exp3 = LExp([Pterm([1, 1]), Pterm([1, 0])])
    exp1c = exp1.deepcopyExp()
    exp4 = LExp([Pterm([1, 0]), Pterm([1, 1]), Pterm([1, -1])])
    exp4.changeTerm(Pterm([1, -1]), 0, 0)
    # Algoritme
    p12 = reduce(p1, p2, 5)
    assert p12.equal(Pterm([1, 0, -1, 1, 0, -1]))
    dict = makeTable(exp4.terms)
    assert dict[0][0].equal(Pterm([0, -1]))
    assert dict[1][0].equal(Pterm([1, 0]))
    assert dict[2][0].equal(Pterm([1, 1]))
    expTest1 = LExp([Pterm([1, 1]), Pterm([1, 0])])
    assert mcCluskey(expTest1).equal(LExp([Pterm([1, -1])]))
    expTest2 = LExp([Pterm([0, 1, 0]), Pterm([1, 1, 1]), Pterm([1, 1, 0]), Pterm([0, 1, 1]), Pterm([1, 0, 0])])
    assert mcCluskey(expTest2).equal(LExp([Pterm([1,-1,0]), Pterm([-1,1,-1])]))


def main():
    test()


if __name__ == '__main__':
    main()
