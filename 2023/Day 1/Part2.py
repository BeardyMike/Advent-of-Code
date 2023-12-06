def function():
    with open('2023\Day 1\input.txt', 'r') as values:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        numbersfixed = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
        strings = []
        for line in values:
            # search the line for any text that matches the keys in the numbers dictionary.
            # if there is a match, replace the text with the corresponding value in numbersfixed.
            for number in numbers:
                line = line.replace(number, numbersfixed[number])
            # remove any letters from the line.
            for letter in alphabet:
                line = line.replace(letter, '')
            # remove any spaces from the line.
            line = line.replace(' ', '')
            # remove any newlines from the line.
            line = line.replace('\n', '')
            # add the line to the strings list.
            number = list(line)
            string = number[0] + number[-1]
            string = int(string)
            strings.append(string)
            #print(string)
        string = ""
        total = 0
        for string in strings:
            total += string
        return total

