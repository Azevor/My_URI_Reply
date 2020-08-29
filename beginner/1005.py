'''
Read two floating points' values of double precision A and B, corresponding to
two student's grades. After this, calculate the student's average, considering
that grade A has weight 3.5 and B has weight 7.5. Each grade can be from zero
to ten, always with one digit after the decimal point.
'''

m_N1 = float(input())
m_N2 = float(input())
m_Pounds = 3.5+7.5

m_N1 = m_N1*3.5
m_N2 = m_N2*7.5

print('MEDIA = {:.5f}'.format((m_N1+m_N2)/m_Pounds))
