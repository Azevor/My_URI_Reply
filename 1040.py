'''
Read four numbers (N1, N2, N3, N4), which one with 1 digit after the decimal
point, corresponding to 4 scores obtained by a student. Calculate the average
with weights 2, 3, 4 e 1 respectively, for these 4 scores and print the
message "Media: " (Average), followed by the calculated result. If the average
was 7.0 or more, print the message "Aluno aprovado." (Approved Student).
If the average was less than 5.0, print the message: "Aluno reprovado."
(Reproved Student). If the average was between 5.0 and 6.9, including these,
the program must print the message "Aluno em exame." (In exam student).

In case of exam, read one more score. Print the message "Nota do exame:"
(Exam score) followed by the typed score. Recalculate the average (sum the
exam score with the previous calculated average and divide by 2) and print the
message “Aluno aprovado.” (Approved student) in case of average 5.0 or more)
or "Aluno reprovado." (Reproved student) in case of average 4.9 or less.
For these 2 cases (approved or reproved after the exam) print the message
"Media final: " (Final average) followed by the final average for this
student in the last line.
'''

m_N1, m_N2, m_N3, m_N4 = input().split()
m_N1, m_N2, m_N3, m_N4 = float(m_N1), float(m_N2), float(m_N3), float(m_N4)
m_Pounds = 2+3+4+1

m_Average = (m_N1*2+m_N2*3+m_N3*4+m_N4)/m_Pounds
print('Media: {:.1f}'.format(m_Average))

if m_Average >= 7.0:
    print('Aluno aprovado.')
elif m_Average < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    v_Exam = float(input())
    print('Nota do exame: {:.1f}'.format(v_Exam))
    v_FinalAverage = (v_Exam+m_Average)/2
    if v_FinalAverage >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(v_FinalAverage))
