'''
Using the following table, write a program that reads a code and the amount of
an item. After, print the value to pay. This is a very simple program with the
only intention of practice of selection commands.
            CODE        SPECIFICATION      PRICE
            1          Cachorro Quente     R$ 4.00
            2          X-Salada            R$ 4.50
            3          X-Bacon             R$ 5.00
            4          Torrada simples     R$ 2.00
            5          Refrigerante        R$ 1.50
'''

m_Items = {
            1: ['Cachorro Quente', 4.00],
            2: ['X-Salada', 4.50],
            3: ['X-Bacon', 5.00],
            4: ['Torrada simples', 2.00],
            5: ['Refrigerante', 1.50],
           }

m_Cod, m_Count = input().split()
m_Cod, m_Count = int(m_Cod), int(m_Count)

print('Total: R$ {:.2f}'.format(m_Items[m_Cod][1]*m_Count))
