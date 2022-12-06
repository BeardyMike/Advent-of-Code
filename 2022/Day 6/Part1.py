def partone(num):
    with open('2022\Day 6\input.txt') as f:
        data = f.read().splitlines()[0]
        for i in range(len(data[num - 1:])):
            if num == len(set(data[i:i + num])):
                return i+num