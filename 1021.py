'''
Read a value of floating point with two decimal places. This represents a
monetary value. After this, calculate the smallest possible number of notes
and coins on which the value can be decomposed. The considered notes are of
100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05
and 0.01. Print the message “NOTAS:” followed by the list of notes and the
message “MOEDAS:” followed by the list of coins.
'''


class Bank:

    def __init__(self):
        self.m_Bills = [100, 50, 20, 10, 5, 2]
        self.m_Coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

    def withDraw(self, p_Value):
        v_Change = self.amountBills(p_Value)
        self.amountCoins(v_Change)

    def amountBills(self, p_Value):

        print('NOTAS:')
        for i_Value in self.m_Bills:
            v_AmountBills = int(p_Value/i_Value)
            p_Value -= v_AmountBills*i_Value
            print('{} nota(s) de R$ {:.2f}'.format(v_AmountBills, i_Value))

        return p_Value

    def amountCoins(self, p_Value):

        print('MOEDAS:')
        for i_Value in self.m_Coins:
            v_AmountCoins = int(p_Value/i_Value+0.000001)
            p_Value -= v_AmountCoins*i_Value
            print('{} moeda(s) de R$ {:.2f}'.format(v_AmountCoins, i_Value))


if __name__ == '__main__':
    v_Draw = Bank()
    v_Value = float(input())

    v_Draw.withDraw(v_Value)
