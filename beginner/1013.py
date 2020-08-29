'''
Make a program that reads 3 integer values and present the greatest one
followed by the message "eh o maior". Use the following formula:
'''

m_Int1, m_Int2, m_Int3 = input().split()
m_Int1, m_Int2, m_Int3 = int(m_Int1), int(m_Int2), int(m_Int3)

m_Maior = int((m_Int1+m_Int2+abs(m_Int1-m_Int2))/2)
m_Maior = int((m_Maior+m_Int3+abs(m_Maior-m_Int3))/2)

print('{} eh o maior'.format(m_Maior))
