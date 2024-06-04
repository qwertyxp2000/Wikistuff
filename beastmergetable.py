import math

#Begin with the Beast Handler "base" costs of the base tower and its upgrades
beasthandler_cost = 250
beastupgrade_cost_medium = [
    [160, 810, 2010, 12500],
    [175, 830, 2065, 9500],
    [190, 860, 2120, 7800]
    ]
crosspath = [0, 0, 0]

def RoundToFive(num): #the annoying BTD6 rounding stuff
    num = math.floor(num)
    num = (num + 2.5)
    rem = num % 10
    if rem > 5:
        rem = rem - 5
    return round(num-rem)

def easyify(cost): #purpose is to make the Easy cost and do the annoying rounding junk afterwards
    cost = RoundToFive(cost * 0.85)
    return cost
def hardify(cost): #purpose is to make the Easy cost and do the annoying rounding junk afterwards
    cost = RoundToFive(cost * 1.08)
    return cost
def impoppableify(cost): #purpose is to make the Easy cost and do the annoying rounding junk afterwards
    cost = RoundToFive(cost * 1.2)
    return cost

#Easy Costs Table (n.b. there's gotta be an easier way to write this junk)
beastupgrade_cost_easy = [
    [easyify(beastupgrade_cost_medium[0][0]), easyify(beastupgrade_cost_medium[0][1]), easyify(beastupgrade_cost_medium[0][2]), easyify(beastupgrade_cost_medium[0][3])],
    [easyify(beastupgrade_cost_medium[1][0]), easyify(beastupgrade_cost_medium[1][1]), easyify(beastupgrade_cost_medium[1][2]), easyify(beastupgrade_cost_medium[1][3])],
    [easyify(beastupgrade_cost_medium[2][0]), easyify(beastupgrade_cost_medium[2][1]), easyify(beastupgrade_cost_medium[2][2]), easyify(beastupgrade_cost_medium[2][3])],
    ]
#Hard Costs Table (n.b. there's gotta be an easier way to write this junk)
beastupgrade_cost_hard = [
    [hardify(beastupgrade_cost_medium[0][0]), hardify(beastupgrade_cost_medium[0][1]), hardify(beastupgrade_cost_medium[0][2]), hardify(beastupgrade_cost_medium[0][3])],
    [hardify(beastupgrade_cost_medium[1][0]), hardify(beastupgrade_cost_medium[1][1]), hardify(beastupgrade_cost_medium[1][2]), hardify(beastupgrade_cost_medium[1][3])],
    [hardify(beastupgrade_cost_medium[2][0]), hardify(beastupgrade_cost_medium[2][1]), hardify(beastupgrade_cost_medium[2][2]), hardify(beastupgrade_cost_medium[2][3])],
    ]
#Hard Costs Table (n.b. there's gotta be an easier way to write this junk)
beastupgrade_cost_impoppable = [
    [impoppableify(beastupgrade_cost_medium[0][0]), impoppableify(beastupgrade_cost_medium[0][1]), impoppableify(beastupgrade_cost_medium[0][2]), impoppableify(beastupgrade_cost_medium[0][3])],
    [impoppableify(beastupgrade_cost_medium[1][0]), impoppableify(beastupgrade_cost_medium[1][1]), impoppableify(beastupgrade_cost_medium[1][2]), impoppableify(beastupgrade_cost_medium[1][3])],
    [impoppableify(beastupgrade_cost_medium[2][0]), impoppableify(beastupgrade_cost_medium[2][1]), impoppableify(beastupgrade_cost_medium[2][2]), impoppableify(beastupgrade_cost_medium[2][3])],
    ]

#Testing that the tables are working as expected
print(beastupgrade_cost_medium)
print("-----------------------------------------------------------------")
print(beastupgrade_cost_easy)
print(beastupgrade_cost_medium)
print(beastupgrade_cost_hard)
print(beastupgrade_cost_impoppable)
print("-----------------------------------------------------------------")

#Now to write the actual tables
print("|-")
for beastpath in range(0, (len(beastupgrade_cost_medium))):
    print(beastpath)
    for beastpath2 in range(1, (len(beastupgrade_cost_medium[beastpath]) + 1)):
        print(beastpath2)
        print(crosspath)
