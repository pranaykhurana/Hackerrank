if __name__ == '__main__':
    count = int(input())
    finalSet = set()
    for i in range(count):
        temp = input()
        if temp not in  finalSet:
            finalSet.add(temp)
    
    print(len(finalSet))