'''
In this problem, the task is to read a code of a product 1, the number of
units of product 1, the price for one unit of product 1, the code of a product
2, the number of units of product 2 and the price for one unit of product 2.
After this, calculate and show the amount to be paid.
'''

m_Product01, m_AmountProduct01, m_PriceProduct01 = input().split()
m_Product02, m_AmountProduct02, m_PriceProduct02 = input().split()

m_Product01, m_AmountProduct01, m_PriceProduct01 = int(
    m_Product01), int(m_AmountProduct01), float(m_PriceProduct01)
m_Product02, m_AmountProduct02, m_PriceProduct02 = int(
    m_Product02), int(m_AmountProduct02), float(m_PriceProduct02)

print('VALOR A PAGAR: R$ {:.2f}'.format(
    m_AmountProduct01*m_PriceProduct01+m_AmountProduct02*m_PriceProduct02))
