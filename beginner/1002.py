'''
The formula to calculate the area of a circumference is defined as A = π . R2.
Considering to this problem that π = 3.14159:
'''

m_PI = 3.14159


def calcAreaCircle(p_R):
    return m_PI*p_R**2


print('A={:.4f}'.format(calcAreaCircle(float(input()))))
