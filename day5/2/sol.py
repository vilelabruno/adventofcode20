with open("data.txt", "r") as f:
    maxSeat = 0
    seatsAr = []
    for line in f:
        rowMin = 0
        rowMax = 127
        colMin = 0
        colMax = 7
        row = 0
        col = 0
        for i in range(0,7):
            letter = line[i]
            if letter == "F":
                rg = rowMax - rowMin
                rowMin = rowMin
                rowMax = int(rg/2) + rowMin
                row = rowMin
            elif letter == "B":
                rg = rowMax - rowMin
                rowMin = rowMax - (int(rg/2) ) 
                rowMax = rowMax
                row = rowMax
        for i in range(7,10):
            letter = line[i]
            if letter == "L":
                rg = colMax - colMin
                colMin = colMin
                colMax =( int(rg/2)) + colMin
                col = colMin
            elif letter == "R":
                rg = colMax - colMin
                colMin = colMax - (int(rg/2) ) 
                colMax = colMax
                col = colMax
        seatID = (row * 8) + col
        seatsAr.append(seatID)
        if seatID > maxSeat:
            maxSeat = seatID
    for i in range(818):
        if i not in seatsAr:
            print(i)
