

def get_input():
    return str(input('Enter a Name : '))


def detector():
    user_input = get_input()
    rev_input = ''
    i = len(user_input)-1

    while i >= 0:
        rev_input += user_input[i]
        i -= 1

    print(rev_input)

detector()