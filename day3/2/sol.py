
with open("data.txt", "r") as f:
    x = 0
    trees = 0
    square = 0
    lim = 30
    line = f.readline()
    cont = 1
    for line in f:
        cont += 1
        if (cont % 2) == 0:
            continue
        x += 1
        if x > lim:
            x = (x-lim) - 1
        if line[x] == "#":
            trees += 1
        if line[x] == ".":
            square += 1
        
    print (trees)
    print(square)