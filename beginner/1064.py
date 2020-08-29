mAmountNum = 6
mAmountPositive = 0
mAverage = 0

for i in range(mAmountNum):
    vTemp = float(input())
    if vTemp >= 0:
        mAverage += vTemp
        mAmountPositive += 1

if mAmountPositive > 0:
    mAverage /= mAmountPositive
else:
    mAverage = 0

print("{:.0f} valores positivos".format(mAmountPositive))
print("{:.1f}".format(mAverage))
