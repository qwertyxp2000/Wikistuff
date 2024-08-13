import math

nameOfUpgrade = "Comanche Commander"
costMedium = 35000
aerosub = True
aerodiscount_modifier = 0.9

#Difficulty multipliers
difficulty_multiplier = [0.85, 1, 1.08, 1.2]
#Rosalia multipliers
rosa_multiplier = [1, 0.95, 0.9]

def RoundToFive(num): #the annoying BTD6 rounding stuff
    num = math.floor(num)
    num = (num + 2.5)
    rem = num % 10
    if rem > 5:
        rem = rem - 5
    return round(num-rem)

costs = [[], []]
for i in range(0, 3):
    costs[0].append([])
    for j in range(0, len(difficulty_multiplier)):
        costs[0][i].append(RoundToFive(costMedium * rosa_multiplier[i] * difficulty_multiplier[j]))
if aerosub == True:
    for i in range(0, 3):
        costs[1].append([])
        for j in range(0, len(difficulty_multiplier)):
            costs[1][i].append(RoundToFive(costMedium * rosa_multiplier[i] * aerodiscount_modifier * difficulty_multiplier[j]))

print(costs)

print("*Version 44.0 buffed Rosalia's Level 6+ discount from 5%% to 10%%, which changed the prices of %s when buffed by her:" % (nameOfUpgrade))
print("**Easy: $%s → $%s" % (costs[0][1][0], costs[0][2][0]))
print("**Medium: $%s → $%s" % (costs[0][1][1], costs[0][2][1]))
print("**Hard: $%s → $%s" % (costs[0][1][2], costs[0][2][2]))
print("**Impoppable: $%s → $%s" % (costs[0][1][3], costs[0][2][3]))
print("**Easy + Aeronautic Subsidy: $%s → $%s" % (costs[1][1][0], costs[1][2][0]))
print("**Medium + Aeronautic Subsidy: $%s → $%s" % (costs[1][1][1], costs[1][2][1]))
print("**Hard + Aeronautic Subsidy: $%s → $%s" % (costs[1][1][2], costs[1][2][2]))
print("**Impoppable + Aeronautic Subsidy: $%s → $%s" % (costs[1][1][3], costs[1][2][3]))
