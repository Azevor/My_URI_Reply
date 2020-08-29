'''
Read two integer values X and Y. Print the sum of all odd values between them.

Input
The input file contain two integer values.

Output
The program must print an integer number. This number is the sum off all odd
values between both input values that must fit in an integer number.
'''

m_InputX = int(input())
m_InputY = int(input())
m_OddSum = 0


if m_InputY % 2 == 0:
    m_InputY += 1
else:
    m_InputY += 2

for i in range(m_InputY, m_InputX, 2):
    print("i:", i)
    m_OddSum += i

print(m_OddSum)
