

def level1(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        game = line.split(':')
        valid = True
        for set in game[1].split(';'):
            numOfReds = 0
            numOfBlues = 0
            numOfGreens = 0
            for cubes in set.split(','):
                if cubes.__contains__('green'):
                    numOfGreens += int(cubes.split('green')[0].strip())
                elif cubes.__contains__('blue'):
                    numOfBlues += int(cubes.split('blue')[0].strip())
                elif cubes.__contains__('red'):
                    numOfReds += int(cubes.split('red')[0].strip())
            if not ((numOfBlues <= 14) and (numOfGreens <= 13) and (numOfReds <= 12)):
                valid = False
                break
        if valid:
            total += int(game[0].split('Game')[1].strip())    


    print(total)
level1('input1.txt')

def level2(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        game = line.split(':')
        maxRed = 0
        maxBlue = 0
        maxGreen = 0
        for set in game[1].split(';'):
            numOfReds = 0
            numOfBlues = 0
            numOfGreens = 0
            for cubes in set.split(','):
                if cubes.__contains__('green'):
                    numOfGreens += int(cubes.split('green')[0].strip())
                elif cubes.__contains__('blue'):
                    numOfBlues += int(cubes.split('blue')[0].strip())
                elif cubes.__contains__('red'):
                    numOfReds += int(cubes.split('red')[0].strip())
            if maxRed < numOfReds:
                maxRed = numOfReds
            if maxBlue < numOfBlues:
                maxBlue = numOfBlues
            if maxGreen < numOfGreens:
                maxGreen = numOfGreens
        total += maxRed*maxBlue*maxGreen
    print(total)

level2('input2.txt')
