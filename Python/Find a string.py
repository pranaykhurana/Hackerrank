def count_substring(string, sub_string):
    # save lengths of both the strings
    sub_string_length = len(sub_string)
    string_length = len(string)

    count = 0
    # iterate over the string in steps of substring length
    # for example: string-ABCDCDC, for loop would produce ABC, BCD, CDC,DCD ...
    # check if the substring is present in these produced string, increase count if true
    for i in range(string_length):
        search_string = string[i:i+sub_string_length]
        if sub_string in search_string:
            count += 1
    return count
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)