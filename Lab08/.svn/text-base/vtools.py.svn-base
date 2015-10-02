#!/usr/local/bin/python3.4
__author__ = 'ee364e10'

def is_valid_name(str):
    for i in str:
        if ((i >= '0') & (i <= '9')) | ((i >= 'a') & (i <= 'z'))| ((i >= 'A') & (i <= 'Z'))  | ( i == '_'):
            pass
        else:
            # print("The error is ", i)
            return False
    return True

def parse_pin_assignment(assignment):
    # print("assignmnt: ",assignment)
    if assignment[0] != '.':
        raise ValueError
    if not assignment.endswith(')'):
        # print("NUMEBR ZERO")
        raise ValueError
    assignment = assignment.strip('.')
    assignment = assignment.strip(')')
    list = assignment.split('((')
    # print("THIS IS LEN LIST: ",len(list))
    if len(list) == 1:
        assignment = list[0]
        list = assignment.split('(')
    else:
        # print("NUMBER ONE")
        raise ValueError
    # print("BEFORE: ",list , is_valid_name(list[0]) , is_valid_name(list[1]))
    if (not is_valid_name(list[0])) | (not is_valid_name(list[1])):
        print(list , is_valid_name(list[0]) , is_valid_name(list[1]))
        # print("NUMBER TWO")
        raise ValueError

    #return tuple pin name and wire name
    tup_list = []
    tup_list.append(list[0])
    tup_list.append(list[1])
    tup = tuple(tup_list)
    return tup

def parse_net(line):
    list = line.split('(')
    names = list[0].split()
    # print("names : ",names)
    list1 = line.split()
    str = ""
    c = 0
    # print(list1)
    for i in list1:
        if (c > 1):
            str += i
        c += 1

    # print(str)

    str = str.strip('(').strip(')')

    str_list = str.split(',')

    assignment_list = []
    c=1
    for j in str_list:
        # print(j)
        if c==len(str_list):
            j+=')'
        c+=1
        q = parse_pin_assignment(j)
        assignment_list.append(q)
    # print("list1 : ", list1)

    assignment_tup = tuple(assignment_list)
    tup_list = []
    tup_list.append(names[0])
    tup_list.append(names[1])
    tup_list.append(assignment_tup)
    tup = tuple(tup_list)
    return tup

if __name__ == "__main__":
    a = parse_net("OAI22X1     U11(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))")
    print(a)