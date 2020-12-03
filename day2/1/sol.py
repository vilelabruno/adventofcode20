with open("data.txt", "r") as f:
    validPasswd = 0
    for line in f:
        passwd = line.split(":")[1]
        passwd = passwd[1:]
        principalLetter = line.split(":")[0].split(" ")[1]
        minLim = int(line.split(":")[0].split(" ")[0].split("-")[0])
        maxLim = int(line.split(":")[0].split(" ")[0].split("-")[1])
        cont = 0
        for letter in passwd:
            if letter == principalLetter:
                cont += 1
        
        if (cont >= minLim) and (cont <= maxLim):
            validPasswd += 1
    
    print(validPasswd)