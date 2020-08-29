'''
Read the start time and end time of a game, in hours. Then calculate the
duration of the game, knowing that the game can begin in a day and finish in
another day, with a maximum duration of 24 hours. The message must be printed
in portuguese “O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”
'''

m_Begin, m_End = input().split()
m_Begin, m_End = int(m_Begin), int(m_End)
m_Duration = m_End-m_Begin

if m_Duration <= 0:
    m_Duration += 24

print('O JOGO DUROU {} HORA(S)'.format(m_Duration))
