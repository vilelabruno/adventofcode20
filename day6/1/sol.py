with open("data.txt", "r") as f:
    globalSum = 0
    letters = []
    localSum = 0
    qttYes = []
    i =0
    f = f.read()
    groups = f.split("\n\n")
    for group in groups:
        group = group.replace("\n", "")
        for letter in group:
            if letter not in letters:
                letters.append(letter)
        globalSum += len(letters)
        letters = []
    print(globalSum)