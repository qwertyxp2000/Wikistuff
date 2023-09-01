import math

def grid(minimum, maximum):
    # Beast Power
    b_M = 64
    b_m = 16
    b_c = b_m
    # Pierce
    p_M = 90
    p_m = 30
    p_c = p_m
    # Damage
    d_M = 6
    d_m = 2
    d_c = d_m

    #Ceramics, MOABs, BFBs
    ceramic = 0
    moab = 0
    bfb = 0

    for i in range(minimum, maximum + 1):
        b_c = i
        p_c = math.floor(p_m + (p_M - p_m)/(b_M - b_m) * (b_c - b_m))
        d_c = math.floor(d_m + (d_M - d_m)/(b_M - b_m) * (b_c - b_m))
        ceramic = math.ceil(p_c/2)
        moab = math.ceil(p_c/10)
        bfb = math.ceil(p_c/30)
        
        print("|-")
        print("| %s || %s || %s || ??? || Picks up to %s Ceramics, %s MOABs, %s BFBs, and 2 (targetable) DDT" % (i, p_c, d_c, ceramic, moab, bfb))

grid(33, 63)
