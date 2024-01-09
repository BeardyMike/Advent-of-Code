def function():
    with open('2023\Day 1\input.txt', 'r') as values:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        numbersfixed = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
        strings = []
        for line in values:
            for number in numbersfixed:
                line = line.replace(number, numbersfixed[number])
            for letter in alphabet:
                line = line.replace(letter, '')
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            number = list(line)
            string = number[0] + number[-1]
            string = int(string)
            strings.append(string)
        string = ""
        total = 0
        for string in strings:
            total += string
        return total

print(function())