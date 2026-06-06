
def get_user_input(count):
    if count == 1:
        user_input = list(map(int, input(f'Enter {count}st row of matrix (space between) :').split()))
    elif count == 2:
        user_input = list(map(int, input(f'Enter {count}nd row of matrix (space between) :').split()))
    else:
        user_input = list(map(int, input(f'Enter {count}th row of matrix (space between) :').split()))

    return user_input


def matrix_setter():

    counter = 1
    column_size = 0
    matrix = []

    while True:

        user_input = get_user_input(counter)

        if counter > 1:

            if column_size != len(user_input):
                print('row size does not match last one')
                continue
            else:
                matrix.append(user_input)
                counter += 1
        else:
            column_size = len(user_input)
            matrix.append(user_input)
            counter += 1

        continue_clause = input('Do you want to add another row? (y/n) ')

        if continue_clause != 'y':
            break

    return matrix


def calculator():

    matrix = matrix_setter()

    print(50 * '=')

    counter = 0

    for i in matrix:
        counter += 1
        row_sum = 0

        for j in i:
            row_sum += j


        if counter == 1:
            print(f'Sum of {counter}st rows of matrix is: {row_sum}')
        elif counter == 2:
            print(f'Sum of {counter}nd rows of matrix is: {row_sum}')
        else:
            print(f'Sum of {counter}th row of matrix is: {row_sum}')

    print(50*'=')
    column_sum = [sum(col) for col in zip(*matrix)]

    for i, column_sum in enumerate(column_sum, 1):
        print(f"Sum of {i}th column of matrix is: {column_sum}")

calculator()