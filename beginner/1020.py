'''
Read an integer value corresponding to a person's age (in days) and
print it in years, months and days, followed by its respective message
“ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation, consider the whole year with 365 days
and 30 days every month. In the cases of test there will never be a situation
that allows 12 months and some days, like 360, 363 or 364. This is just an
exercise for the purpose of testing simple mathematical reasoning.
'''


class Age:

    def __init__(self, p_Age):
        self.m_Age = p_Age

    def convertAge(self):
        v_Years = int(self.m_Age/365)
        v_Months = int((self.m_Age % 365)/30)
        v_Days = self.m_Age-(v_Years*365+v_Months*30)

        return [v_Years, v_Months, v_Days]


if __name__ == '__main__':
    v_Age = Age(int(input()))

    v_Format = v_Age.convertAge()
    print('{} ano(s)'.format(v_Format[0]))
    print('{} mes(es)'.format(v_Format[1]))
    print('{} dia(s)'.format(v_Format[2]))
