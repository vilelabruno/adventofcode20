with open("data.txt", "r") as f:
    globalSum = 0
    letters = []
    dictLetters = {}
    localSum = 0
    qttYes = []
    i =0
    f = f.read()
    groups = f.split("\n\n")
    for group in groups:
        
        persons = group.split("\n")
        for person in persons:
            for letter in person:
                if letter not in letters:
                    letters.append(letter)
                    dictLetters[letter] = 1
                    if dictLetters[letter] == len(persons):
                        globalSum += 1
                else:
                    dictLetters[letter] += 1
                    if dictLetters[letter] == len(persons):
                        globalSum += 1
        
        letters = []
    print(globalSum)