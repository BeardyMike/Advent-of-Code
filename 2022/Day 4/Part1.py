def partone():
    count = 0
    with open("2022\Day 4\input.txt",'r') as f:
        for line in f:
            rangeone, rangetwo = map(lambda x: tuple(map(int, x)), map(lambda x: x.split('-'), line.strip().split(',')),)
            if rangeone[0] >= rangetwo[0] and rangeone[1] <= rangetwo[1] or rangetwo[0] >= rangeone[0] and rangetwo[1] <= rangeone[1]:
                count += 1                
    return count