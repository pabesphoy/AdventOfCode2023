def isValidChar(char):
    return char != '.' and not char.isnumeric() and char != '\n'



def level1(file):
    with open(file) as file:
        lines = file.readlines()
    total = 0
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            char = lines[i][j]
            if isValidChar(char):
                print(char)
                numberBack = ''
                for jBack in range(j-1, -1, -1):
                    if lines[i][jBack].isnumeric():
                        numberBack = lines[i][jBack] + numberBack
                    else:
                        break
                if(numberBack != ''):
                    total += int(numberBack)
                    print(numberBack)
                numberForward = ''
                for jForward in range(j+1, len(lines[i])):
                    if lines[i][jForward].isnumeric():
                        numberForward = numberForward + lines[i][jForward]
                    else:
                        break
                if(numberForward != ''):
                    total += int(numberForward)
                    print(numberForward)
                if lines[i+1][j].isnumeric():
                    numberAbove = lines[i+1][j]
                    for jUpLeft in range(j-1, -1, -1):
                        if lines[i+1][jUpLeft].isnumeric():
                            numberAbove = lines[i+1][jUpLeft] + numberAbove
                        else:
                            break
                    for jUpRight in range(j+1, len(lines[i+1])):
                        if lines[i+1][jUpRight].isnumeric():
                            numberAbove = numberAbove + lines[i+1][jUpRight]
                        else:
                            break
                    if(numberAbove != ''):
                        print(numberAbove)
                        total += int(numberAbove)
                else:
                    if lines[i+1][j-1].isnumeric():  #upleft
                        numberAboveLeft = ''
                        for jUpLeft in range(j-1, -1, -1):
                            if lines[i+1][jUpLeft].isnumeric():
                                numberAboveLeft = lines[i+1][jUpLeft] + numberAboveLeft
                            else:
                                break
                        if(numberAboveLeft != ''):
                            print(numberAboveLeft)
                            total+= int(numberAboveLeft)
                    if lines[i+1][j+1].isnumeric():
                        numberAboveRight = '' #upright
                        for jUpRight in range(j+1, len(lines[i+1])):
                            if lines[i+1][jUpRight].isnumeric():
                                numberAboveRight = numberAboveRight + lines[i+1][jUpRight]
                            else:
                                break
                        if(numberAboveRight != ''):
                            print(numberAboveRight)
                            total += int(numberAboveRight)
                if lines[i-1][j].isnumeric():
                    print('Tiene just arriba')
                    numberBelow = lines[i-1][j]
                    for jDownLeft in range(j-1, -1, -1):
                        if lines[i-1][jDownLeft].isnumeric():
                            numberBelow = lines[i-1][jDownLeft] + numberBelow
                        else:
                            break
                    for jDownRight in range(j+1, len(lines[i-1])):
                        if lines[i-1][jDownRight].isnumeric():
                            numberBelow = numberBelow + lines[i-1][jDownRight]
                        else:
                            break
                    if(numberBelow != ''):
                        print(numberBelow)
                        total += int(numberBelow)
                else:
                    print('No tiene just arriba')
                    if lines[i-1][j-1].isnumeric():  #downleft
                        numberBelowLeft = ''
                        for jDownLeft in range(j-1, -1, -1):
                            if lines[i-1][jDownLeft].isnumeric():
                                numberBelowLeft = lines[i-1][jDownLeft] + numberBelowLeft
                            else:
                                break
                        if(numberBelowLeft != ''):
                            print(numberBelowLeft)
                            total += int(numberBelowLeft)
                    if lines[i-1][j+1].isnumeric():
                        numberBelowRight = '' #downright
                        for jDownRight in range(j+1, len(lines[i-1])):
                            if lines[i-1][jDownRight].isnumeric():
                                numberBelowRight = numberBelowRight + lines[i-1][jDownRight]
                            else:
                                break
                        if(numberBelowRight != ''):
                            print('Upright: ', numberBelowRight)
                            total += int(numberBelowRight)
                        else:
                            print('empty')
    print('1: ', total)    


def level2(file):
    with open(file) as file:
        lines = file.readlines()
    total = 0
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            char = lines[i][j]
            if isValidChar(char) and char == '*':
                adjacentNums = []
                #print(char)
                numberBack = ''
                for jBack in range(j-1, -1, -1):
                    if lines[i][jBack].isnumeric():
                        numberBack = lines[i][jBack] + numberBack
                    else:
                        break
                if(numberBack != ''):
                    adjacentNums.append(int(numberBack))
                    #print(numberBack)
                numberForward = ''
                for jForward in range(j+1, len(lines[i])):
                    if lines[i][jForward].isnumeric():
                        numberForward = numberForward + lines[i][jForward]
                    else:
                        break
                if(numberForward != ''):
                    adjacentNums.append(int(numberForward))
                    #print(numberForward)
                if lines[i+1][j].isnumeric():
                    numberAbove = lines[i+1][j]
                    for jUpLeft in range(j-1, -1, -1):
                        if lines[i+1][jUpLeft].isnumeric():
                            numberAbove = lines[i+1][jUpLeft] + numberAbove
                        else:
                            break
                    for jUpRight in range(j+1, len(lines[i+1])):
                        if lines[i+1][jUpRight].isnumeric():
                            numberAbove = numberAbove + lines[i+1][jUpRight]
                        else:
                            break
                    if(numberAbove != ''):
                        #print(numberAbove)
                        adjacentNums.append(int(numberAbove))
                else:
                    if lines[i+1][j-1].isnumeric():  #upleft
                        numberAboveLeft = ''
                        for jUpLeft in range(j-1, -1, -1):
                            if lines[i+1][jUpLeft].isnumeric():
                                numberAboveLeft = lines[i+1][jUpLeft] + numberAboveLeft
                            else:
                                break
                        if(numberAboveLeft != ''):
                            #print(numberAboveLeft)
                            adjacentNums.append(int(numberAboveLeft))
                    if lines[i+1][j+1].isnumeric():
                        numberAboveRight = '' #upright
                        for jUpRight in range(j+1, len(lines[i+1])):
                            if lines[i+1][jUpRight].isnumeric():
                                numberAboveRight = numberAboveRight + lines[i+1][jUpRight]
                            else:
                                break
                        if(numberAboveRight != ''):
                            #print(numberAboveRight)
                            adjacentNums.append(int(numberAboveRight))
                if lines[i-1][j].isnumeric():
                    #print('Tiene just arriba')
                    numberBelow = lines[i-1][j]
                    for jDownLeft in range(j-1, -1, -1):
                        if lines[i-1][jDownLeft].isnumeric():
                            numberBelow = lines[i-1][jDownLeft] + numberBelow
                        else:
                            break
                    for jDownRight in range(j+1, len(lines[i-1])):
                        if lines[i-1][jDownRight].isnumeric():
                            numberBelow = numberBelow + lines[i-1][jDownRight]
                        else:
                            break
                    if(numberBelow != ''):
                        #print(numberBelow)
                        adjacentNums.append(int(numberBelow))
                else:
                    #print('No tiene just arriba')
                    if lines[i-1][j-1].isnumeric():  #downleft
                        numberBelowLeft = ''
                        for jDownLeft in range(j-1, -1, -1):
                            if lines[i-1][jDownLeft].isnumeric():
                                numberBelowLeft = lines[i-1][jDownLeft] + numberBelowLeft
                            else:
                                break
                        if(numberBelowLeft != ''):
                            #print(numberBelowLeft)
                            adjacentNums.append(int(numberBelowLeft))
                    if lines[i-1][j+1].isnumeric():
                        numberBelowRight = '' #downright
                        for jDownRight in range(j+1, len(lines[i-1])):
                            if lines[i-1][jDownRight].isnumeric():
                                numberBelowRight = numberBelowRight + lines[i-1][jDownRight]
                            else:
                                break
                        if(numberBelowRight != ''):
                            #print(numberBelowRight)
                            adjacentNums.append(int(numberBelowRight))
                        else:
                            break
                            #print('empty')
                if len(adjacentNums) == 2:
                    if adjacentNums[0] < adjacentNums[1]:
                        print('gear has adjacent [' + str(adjacentNums[0]) + ' ' +  str(adjacentNums[1]) + ']')
                    else:
                        print('gear has adjacent [' + str(adjacentNums[1]) + ' ' +  str(adjacentNums[0]) + ']')
                    total += adjacentNums[0] * adjacentNums[1]            
    print('2: ', total)                

#level1('./input1.txt')
level2('./inputbasi.txt')