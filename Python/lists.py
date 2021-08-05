"""
I HAVE USED AN ACTION METHODOLOGY WHICH IS OFTEN USED IN HIGH FREQUENCY TRADING PLATFORMS TO EXECUTE ACTIONS, UPDATE VALUES, ETC
IN A PROFESSIONAL ENVIRONMENT, ACTIONS WOULD BE CONVERTED TO A CLASS FOR EFFICIENCY AND PROPER PRACTICE
"""
def insertAction(tempLst, action):
    # action receives something like ->
    # insert 0 5
    action_split = action.split(" ")
    pos = int(action_split[1])
    item = int(action_split[2])

    if pos >= 0:
        tempLst.insert(pos, item)
    
    return tempLst

def printAction(tempLst):
    if(len(tempLst) > 0):
        print(tempLst)
    
    else:
        print("Trying to print an empty list")


def removeAction(tempLst, action):
    action_split = action.split(" ")
    item = int(action_split[1]) 

    if(len(tempLst) > 0 ):
        tempLst.remove(item)
    
    else:
        print("Trying to remove item from an empty list")

    return tempLst

def appendAction(tempLst, action):
    action_split = action.split(" ")
    item = int(action_split[1]) 
    tempLst.append(item)

    return tempLst

def sortAction(tempLst):
    if(len(tempLst) > 0):
        return sorted(tempLst)
    
    else:
        print("Trying to sort an empty list")
        return tempLst

def popAction(tempLst):
    if(len(tempLst) > 0):
        popped_element = tempLst.pop(len(tempLst) - 1)
    
    else:
        print("Trying to pop from  an empty list")

    return tempLst

def reverseAction(tempLst):
    return list(reversed(tempLst))

if __name__ == '__main__':
    N = int(input())

    # number list to which the actions will be performed
    number_lst = []

    # create a list to store the actions and input them into the list
    actions = []
    for i in range(N):
        actions.append(str(input()))
    

    for action in actions:
        action_split = action.lower().split(" ")
        action_verb = str(action_split[0])

        if action_verb == "insert":
            number_lst = insertAction(number_lst, action)

        
        elif action_verb == "print":
            printAction(number_lst)

        
        elif action_verb == "remove":
            number_lst = removeAction(number_lst, action)

        elif action_verb == "append":
            number_lst = appendAction(number_lst, action)

        
        elif action_verb == "sort":
            number_lst = sortAction(number_lst)

        
        elif action_verb == "pop":
            number_lst = popAction(number_lst)

        
        elif action_verb == "reverse":
            number_lst = reverseAction(number_lst)
        
        else:
            print("---------------------------\n")
            print("ACTION NOT FOUND ERROR IN LOOP")

