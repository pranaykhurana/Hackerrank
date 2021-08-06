import textwrap

def wrap(string, max_width):
    finalString = ""
    for i in range(0, len(string), int(max_width)):
        finalString += string[i:i+max_width] + '\n'
    return finalString

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
