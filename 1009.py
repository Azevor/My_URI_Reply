'''
Make a program that reads a seller's name, his/her fixed salary and the sale's
total made by himself/herself in the month (in money). Considering that this
seller receives 15% over all products sold, write the final salary (total) of
this seller at the end of the month , with two decimal places.
'''

m_SellerName = input()
m_Salary = float(input())
m_TotalMade = float(input())
m_Commission = 15

print('TOTAL = R$ {:.2f}'.format(m_Salary+(m_TotalMade*m_Commission/100)))
