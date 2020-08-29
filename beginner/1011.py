'''
Make a program that calculates and shows the volume of a sphere being provided
the value of its radius (R) . The formula to calculate the volume is:
(4/3) * pi * R³. Consider (assign) for pi the value 3.14159.
'''

m_PI = 3.14159
m_Radius = int(input())

print('VOLUME = {:.3f}'.format((4/3)*m_PI*m_Radius**3))
