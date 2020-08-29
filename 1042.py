'''
Read three integers and sort them in ascending order. After, print these
values in ascending order, a blank line and then the values in the sequence
as they were readed.
'''

m_Input = input().split()
m_Sorted = []

for i in range(len(m_Input)):
    m_Input[i] = int(m_Input[i])
    m_Sorted.append(m_Input[i])

m_Sorted.sort()

for i in range(len(m_Sorted)):
    print(m_Sorted[i])

print()
for i in range(len(m_Input)):
    print(m_Input[i])
