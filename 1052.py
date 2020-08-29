'''
Read an integer number between 1 and 12, including. Corresponding to this
number, you must print the month of the year, in english, with the first
letter in uppercase.
'''

m_Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December']
m_Input = int(input())

print(m_Month[m_Input-1])
