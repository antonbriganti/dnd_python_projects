def print_list(lst):
    for i in range(len(lst)):
        print(i, lst[i]) if not isinstance(lst[0], list) else print(i, lst[i][0])

def input_loop(lst, prompt):
    flag = True
    while flag:
        print_list(lst)
        try:
            ind = int(input(prompt))
        except ValueError:
            ind = -1

        if 0 <= ind <= len(lst)-1:
            return ind

        print('Bad input, try again. \n')
