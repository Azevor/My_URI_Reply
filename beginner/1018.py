'''
In this problem you have to read an integer value and calculate the smallest
possible number of banknotes in which the value may be decomposed.
The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and
the list of banknotes.
'''


class Bank:

    def __init__(self, p_Notes):
        self.m_Notes = p_Notes

    def amountPerValue(self, p_Value):
        v_Count = 0

        for i_Value in self.m_Notes:
            while int(p_Value/i_Value) > 0:
                v_Count += 1
                p_Value -= i_Value
            print('{} nota(s) de R$ {},00'.format(v_Count, i_Value))
            v_Count = 0


if __name__ == '__main__':
    v_Notes = [100, 50, 20, 10, 5, 2, 1]
    v_Draw = Bank(v_Notes)
    v_Value = int(input())

    print(v_Value)
    v_Draw.amountPerValue(v_Value)
