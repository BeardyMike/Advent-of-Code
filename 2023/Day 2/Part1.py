import re
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def checker(cubes,colour):
    redlimit = 12
    greenlimit = 13
    bluelimit = 14
    #check if the number of cubes exceeds the limit for the colour.
    if colour == "red":
        if int(cubes) > redlimit:
            return False
    elif colour == "green":
        if int(cubes) > greenlimit:
            return False
    elif colour == "blue":
        if int(cubes) > bluelimit:
            return False
    return True

def function():
    with open("2023\Day 2\input.txt", "r") as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.replace(';', ',')
            line = line.replace(' ', '')
            print(line)
            #break the line into a list of parts, separated by colons.
            parts = line.split(":")
            print(parts)
            #the first part is the GameID.
            GameID = parts[0]
            #remove any letters in alphabet from the GameID.
            for letter in alphabet:
                GameID = GameID.replace(letter, "")
            #the second part is the PulledCubes
            PulledCubes = parts[1]
            #split the PulledCubes into a list of cubes, separated by commas.
            PulledCubes = PulledCubes.split(",")
            print(PulledCubes)
            #split each PulledCube after the number.
            for PulledCube in PulledCubes:
                r = re.compile("([0-9]+)([a-zA-Z]+)")
                m = r.match(PulledCube)
                print(m.group(1))
                print(m.group(2))
                colour = m.group(2)
                cubes = m.group(1)
                #check if the number of cubes exceeds the limit for the colour.                          
                validGameIDs = []
                if checker(cubes,colour) == True:
                    #if it passes the checker function, add GameID to a list of valid GameIDs.
                    validGameIDs.append(GameID)
                # add all the gameIDs in the list of valid GameIDs together into one nubmer.
                total = 0
                for GameID in validGameIDs:
                    total += int(GameID)
                #return the total.
                return total

