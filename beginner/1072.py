'''
Read an integer N. This N will be the number of integer numbers X that
will be read.

Print how many these numbers X are in the interval [10,20] and how many
values are out of this interval.

Input
The first line of input is an integer N (N < 10000), that indicates the
total number of test cases.
Each case is an integer number X (-107 < X < 107).

Output
For each test case, print how many numbers are in and how many values are
out of the interval.
'''

m_InputN = int(input())
m_InputX = []
m_In, m_Out = 0, 0
m_Min, m_Max = 10, 20

if m_InputN > 0:
    for i in range(m_InputN):
        m_InputX.append(int(input()))

for i in m_InputX:
    if i >= m_Min and i <= m_Max:
        m_In += 1
    else:
        m_Out += 1

print("{} in".format(m_In))
print("{} out".format(m_Out))
