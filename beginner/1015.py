'''
Read the four values corresponding to the x and y axes of two points in the
plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them,
showing four decimal places after the comma, according to the formula.
'''

from math import sqrt

m_X1, m_Y1 = input().split()
m_X2, m_Y2 = input().split()

m_X1, m_X2, m_Y1, m_Y2 = float(m_X1), float(m_X2), float(m_Y1), float(m_Y2)
m_Dist = sqrt(((m_X2-m_X1)**2)+((m_Y2-m_Y1)**2))

print('{:.4f}'.format(m_Dist))
