
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tempList = []
    for i in integer_list:
        tempList.append(i)
    finalTuple = tuple(tempList)
    print(hash(finalTuple))
