import re
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def function():
    total = 0
    with open("2023\Day 2\input.txt", "r") as f:
        for line in f:
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
            #the first part is the GameID.
            GameID = parts[0]
            #remove any letters in alphabet from the GameID.
            for letter in alphabet:
                GameID = GameID.replace(letter, "")
            #the second part is the PulledCubes
            PulledCubes = parts[1]
            #split the PulledCubes into a list of cubes, separated by commas.
            PulledCubes = PulledCubes.split(",")
            #split each PulledCube after the number.
            for PulledCube in PulledCubes:
                r = re.compile("([0-9]+)([a-zA-Z]+)")
                m = r.match(PulledCube)
                colour = m.group(2)
                cubes = m.group(1)
                if colour == "red":
                    #add the cubes to redcubes
                    redcubes.append(int(cubes))
                elif colour == "blue":
                    #add the cubes to bluecubes
                    bluecubes.append(int(cubes))
                elif colour == "green":
                    #add the cubes to greencubes
                    greencubes.append(int(cubes))
            # sort the lists with the largest number first.
            redcubes.sort(reverse=True)
            bluecubes.sort(reverse=True)
            greencubes.sort(reverse=True)
            math = redcubes[0] * greencubes[0] * bluecubes[0]
            total = total + math
        return total