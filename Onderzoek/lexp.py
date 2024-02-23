from Onderzoek.pterm import *

#########################
#   Logic expressions   #
#########################

#   Een logische expressie wordt voorgesteld met de klasse LExp. Deze klasse heeft
#   1 veld self.terms. Dit is een lijst van Ptermen


class LExp:
    def __init__(self, PTerms):  # GETEST
        for pterm in PTerms:
            assert type(pterm) == Pterm
        self.terms = PTerms

    def toDecimals(self):
        res = []
        for i in range(2 ** 8):
            res.append(0)
        for term in self.terms:
            res[term.getDecimal()] = 1
        return res



    def countPterms(self):
        counter = 0
        for i in self.terms:
            counter += 1
        return counter

    def countVariables(self):
        if self.countPterms() > 0:
            return self.terms[0].length
        return None

    def averageVarPerTerm(self):
        varCounter = 0
        for i in self.terms:
            varCounter += i.countOnes()
            varCounter += i.countZeros()
        termCount = self.countPterms()
        if termCount == 0:
            return 0
        return varCounter / termCount

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

    def containsTerm(self, term):  # GETEST
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
            if not other.containsTerm(i):
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
#   TESTCASES   #
#################


def test():
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


def main():
    test()


if __name__ == '__main__':
    main()