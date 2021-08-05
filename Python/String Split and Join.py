def split_and_join(line):
    # write your code here
    line_split = line.split(" ")
    finalString = "-".join(line_split)
    return finalString



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)