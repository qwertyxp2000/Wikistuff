

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

    for i in range(minimum, maximum + 1):
        b_c = i
        p_c = p_m + (p_M - p_m)/(b_M - b_m) * (b_c - b_m)
        d_c = d_m + (d_M - d_m)/(b_M - b_m) * (b_c - b_m)
        print("|-")
        print("| %s || %s || %s || ??? || Picks up to ??? Ceramics, ??? MOABs, ??? BFBs, and 1 (targetable) DDT" % (i, p_c, d_c))

grid(16, 32)
