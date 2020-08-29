'''
The company ABC decided to give a salary increase to its employees,
according to the following table:

                Salary                  Readjustment Rate
            0 - 400.00                          15%
            400.01 - 800.00                     12%
            800.01 - 1200.00                    10%
            1200.01 - 2000.00                   7%
            Above 2000.00                       4%

Read the employee's salary, calculate and print the new employee's salary, as
well the money earned and the increase percentual obtained by the employee,
with corresponding messages in Portuguese, as the below example.
'''

m_Salary = float(input())
m_Readjustment = None

if m_Salary > 0.0:
    if m_Salary < 400.01:
        m_Readjustment = m_Salary * 0.15
    elif m_Salary < 800.01:
        m_Readjustment = m_Salary * 0.12
    elif m_Salary < 1200.01:
        m_Readjustment = m_Salary * 0.1
    elif m_Salary < 2000.01:
        m_Readjustment = m_Salary * 0.07
    else:
        m_Readjustment = m_Salary * 0.04

print('Novo salario: {:.2f}'.format(m_Salary+m_Readjustment))
print('Reajuste ganho: {:.2f}'.format(m_Readjustment))
print('Em percentual: {} %'.format(int(m_Readjustment/(m_Salary)*100)))
