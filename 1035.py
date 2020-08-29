'''
Read 4 integer values A, B, C and D. Then if B is greater than C and D is
greater than A and if the sum of C and D is greater than the sum of A and B
and if C and D were positives values and if A is even, write the message
“Valores aceitos” (Accepted values). Otherwise, write the message “Valores
nao aceitos” (Values not accepted).
'''

v_A, v_B, v_C, v_D = input().split()
v_A, v_B, v_C, v_D = int(v_A), int(v_B), int(v_C), int(v_D)

v_IsAccepted = v_B > v_C and v_D > v_A and v_C+v_D > v_A + v_B \
    and v_C >= 0 and v_D >= 0 and v_A % 2 == 0

print('Valores', ('nao aceitos', 'aceitos')[v_IsAccepted])
