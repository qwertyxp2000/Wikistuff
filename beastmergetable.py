import math

#Begin with the Beast Handler "base" costs of the base tower and its upgrades
beasthandler_cost = 250
beastupgrade_cost_medium = [
    [160, 810, 2010, 12500],
    [175, 830, 2065, 9500],
    [190, 860, 2120, 7800]
    ]
crosspath = [0, 0, 0]
beastpowermax = [1, 3, 8, 16]

#Difficulty multipliers
difficulty_multiplier = [0.85, 1, 1.08, 1.2]

def RoundToFive(num): #the annoying BTD6 rounding stuff
    num = math.floor(num)
    num = (num + 2.5)
    rem = num % 10
    if rem > 5:
        rem = rem - 5
    return round(num-rem)

#Upgrade Costs Table
beastupgrade_cost_table = []
for i in range(0, len(difficulty_multiplier)): #Start with appending an empty four-unit list, the four units for Easy, Medium, Hard, Impoppable
    beastupgrade_cost_table.append([])
    for j in range(0, len(beastupgrade_cost_medium)): #Append the empty three-unit list, the three units for the Path 1-3 upgrades
        beastupgrade_cost_table[i].append([])
#print(beastupgrade_cost_table)
# i = Difficulty (Easy, Medium, Hard, Impoppable)
# j = The Beast Handler upgrade path (0, 1, 2; top, middle, bottom)
# k = The Beast Handler upgrade tier of a upgrade path (0-3, or in this case Tiers 1-4)
for i in range(0, len(difficulty_multiplier)): #Easy, Medium, Hard, Impoppable
    for j in range(0, len(beastupgrade_cost_medium)):
        for k in range(0, len(beastupgrade_cost_medium[j])):
            beastupgrade_cost_table[i][j].append(RoundToFive(beastupgrade_cost_medium[j][k] * difficulty_multiplier[i]))
#print(beastupgrade_cost_table)

# Cumulative Costs Table
beastcumulative_cost_table = []
for i in range(0, len(difficulty_multiplier)): #Start with appending an empty four-unit list, the four units for Easy, Medium, Hard, Impoppable
    beastcumulative_cost_table.append([])
    for j in range(0, len(beastupgrade_cost_medium)): #Append the empty three-unit list, the three units for the Path 1-3 upgrades
        beastcumulative_cost_table[i].append([])
#print(beastcumulative_cost_table)
# i = Difficulty (Easy, Medium, Hard, Impoppable)
# j = The Beast Handler upgrade path (0, 1, 2; top, middle, bottom)
# k = The Beast Handler upgrade tier of a upgrade path (0-3, or in this case Tiers 1-4)
# l = Summation process from 0 to k for that Beast Handler summation process
for i in range(0, len(difficulty_multiplier)): #Easy, Medium, Hard, Impoppable
    for j in range(0, len(beastupgrade_cost_medium)):
        for k in range(0, len(beastupgrade_cost_medium[j])):
            beast_summation = beasthandler_cost
            for l in range(0, k + 1): #Increased cap of max by 1 so that the process is shifted 1 up; basically from 1 to (k + 1) instead of 0 to k. If 0 to k, then we get the default "0" which would be just the Beast Handler base cost without any of that extra calculations inside that condition block
                beast_summation += beastupgrade_cost_table[i][j][l] #go from 0-k again so the summation actually can occur
            #print(beast_summation)
            beastcumulative_cost_table[i][j].append(beast_summation)
#print(beastcumulative_cost_table)

##Testing that the tables are working as expected
#print(beastupgrade_cost_medium)
#print("-----------------------------------------------------------------")
#print(beastupgrade_cost_easy)
#print(beastupgrade_cost_medium)
#print(beastupgrade_cost_hard)
#print(beastupgrade_cost_impoppable)
#print("-----------------------------------------------------------------")

#Now to write the actual tables
# j = The Beast Handler upgrade path (0, 1, 2; top, middle, bottom)
# k = The Beast Handler upgrade tier of a upgrade path (0-3, or in this case Tiers 1-4)
# l = Difficulty but it is a pushing process
for j in range(0, len(beastcumulative_cost_table[i])):
    for k in range(0, len(beastcumulative_cost_table[i][j])):
        print("|-")
        #these (j==0)*mathematics stuff are bool conditions, sorta like a compressed IF statement, also a non-newline ending with just a space
        print("| %s-%s-%s" % ((j == 0) * (k + 1), (j == 1) * (k + 1), (j == 2) * (k + 1)), end = " ")
        #Hint: int() on a boolean results in 0 or 1 depending on false or true
        for l in range(0, len(difficulty_multiplier)): #Easy, Medium, Hard, Impoppable
            #print(beastcumulative_cost_table[l][j][k])
            print("||", end = " ")
            print("$%s, %s power" % (beastcumulative_cost_table[l][j][k], beastpowermax[k]), end = " ")
            print("<br />", end = " ")
            print("$%s / %s power" % (round(beastcumulative_cost_table[l][j][k] / beastpowermax[k], 4), beastpowermax[k]), end = " ")
        print("")
