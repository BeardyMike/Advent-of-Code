import re
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
RedLimit = 12
GreenLimit = 13
BlueLimit = 14
def function():
    total = 0
    with open("2023\Day 2\input.txt", "r") as f:
        for line in f:
            #print("--------------------")
            colour = ""
            cubes = ""
            r = ""
            m = ""
            redcubes = [0]
            bluecubes = [0]
            greencubes = [0]
            line = line.replace('\n', '')
            line = line.replace(';', ',')
            line = line.replace(' ', '')
            #break the line into a list of parts, separated by colons.
            parts = line.split(":")
            #print(parts)
            #the first part is the GameID.
            GameID = parts[0]
            #remove any letters in alphabet from the GameID.
            for letter in alphabet:
                GameID = GameID.replace(letter, "")
            #print("GameID is " +GameID)
            #the second part is the PulledCubes
            PulledCubes = parts[1]
            #split the PulledCubes into a list of cubes, separated by commas.
            PulledCubes = PulledCubes.split(",")
            #print(PulledCubes)
            #split each PulledCube after the number.
            for PulledCube in PulledCubes:
                r = re.compile("([0-9]+)([a-zA-Z]+)")
                m = r.match(PulledCube)
                #print(m.group(1) + " " + m.group(2))
                colour = m.group(2)
                cubes = m.group(1)
                if colour == "red":
                    #add the cubes to redcubes
                    redcubes.append(cubes)
                    #print(redcubes)
                elif colour == "blue":
                    #add the cubes to bluecubes
                    bluecubes.append(cubes)
                    #print(bluecubes)
                elif colour == "green":
                    #add the cubes to greencubes
                    greencubes.append(cubes)
                    #print(greencubes)
            #check if any number in redcubes is more than 12
            for redcube in redcubes:
                if int(redcube) > RedLimit:
                    #print("there are more than 12 red cubes.")
                    #print("there are " + redcube + " red cubes.")
                    redvalid = False
                    break
                else:
                    redvalid = True
            #check if any number in bluecubes is more than 12
            for bluecube in bluecubes:
                if int(bluecube) > BlueLimit:

                    #print("there are more than 13 blue cubes.")
                    #print("there are " + bluecube + " blue cubes.")
                    bluevalid = False
                    break
                else:
                    bluevalid = True
            #check if any number in greencubes is more than 12
            for greencube in greencubes:
                if int(greencube) > GreenLimit:
                    #print("there are more than 14 green cubes.")
                    #print("there are " + greencube + " green cubes.")
                    greenvalid = False
                    break
                else:
                    greenvalid = True
            if redvalid == True and bluevalid == True and greenvalid == True:
                #print("GameID " + GameID + " is valid.")
                #add the gameID to the total
                #print("Adding " + GameID + " to " + str(total) + ".")
                total += int(GameID)
                #print("The total is now " + str(total))
            else:
                pass
                #print("GameID " + GameID + " is invalid.")
            #print("--------------------")
        #print("The total is " + str(total))
    return total