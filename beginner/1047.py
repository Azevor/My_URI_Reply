'''
Read the start time and end time of a game, in hours and minutes (initial hour,
initial minute, final hour, final minute). Then print the duration of the game,
knowing that the game can begin in a day and finish in another day.

Obs.: With a maximum game time of 24 hours
and the minimum game time of 1 minute.
'''

m_HourBegin, m_MinuteBegin, m_HourEnd, m_MinuteEnd = input().split()

m_HourBegin, m_MinuteBegin, m_HourEnd, m_MinuteEnd = int(
    m_HourBegin), int(m_MinuteBegin), int(m_HourEnd), int(m_MinuteEnd)

m_DurationHour = m_HourEnd-m_HourBegin
m_DurationMinute = m_MinuteEnd-m_MinuteBegin

if m_DurationMinute < 0:
    m_DurationMinute += 60
    if m_DurationHour <= 0:
        m_DurationHour += 23
    elif m_DurationHour > 0:
        m_DurationHour -= 1
elif m_DurationMinute == 0:
    if m_DurationHour >= 0:
        m_DurationHour += 24
else:
    if m_DurationHour < 0:
        m_DurationHour += 23

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(
    m_DurationHour, m_DurationMinute))
