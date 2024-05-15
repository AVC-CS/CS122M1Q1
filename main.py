

def main():
    number = []
    evencnt = 0

    for i in range(10):
        number.append(int(input('Enter a number: ')))

    on = prev = 0
    for i in range(len(number)):
        if on == 0 and prev == 1 and number[i] % 2 == 0:
            evencnt += 1
            on = 1
        if number[i] % 2 == 1:
            on = 0

        prev = 0 if number[i] % 2 else 1

    print(evencnt)
    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return evencnt


if __name__ == '__main__':
    main()
