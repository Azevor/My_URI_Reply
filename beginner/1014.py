'''
Calculate a car's average consumption being provided the total distance
traveled (in Km) and the spent fuel total (in liters).
'''

m_Distance = int(input())
m_FuelSpent = float(input())

print('{:.3f} km/l'.format(m_Distance/m_FuelSpent))
