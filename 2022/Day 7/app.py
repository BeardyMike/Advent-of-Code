from Part1 import partone

with open('2022\Day 7\input.txt') as f:
    s = f.read()
print("Of the dir's that are, at most, 100,000CB, their total size is", partone(s,False), "CandyBytes")
print("The smallest deletable directory is", partone(s,True), "CandyBytes")