'''
In an imaginary country called Lisarb, all the people are very happy to pay
their taxes because they know that doesn’t exist corrupt politicians and the
taxes are used to benefit the population, without any misappropriation.
The currency of this country is Rombus, whose symbol is R$.
* view table in URI *
Read a value with 2 digits after the decimal point, equivalent to the salary
of a Lisarb inhabitant. Then print the due value that this person must pay of
taxes, according to the table below.

Remember, if the salary is R$ 3,002.00 for example, the rate of 8% is only over
R$ 1,000.00, because the salary from R$ 0.00 to R$ 2,000.00 is tax free.
In the follow example, the total rate is 8% over R$ 1000.00 + 18% over R$ 2.00,
resulting in R$ 80.36 at all. The answer must be printed with 2 digits after
the decimal point.
'''

m_Input = round(float(input()), 2)

if m_Input < 2000.01:
    print('Isento')
else:
    if m_Input < 3000.01:
        m_Taxes = (m_Input-2000)*0.08
    elif m_Input < 4500.01:
        m_Taxes = (m_Input-3000)*0.18+1000*0.08
    else:
        m_Taxes = (m_Input-4500)*0.28+1500*0.18+1000*0.08

    print('R$ {:.2f}'.format(m_Taxes))

    '''
else:
    m_Salary = {
        '0.00 to 2000.00': 0,
        '2000.01 to 3000.00': 8,
        '3000.01 to 4500.00': 18,
        'more than 4500.00': 28,
    }
    m_Range = None

    if m_Input < 2000.01:
        m_Range = '0.00 to 2000.00'
    elif m_Input < 3000.01:
        m_Range = '2000.01 to 3000.00'
    elif m_Input < 4500.01:
        m_Range = '3000.01 to 4500.00'
    else:
        m_Range = 'more than 4500.00'

    print('Faixa: {}'.format(m_Range))
'''
