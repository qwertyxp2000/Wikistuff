speedBonus = 1/0.92
pierceBonus = 0.08
maxStacks = 20

for i in range(maxStacks+1):
    speedBoost = pow(speedBonus, float(i))
    pierceBoost = pierceBonus * float(i)
    
    print("|-")
    print("| %s" % (i))
    print("| +%s%% " % (round(speedBoost * 100 - 100, 2)))
    print("| +%s%% " % (round(pierceBoost * 100, 2)))
