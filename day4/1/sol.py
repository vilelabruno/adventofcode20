with open("data.txt", "r") as f:
    fields = 0
    passpt = 0
    validPassp = 0
    cidFound = False
    fieldsAr = []
    for line in f:
        if line == "\n":
            passpt += 1
            if ((fields == 7) and (not cidFound)) or (fields == 8): #
                print(fieldsAr)
                print(fields)
                validPassp += 1
            cidFound = False
            fieldsAr = []
            fields = 0
            continue
        line = line.split(" ")
        fieldsAr.append(line)
        fields += len(line)
        for field in line:
            if "cid" == field.split(":")[0]:
                cidFound = True
    print(validPassp)