"""
TODO: fix int conversion 
"""
if __name__ == '__main__':
    inputs = int(input())
    numList = []
    for i in range(inputs):
        numList.append(input())

    for n in numList:
        n = n.split(" ")
        n = [int(x) for x in n]

        try:
            print(n[0]/n[1])
        except Exception as e:
            print("Error Code: ", e)

