'''
Read an integer value X (1 <= X <= 1000).  Then print the odd numbers from
1 to X, each one in a line, including X if is the case.

Input
The input will be an integer value.

Output
Print all odd values between 1 and X, including X if is the case.
'''

m_InputValue = int(input())

if m_InputValue >= 1 and m_InputValue <= 1000:
    for i in range(m_InputValue):
        if not (i+1) % 2 == 0:
            print(i+1)
