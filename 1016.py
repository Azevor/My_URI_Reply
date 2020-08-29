'''
Two cars (X and Y) leave in the same direction. The car X leaves with a
constant speed of 60 km/h and the car Y leaves with a constant speed of
90 km / h.

In one hour (60 minutes) the car Y can get a distance of 30 kilometers from the
X car, in other words, it can get away one kilometer for each 2 minutes.

Read the distance (in km) and calculate how long it takes (in minutes) for the
car Y to take this distance in relation to the other car.
'''

'''
Análise:

    tempo1 = tempo2 = t

    distancia1 = velocidade1*t
    distancia2 = velocidade2*t

    diferençaDistancia = distancia2-distancia1
                       = velocidade2*t-velocidade1*t
                       = t*(velocidade2-velocidade1)
    Portanto:
    t = diferençaDistancia/(velocidade2-velocidade1)
'''

m_CarVelocityX = 60
m_CarVelocityY = 90
m_DifDistance = int(input())

m_Time = int(m_DifDistance/abs((m_CarVelocityY-m_CarVelocityX))*60)
print('{} minutos'.format(m_Time))
