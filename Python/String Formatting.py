def print_formatted(number):
    length = len(bin(number))
    for i in range(1, number+1, 1):
        print(" " *(length-len(str(i))), i, " " *(length-len(oct(i))), oct(i), " " *(length-len(hex(i))), hex(i), " " *(length-len(bin(i))), bin(i))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)