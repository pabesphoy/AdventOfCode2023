with open('file.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    for letter in line:
        print(letter)
    
