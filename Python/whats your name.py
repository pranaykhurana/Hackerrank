def print_full_name(first, last):
    # Write your code here
    hello_string = "Hello %s %s! You just delved into python."
    print(hello_string % (first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)