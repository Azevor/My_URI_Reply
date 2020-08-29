'''
Read three values (variables A, B and C), which are the three student's grades.
Then, calculate the average, considering that grade A has weight 2, grade B has
weight 3 and the grade C has weight 5. Consider that each grade can go from 0
to 10.0, always with one decimal place.
'''

m_N1 = float(input())*2
m_N2 = float(input())*3
m_N3 = float(input())*5
m_Pound = 2+3+5

print('MEDIA = {:.1f}'.format((m_N1+m_N2+m_N3)/m_Pound))
