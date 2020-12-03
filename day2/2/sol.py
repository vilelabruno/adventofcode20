with open("data.txt", "r") as f:
    validPasswd = 0
    for line in f:
        passwd = line.split(":")[1]
        passwd = passwd[1:]
        principalLetter = line.split(":")[0].split(" ")[1]
        minLim = int(line.split(":")[0].split(" ")[0].split("-")[0])
        maxLim = int(line.split(":")[0].split(" ")[0].split("-")[1])

        print(passwd[minLim-1])
        if (passwd[minLim-1] == principalLetter) and (passwd[maxLim-1] != principalLetter):
            validPasswd += 1
        if (passwd[minLim-1] != principalLetter) and (passwd[maxLim-1] == principalLetter):
            validPasswd += 1
    
    print(validPasswd)