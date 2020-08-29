'''
Read 3 double numbers (A, B and C) representing the sides of a triangle and
arrange them in decreasing order, so that the side A is the biggest of the
three sides. Next, determine the type of triangle that they can make, based
on the following cases always writing an appropriate message:

* if A ≥ B + C, write the message: NAO FORMA TRIANGULO
* if A² = B² + C², write the message: TRIANGULO RETANGULO
* if A² > B² + C², write the message: TRIANGULO OBTUSANGULO
* if A² < B² + C², write the message: TRIANGULO ACUTANGULO
* if the three sides are the same size, write the message: TRIANGULO EQUILATERO

if only two sides are the same and the third one is different,
write the message: TRIANGULO ISOSCELES
'''

m_Sides = input().split()

for i in range(len(m_Sides)):
    m_Sides[i] = round(float(m_Sides[i]), 1)

m_Sides.sort(reverse=True)

m_A, m_B, m_C = m_Sides[0], m_Sides[1], m_Sides[2]
m_A2, m_B2, m_C2 = m_A**2, m_B**2, m_C**2

if m_A < m_B+m_C:
    if m_A2 == m_B2+m_C2:
        print('TRIANGULO RETANGULO')
    if m_A2 > m_B2+m_C2:
        print('TRIANGULO OBTUSANGULO')
    if m_A2 < m_B2+m_C2:
        print('TRIANGULO ACUTANGULO')

    if m_A == m_B and m_B == m_C:
        print('TRIANGULO EQUILATERO')
    elif m_A == m_B or m_A == m_C or m_B == m_C:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
