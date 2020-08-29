'''
Write an algorithm that reads two floating values (x and y), which should
represent the coordinates of a point in a plane. Next, determine which
quadrant the point belongs, or if you are over one of the Cartesian axes or
the origin (x = y = 0).
                                    |Y
                                Q2  |   Q1
                             _______|_______X
                                    |
                                Q3  |   Q4
                                    |
If the point is at the origin, write the message "Origem".
If the point is over X axis write "Eixo X", else if the point is over Y axis
write "Eixo Y".
'''

m_X, m_Y = input().split()
m_X, m_Y = float(m_X), float(m_Y)

if m_X > 0.0:
    if m_Y > 0.0:
        print('Q1')
    else:
        print('Q4' if m_Y < 0.0 else 'Eixo X')
elif m_X < 0.0:
    if m_Y > 0.0:
        print('Q2')
    else:
        print('Q3' if m_Y < 0.0 else 'Eixo X')
else:
    print('Eixo Y' if m_Y != 0.0 else 'Origem')
