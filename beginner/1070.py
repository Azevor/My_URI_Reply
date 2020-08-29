'''
Read an integer value X and print the 6 consecutive odd numbers from X,
a value per line, including X if it is the case.

Input
The input will be a positive integer value.

Output
The output will be a sequence of six odd numbers.
'''

m_InputValue = int(input())

if m_InputValue > 0:
    if m_InputValue % 2 == 0:
        m_InputValue += 1
    for i in range(m_InputValue, m_InputValue+12, 2):
        print(i)
