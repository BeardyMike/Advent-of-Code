def parttwo():
    count = 0
    with open("2022\Day 4\input.txt",'r') as f:
        for line in f:
            rangeone, rangetwo = map(lambda x: tuple(map(int, x)), map(lambda x: x.split('-'), line.strip().split(',')),)
            if not (rangeone[0] > rangetwo[1] or rangeone[1] < rangetwo[0]):
                count += 1             
    return count