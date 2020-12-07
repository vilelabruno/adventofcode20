with open("data.txt", "r") as f:
    fields = 0
    passpt = 0
    validPassp = 0
    cidFound = False
    validFields = True
    fieldsAr = []
    colorsEye = ["amb","blu","brn","gry","grn","hzl","oth"]
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    letters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','#']
    for line in f:
        if line == "\n":
            passpt += 1
            if (((fields == 7) and (not cidFound)) or (fields == 8)) and validFields: #
                print(fieldsAr)
                print(fields)
                validPassp += 1
                #input()
            validFields = True
            cidFound = False
            fieldsAr = []
            fields = 0
            continue
        line = line.split(" ")
        fieldsAr.append(line)
        fields += len(line)
        for field in line:
            fieldName = field.split(":")[0].strip()
            fieldValue = field.split(":")[1].strip()
            if fieldName == "byr":
                if (len(fieldValue) != 4) or (int(fieldValue) < 1920) or (int(fieldValue) > 2002):
                    validFields = False
            elif fieldName == "iyr":
                if (len(fieldValue) != 4) or (int(fieldValue) < 2010) or (int(fieldValue) > 2020):
                    validFields = False
            elif fieldName == "eyr":
                if (len(fieldValue) != 4) or (int(fieldValue) < 2020) or (int(fieldValue) > 2030):
                    validFields = False
            elif fieldName == "hgt":
                if ("cm" in fieldValue): 
                    fieldValue = int(fieldValue[:len(fieldValue) - 2])
                    if (fieldValue < 150) or (fieldValue > 193):
                        validFields = False
                elif ("in" in fieldValue):
                    fieldValue = int(fieldValue[:len(fieldValue) - 2])
                    if (fieldValue < 59) or (fieldValue > 76):
                        validFields = False
                else:
                    validFields = False
            elif fieldName == "hcl":
                if "#" not in fieldValue:
                    validFields = False
                else:
                    for letter in fieldValue:
                        if letter not in letters:
                            validFields = False
            elif fieldName == "ecl":
                if fieldValue not in colorsEye:
                    validFields = False
            elif fieldName == "pid":
                if len(fieldValue) != 9:
                    validFields = False
                else:
                    for letter in fieldValue:
                        if letter not in numbers:
                            validFields = False 
            elif fieldName == "cid":
                cidFound = True
    print(validPassp)