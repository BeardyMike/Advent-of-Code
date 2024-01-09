import re
def function():
    with open("2023\Day 3\input.txt", "r") as f:
        grid = []
        for line in f:
            line = line.replace('\n', '') # remove the newline character
            line = re.sub(r"[^a-zA-Z0-9.]", "P", line) # replace all non-alphanumeric characters with P
            # print(line + " is " + str(len(line)) + " characters long.")
            # create a 2D list of the lines, with each character as a separate item. each line is ten characters long.
            grid.append(list(line))





            

