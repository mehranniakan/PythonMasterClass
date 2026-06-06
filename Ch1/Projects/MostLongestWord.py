def get_user_input():
    return str(input("Enter a Sentence: "))


def set_user_output(count, value):
    if count == 1:
        print(f'{count}st longest word: {value}')
    elif count == 2:
        print(f'{count}nd longest word: {value}')
    else:
        print(f'{count}th longest word: {value}')


def detector():
    words_dict = {}
    sentence = get_user_input()

    for i in sentence.split():
        words_len = len(i)

        words_dict[i] = words_len


    max = 0
    for key, value in words_dict.items():

        if value > max:

            max = value
        else:
            continue

    counter = 0
    for k , v in words_dict.items():
        if v == max:
            counter += 1
            set_user_output(counter, k)





detector()
