def function():
    with open('2023\Day 1\input.txt', 'r') as values:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        strings = []
        for line in values:
            for letter in alphabet:
                line = line.replace(letter, '')
            line = line.replace('\n', '')
            numbers = list(line)
            string = numbers[0] + numbers[-1]
            strings.append(string)
        total = 0
        for string in strings:
            total += int(string)
        return total

