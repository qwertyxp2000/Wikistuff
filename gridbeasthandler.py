def grid(minimum, maximum):
    for i in range(minimum, maximum + 1):
        print("|-")
        print("| %s || ??? || ??? || ??? || N/A" % (i))

grid(17, 63)
