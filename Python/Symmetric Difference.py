if __name__ == '__main__':
    Asize = int(input())
    Aset = set(list(map(int, input().split(" "))))
    Bsize = int(input())
    Bset = set(list(map(int, input().split(" "))))
    finalSetA = Aset.difference(Bset)
    finalSetb = Bset.difference(Aset)
    finalList = []
    for x in finalSetA:
        finalList.append(x)
    
    for y in finalSetb:
        finalList.append(y)

    finalList.sort()
    
    finalSet = set()
    for z in finalList:
        finalSet.add(z)
        print(z)