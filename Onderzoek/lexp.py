from Onderzoek.pterm import *

#########################
#   Logic expressions   #
#########################

#   Een logische expressie wordt voorgesteld met de klasse LExp. Deze klasse heeft
#   1 veld self.terms. Dit is een lijst van Ptermen

class LExp:

    #   Geeft een nieuwe expressie terug met de gegeven ptermen
    def __init__(self, pTerms):  # GETEST
        try:
            varCount = pTerms[0].length
            for pterm in pTerms:
                assert type(pterm) == Pterm
                assert(pterm.length == varCount)
            self.terms = pTerms
        except Exception as e:
            assert e.__str__() == "list index out of range"
        finally:
            self.terms = pTerms

    #   Geeft het aantal ptermen terug
    def countPterms(self):
        counter = 0
        for i in self.terms:
            counter += 1
        return counter

    #   Geeft het aantal variabelen in de expressie
    def countVariables(self):
        if self.countPterms() > 0:
            return self.terms[0].length
        return None

    #   Het gemiddeld aantal variabelen (dat 1 of 0 zijn) per term
    def averageVarPerTerm(self):
        varCounter = 0
        for i in self.terms:
            varCounter += i.countOnes()
            varCounter += i.countZeros()
        termCount = self.countPterms()
        if termCount == 0:
            return 0
        return varCounter / termCount

    #   Veranderd de i-de variabelen in pterm term naar ni
    def changeTerm(self, term, i, ni):
        if self.containsTerm(term):
            self.removeTerm(term)
            term.setVar(i, ni)
            self.appendTerm(term)

    #   Verwijdert pterm term uit de expressie
    def removeTerm(self, term):  # GETEST
        for origterm in self.terms:
            if origterm.equal(term):
                self.terms.remove(origterm)

    #   Voegt pterm term toe aan de expressie
    def appendTerm(self, term):  # GETEST
        self.terms.append(term)

    #   Geeft true terug wanneer de expressie pterm term bevat
    def containsTerm(self, term):  # GETEST
        found = False
        for origterm in self.terms:
            if origterm.equal(term):
                found = True
                break
        return found

    #   Geeft een expressie terug die dezelfde logische uitdrukking voorstelt maar
    #   waar elke term een toekenning (1 of 0) heeft voor elke variabelen
    def expand(self):
        res = LExp([])
        for term in self.terms:
            if term.countValue(-1) > 0:
                expandedTerms = term.expand()
                for expandedTerm in expandedTerms:
                    res.appendTerm(expandedTerm)
            else:
                res.appendTerm(term)

        if res.isExpanded():
            return res
        return res.expand()

    #   Geeft true terug wanneer elke term een toekenning heeft (0 of 1) voor elke variabelen
    def isExpanded(self):
        for term in self.terms:
            if term.countValue(-1) > 0:
                return False
        return True

    #   Geeft true terug wanneer de expressies dezelfde termen bevatten (volgorde maakt niet uit)
    def equal(self, other):  # GETEST
        if type(other) != LExp:
            return False
        if len(self.terms) != len(other.terms):
            return False
        for i in self.terms:
            if not other.containsTerm(i):
                return False
        return True

    #   Geeft een kopies terug van de expressies, met kopies van de ptermen
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