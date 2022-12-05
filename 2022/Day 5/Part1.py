def partone():
    # I couldnt figurte out how to parse the data from the first ten lines of the file
    # so I just hard coded the data into a dictionary, and removed the lines from the file
    crate = {}
    crate["1"] = ['N', 'R', 'G', 'P',]
    crate["2"] = ['J', 'T', 'B', 'L','F', 'G', 'D', 'C',]
    crate["3"] = ['M', 'S', 'V',]
    crate["4"] = ['L', 'S', 'R', 'C','Z', 'P',]
    crate["5"] = ['P', 'S', 'L', 'V','C', 'W', 'D', 'Q',]
    crate["6"] = ['C', 'T', 'N', 'W','D', 'M', 'S',]
    crate["7"] = ['H', 'D', 'G', 'W','P',]
    crate["8"] = ['Z', 'L', 'P', 'H','S', 'C', 'M', 'V',]
    crate["9"] = ['R', 'P', 'F', 'L','W', 'G', 'Z',]

    with open("2022\Day 5\input.txt",'r') as f:
        # read the input file
        for line in f.readlines()[10:512]:
            line = line.replace("move ", "")
            line = line.replace("from ", "")
            line = line.replace("to ", "")
            line = line.replace(" ", ",")
            line = line.replace("\n", "")
            # split the line into a dictionary of the values
            line = line.split(',')
            cranemove = line[0]
            cranefrom = line[1]
            craneto = line[2]
            #remove spaces from the new variables
            for i in range(0, int(cranemove)):
                crate[craneto].append(crate[cranefrom].pop())
        print("-------Part1-------")       
        print(crate["1"])
        print(crate["2"])
        print(crate["3"])
        print(crate["4"])
        print(crate["5"])
        print(crate["6"])
        print(crate["7"])
        print(crate["8"])
        print(crate["9"])
        print("----End of Part1----") 
        print()
        print()