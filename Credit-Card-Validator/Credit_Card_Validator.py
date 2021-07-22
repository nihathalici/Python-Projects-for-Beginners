# this function adds every digit of the card number to a list and,
# applying Luhn Algorithm to check whether resulting sum is divisible by ten
def check_validity(num):
    validlist = []
    for i in num:
        validlist.append(int(i))
    for i in range(0, len(num), 2):
        validlist[i] = validlist[i] * 2
        if validlist[i] >= 10:
            validlist[i] = (validlist[i] // 10 + validlist[i] % 10)

    if sum(validlist) % 10 == 0:
        print("This is a VALID CARD!")
    else:
        print('INVALID CARD NUMBER')

# accepts card number as a string
def cardnumber():
    n = ''
    while True:
        try:
            n = input('Enter your 16 digit credit card number : ')
            if not (len(n) == 16) or not type(int(n) == int):
                raise Exception

        except Exception:
            print('That is not a valid credit card number. \nMake sure you are entering digits not characters and all the 16 digits.')
            continue
        else:
            break
    return n

def goagain():
    return input('Do you want to check again? (Yes/No) : ').lower()[0] == 'y'


def main():

    while True:

        num = cardnumber()
        check_validity(num)

        if not goagain():
            break

if __name__ == '__main__':
    main()
