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
            assert i in PVAR
        self.term = varlist
        self.decimal = self.toDecimal()
        self.length = len(varlist)

    def setVar(self, i, ni):  # GETEST
        if ni not in PVAR or i >= self.length:
            print("exception")
            return 0
        else:
            self.term[i] = ni

    def toDecimal(self):  #Getest: werkt niet voor geminimaliseerde p-termen
        res = 0
        l = len(self.term) - 1
        for i in self.term:
            res += i * (2 ** l)
            l -= 1
        return res

    def getDecimal(self):
        return self.decimal

    def equal(self, pother):  # GETEST
        return self.term == pother.term

    def differAt(self, term2):  # GETEST
        if self.length != term2.length:
            print("exception")
            return 0
        res = []
        for i in range(self.length):
            if self.term[i] != term2.term[i] and (self.term[i] == 1 or term2.term[i] == 1) and (self.term[i] == 0 or term2.term[i] == 0):
                res.append(i)
        return res

    def countOnes(self):  # GETEST
        counter = 0
        for i in self.term:
            if i == 1:
                counter += 1
        return counter

    def AvgVarTruePerStarterm(self):
        return self.countOnes()/self.length




    def countZeros(self):
        counter = 0
        for i in self.term:
            if i == 0:
                counter += 1
        return counter

def AvgVarTrue(self):

    

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


#################
#   TESTCASES   #
#################


def test():
    p1 = Pterm([1, 0, -1, 1, 0, 0])
    p2 = Pterm([1, 0, -1, 1, 0, 1])
    p3 = Pterm([1, 0, 1, 0, -1, 0])
    assert p1.length == 6
    assert p1.countOnes() == 2
    assert p2.countOnes() == 3
    assert p3.countOnes() == 2
    assert p1.differAt(p2) == [5]

    p1.setVar(5, 1)
    print(p1,p3)
    assert p1.equal(p2)
    assert p1.setVar(4, 3) == 0
    assert p1.setVar(6, 1) == 0
    p1c = p1.__copy__()
    assert p1c != p1
    assert p1c.equal(p1)
    assert p1.differAt(p1c) == []
    p4 = Pterm([1,0,1,0,1])
    p5 = Pterm([1,1,0,0,0,1])
    assert p4.decimal == 21
    assert p5.decimal == 49

def main():
    test()


if __name__ == '__main__':
    main()