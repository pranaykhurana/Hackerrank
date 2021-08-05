if __name__ == '__main__':
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # add name and score to a dict
        records[name] = score
    
    # sort the dictionary based on highest score and convert to a list
    sorted_records = sorted(records.items(), key=lambda x:x[1])

    # get the second highest score
    score_list = []
    for i in sorted_records:
        if i[1] not in score_list:
            score_list.append(i[1])

        else:
            continue

    if len(score_list) >= 2:
        second_highest = score_list[1]
    
    else:
        second_highest = score_list[0]
    
    name_list = []
    for x in sorted_records:
        if x[1] ==  second_highest:
            name_list.append(x[0])
    
    name_list.sort()
    for n in name_list:
        print(n)

