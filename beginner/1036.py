'''
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula.
If it's impossible to calculate the roots because a division by zero or a
square root of a negative number, presents the message “Impossivel calcular”.
'''

from math import sqrt


class Bhaskara:

    def calcDelta(self, p_ValueA, p_ValueB, p_ValueC):
        return p_ValueB**2-4*p_ValueA*p_ValueC

    def validDelta(self, p_DeltaValue):
        return p_DeltaValue > 0

    def calcRoots(self, p_ValueA, p_ValueB, p_DeltaValue):
        v_DeltaRoot = sqrt(p_DeltaValue)
        v_R1 = (-p_ValueB+v_DeltaRoot)/(2*p_ValueA)
        v_R2 = (-p_ValueB-v_DeltaRoot)/(2*p_ValueA)

        return v_R1, v_R2

    def calcBhaskara(self, p_ValueA, p_ValueB, p_ValueC):
        v_DeltaValue = -1

        if p_ValueA > 0.0:
            v_DeltaValue = self.calcDelta(p_ValueA, p_ValueB, p_ValueC)

        if self.validDelta(v_DeltaValue):
            v_R1, v_R2 = self.calcRoots(p_ValueA, p_ValueB, v_DeltaValue)
            print('R1 = {:.5f}'.format(v_R1))
            print('R2 = {:.5f}'.format(v_R2))
        else:
            print('Impossivel calcular')


if __name__ == '__main__':
    v_Calc = Bhaskara()
    v_A, v_B, v_C = input().split()
    v_A, v_B, v_C = float(v_A), float(v_B), float(v_C)

    v_Calc.calcBhaskara(v_A, v_B, v_C)
