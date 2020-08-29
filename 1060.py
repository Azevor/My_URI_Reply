'''
Write a program that reads 6 numbers. These numbers will only be positive or
negative (disregard null values). Print the total number of positive numbers.
'''

m_Cont = 0
m_Positive = 0

while True:
    m_Input = input()

    if m_Input == '':
        continue

    if float(m_Input) >= 0:
        m_Positive += 1

    if m_Cont == 5:
        break
    m_Cont += 1

print('{0} valores positivos'.format(m_Positive))
