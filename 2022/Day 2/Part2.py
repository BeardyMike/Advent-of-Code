def ServerHax():
    PlayerScore = 0
    try:
        with open("2022\Day 2\input.txt",'r') as f:
            data = [x.replace('A','Rock').replace('B','Paper').replace('C','Scissors').replace('X','Lose').replace('Y','Draw').replace('Z','Win').split(' ') for x in f.read().splitlines()]
            for line in data:
                if line[0] =="Rock" and line[1] == "Lose":
                    PlayerScore += 3
                elif line[0] =="Rock" and line[1] == "Draw":
                    PlayerScore += 4
                elif line[0] =="Rock" and line[1] == "Win":
                    PlayerScore += 8
                elif line[0] =="Paper" and line[1] == "Lose":
                    PlayerScore += 1
                elif line[0] =="Paper" and line[1] == "Draw":
                    PlayerScore += 5
                elif line[0] =="Paper" and line[1] == "Win":
                    PlayerScore += 9
                elif line[0] =="Scissors" and line[1] == "Lose":
                    PlayerScore += 2
                elif line[0] =="Scissors" and line[1] == "Draw":
                    PlayerScore += 6
                elif line[0] =="Scissors" and line[1] == "Win":
                    PlayerScore += 7
        return 'For part 2 the score is {}'.format(PlayerScore)
    except:
        return "ERROR - Download YOUR input file and pop in the Day 2 folder"