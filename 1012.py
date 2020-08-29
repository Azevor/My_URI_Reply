'''
Make a program that reads three floating point values: A, B and C. Then,
calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.
'''

m_PI = 3.14159
m_ValueA, m_ValueB, m_ValueC = input().split()
m_ValueA, m_ValueB, m_ValueC = float(
    m_ValueA), float(m_ValueB), float(m_ValueC)

print('TRIANGULO: {:.3f}'.format(m_ValueA*m_ValueC/2))
print('CIRCULO: {:.3f}'.format(m_PI*m_ValueC**2))
print('TRAPEZIO: {:.3f}'.format((m_ValueA+m_ValueB)*m_ValueC/2))
print('QUADRADO: {:.3f}'.format(m_ValueB**2))
print('RETANGULO: {:.3f}'.format(m_ValueA*m_ValueB))
