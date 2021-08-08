def average(array):
    setArray = set(array)
    length = len(setArray)
    avg = 0.000
    for a in setArray:
        avg += float(a)
    
    avg = float(avg) / float(length)
    return float(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)