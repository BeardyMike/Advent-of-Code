def parttwo():
    answer = ""
    with open('2022\Day 5\input.txt') as f:
        stacks = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[]}
        for line in f.readlines()[0:8]:
            stacks["1"].insert(0,line[1])
            stacks["2"].insert(0,line[5])
            stacks["3"].insert(0,line[9])
            stacks["4"].insert(0,line[13])
            stacks["5"].insert(0,line[17])
            stacks["6"].insert(0,line[21])
            stacks["7"].insert(0,line[25])
            stacks["8"].insert(0,line[29])
            stacks["9"].insert(0,line[33])
            for i in stacks:
                while " " in stacks[i]:
                    stacks[i].remove(" ")  
    stacks["CrateVoid"] = []
    with open("2022\Day 5\input.txt",'r') as f:
        # read the input file
        for line in f.readlines()[10:]:      #skip over the first 10 lines of the file
            line = line.replace("move ", "").replace("from ", "").replace("to ", "").replace(" ", ",").replace("\n", "").split(',')
            for i in range(0, int(line[0])):
                stacks["CrateVoid"].append(stacks[line[1]].pop())
            for i in range(0, int(line[0])):   
                stacks[line[2]].append(stacks["CrateVoid"].pop())
        print("--Part2--")    
        # remove cratevoid from the dictionary
        stacks.pop("CrateVoid")  
        for i in stacks: answer = answer + stacks[i][-1]
        print(answer)
    return