from itertools import product


if __name__ == '__main__':
    lst1 = input()
    lst2 = input()

    lst1 = lst1.split(" ")
    lst2 = lst2.split(" ")

    lst1 = ([int(item1) for item1 in lst1])
    lst2 = ([int(item2) for item2 in lst2])
    
    prodLst = list(product(lst1, lst2))
    for x in prodLst:
        print(x, end=" ")