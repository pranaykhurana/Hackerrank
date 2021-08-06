def print_formatted(number):
    # your code goes here
    length = len(bin(number))
    for i in range(1, number+1, 1):
        spaces_d = ""
        spaces_o = ""
        spaces_h = ""
        spaces_b = ""

        print(" ")*(number-len(str(i))
        # print(str(number))
        # for k in range(1, number+1-len(oct(number)), 1):
        #     spaces_o += " "
        # print(oct(number))
        # for l in range(1, number+1-len(hex(number)), 1):
        #     spaces_h += " "
        # print(hex(number))
        # for m in range(1, number+1-len(bin(number)), 1):
        #     spaces_b += " "
        # print(bin(number))

        # decimal_string = spaces_d + str(number)
        # octal_string = spaces_o + oct(number)
        # hex_string = spaces_h + hex(number)
        # bin_string = spaces_b + bin(number)
        

if __name__ == '__main__': 
    n = int(input())
    print_formatted(n)