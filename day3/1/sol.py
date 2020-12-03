with open("data.txt", "r") as f:
    x = 0
    trees = 0
    square = 0
    lim = 30
    line = f.readline()
    for line in f:
        x += 3
        if x > lim:
            x = (x-lim) - 1
        if line[x] == "#":
            trees += 1
        if line[x] == ".":
            square += 1
        
    print (trees)
    print(square)