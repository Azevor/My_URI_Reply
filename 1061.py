vDay1Input = input().split()
vTime1Input = input().split(":")
vDay2Input = input().split()
vTime2Input = input().split(":")

vDay1, vDay2 = int(vDay1Input[1]), int(vDay2Input[1])
vHour1 = int(vTime1Input[0])
vMinute1 = int(vTime1Input[1])
vSecond1 = int(vTime1Input[2])
vHour2 = int(vTime2Input[0])
vMinute2 = int(vTime2Input[1])
vSecond2 = int(vTime2Input[2])

if vDay1 > 0 and vDay2 > 0 and vDay2 >= vDay1:
    if vSecond2 >= vSecond1:
        vGapSecond = vSecond2-vSecond1
    else:
        vGapSecond = 60-vSecond1+vSecond2
        vMinute2 -= 1
    
    if vMinute2 >= vMinute1:
        vGapMinute = vMinute2-vMinute1
    else:
        vGapMinute = 60-vMinute1+vMinute2
        vHour2 -= 1
    
    if vHour2 >= vHour1:
        vGapHour = vHour2-vHour1
    else:
        vGapHour = 24-vHour1+vHour2
        vDay2 -= 1
    
    vGapDay = vDay2-vDay1
    
    if vGapDay < 0:
        vGapDay = 0
        vGapHour = 0
        vGapMinute = 0
        vGapSecond = 0

else:
    vGapDay = 0
    vGapHour = 0
    vGapMinute = 0
    vGapSecond = 0

print(vGapDay, "dia(s)")
print(vGapHour, "hora(s)")
print(vGapMinute, "minuto(s)")
print(vGapSecond, "segundo(s)")
