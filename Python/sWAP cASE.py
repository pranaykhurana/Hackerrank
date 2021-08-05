def swap_case(s):
    finalString = ""
    for i in s:
        if i.isupper() == True:
            i = i.lower()
        else:
            i = i.upper()
        finalString += i
    return finalString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)