if __name__ == '__main__':
    s = input()

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0

    for item in s:
        if item.isalnum():
            c1 += 1
        
        if item.isalpha():
            c2 += 1
        
        if item.isdigit():
            c3 += 1
        
        if item.islower():
            c4 += 1
        
        if item.isupper():
            c5 += 1

    print(True) if c1 > 0 else print(False)
    print(True) if c2 > 0 else print(False)
    print(True) if c3 > 0 else print(False)
    print(True) if c4 > 0 else print(False)
    print(True) if c5 > 0 else print(False)