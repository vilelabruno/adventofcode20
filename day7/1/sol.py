
with open("data.txt", "r") as f:
    f = f.read().split("\n")
    bagsToSearch = []
    bags = 0

    for line in f:

        st = line.split("bags")
        st.pop(0)
        st = ''.join(st)
        if "shiny gold" in st:
            f.remove(line)
            bagsToSearch.append(line.split("bags")[0])
            bags += 1
    while len(bagsToSearch) != 0:
            
        for bag in bagsToSearch:
            bagsToSearch.remove(bag)
            for line in f:
                st = line.split("bags")
                st.pop(0)
                st = ''.join(st)
                if bag in st:

                    f.remove(line)
                    bagsToSearch.append(line.split("bags")[0])
                    bags += 1

    print(bags)