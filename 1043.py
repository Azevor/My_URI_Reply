'''
Read three point floating values (A, B and C) and verify if is possible to
make a triangle with them. If it is possible, calculate the perimeter of the
triangle and print the message:

Perimetro = XX.X


If it is not possible, calculate the area of the trapezium which basis
A and B and C as height, and print the message:

Area = XX.X
'''


class Calculate:

    def validTriangle(self, p_A, p_B, p_C):
        if p_A+p_B > p_C and p_A+p_C > p_B and p_B+p_C > p_A:
            return True
        else:
            return False

    def calcPerimeter(self, p_A, p_B, p_C):
        return p_A+p_B+p_C

    def calcAreaTrapeze(self, p_A, p_B, p_C):
        return (p_A+p_B)*p_C/2


if __name__ == '__main__':
    v_Obj = Calculate()

    v_ValueA, v_ValueB, v_ValueC = input().split()
    v_ValueA, v_ValueB, v_ValueC = round(float(v_ValueA), 1), round(
        float(v_ValueB), 1), round(float(v_ValueC), 1)

    if v_Obj.validTriangle(v_ValueA, v_ValueB, v_ValueC):
        print('Perimetro = {:.1f}'.format(
            v_Obj.calcPerimeter(v_ValueA, v_ValueB, v_ValueC)))
    else:
        print('Area = {:.1f}'.format(
            v_Obj.calcAreaTrapeze(v_ValueA, v_ValueB, v_ValueC)))
