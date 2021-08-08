from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
if  __name__ == '__main__':
    options = int(input())
    inventoryLst = ([int(x) for x in input().split(" ")])
    countedLst = Counter(inventoryLst)
    nCustomer = int(input())
    offerLst = []

    for x in range(nCustomer):
        item = input().split(" ")
        offerLst.append(item)
 
    sales = 0
    for o in offerLst:
        if countedLst[int(o[0])] > 0:
            countedLst[int(o[0])] -= 1
            sales += int(o[1])
    
    print(sales)
        