def ElfHax():
    PlayerScore = 0
    try:
        with open("2022\Day 2\input.txt",'r') as f:
            data = f.read().splitlines()
            data = [x.replace('A','Rock').replace('B','Paper').replace('C','Scissors').replace('X','Rock').replace('Y','Paper').replace('Z','Scissors') for x in data]
            data = [x.split(' ') for x in data]
            for x in data:
                if x[0] == 'Rock' and x[1] == 'Scissors' or x[0] == 'Paper' and x[1] == 'Rock' or x[0] == 'Scissors' and x[1] == 'Paper':
                    PlayerScore += 0
                elif x[0] == 'Rock' and x[1] == 'Paper' or x[0] == 'Paper' and x[1] == 'Scissors' or x[0] == 'Scissors' and x[1] == 'Rock':
                    PlayerScore += 6
                else:
                    PlayerScore += 3
                if x[1] == 'Rock':
                    PlayerScore += 1
                elif x[1] == 'Paper':
                    PlayerScore += 2
                else:
                    PlayerScore += 3
        return 'For part 1 the score is {}'.format(PlayerScore)
    except:
        return "ERROR - Download YOUR input file and pop in the Day 2 folder"