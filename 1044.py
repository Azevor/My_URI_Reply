'''
Read two integer values (A and B). After, the program should print the message
"Sao Multiplos" (are multiples) or "Nao sao Multiplos" (aren’t multiples),
corresponding to the read values.
'''

m_N1, m_N2 = input().split()
m_N1, m_N2 = int(m_N1), int(m_N2)

if m_N1 % m_N2 == 0 or m_N2 % m_N1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
