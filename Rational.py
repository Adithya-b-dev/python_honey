class Rational:
    def __init__(self,numerator,denominator):
        if denominator==0:
            print("Denominator cannot be zero.")

        self.numerator=numerator
        self.denominator=denominator
        self._reduce()

    def _gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return abs(a)

    def _reduce(self):
        gcd=self._gcd(self.numerator,self.denominator)
        self.numerator//=gcd
        self.denominator//=gcd

    def __str__(self):
        return (f"{self.numerator}/{self.denominator}")

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def __add__(self,other):
        new_num=(self.numerator*other.denominator)+(self.denominator*other.numerator)
        new_den=self.denominator*other.denominator
        return Rational(new_num,new_den)

    def __sub__(self,other):
        new_num=(self.numerator*other.denominator)-(self.denominator*other.numerator)
        new_den=self.denominator*other.denominator
        return Rational(new_num,new_den)

    def __mul__(self,other):
        new_num=self.numerator*other.numerator
        new_den=self.denominator*other.denominator
        return Rational(new_num,new_den)

    def __eq__(self,other):
        return (self.numerator==other.numerator and self.denominator==other.denominator)

    def __lt__(self,other):
        return (self.numerator*other.denominator < other.numerator*self.denominator)

    def __gt__(self,other):
        return (self.numerator*other.denominator > other.numerator*self.denominator)
