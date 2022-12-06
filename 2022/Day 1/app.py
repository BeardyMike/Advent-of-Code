#part 1
with open("2022\Day 1\input.txt", 'r') as file:
    valyoos = file.read()
    valyoos = valyoos.split('\n\n')
    valyoos = [q.split('\n') for q in valyoos]
    caloreez = [sum([int(b) for b in q]) for q in valyoos]
    print("the Single BIGGEST cache of caloreez is",max(caloreez))
#Part 2
    caloreez = sorted(caloreez, reverse=True)
    print("the top three caches of caloreez added together is",caloreez[0] + caloreez[1] + caloreez[2])