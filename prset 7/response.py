from validators import email


def main():
    a = input('What is your email address? '.strip())
    if email(a) == True:
        print('Valid')
    else:
        print('Invalid')



if __name__ == '__main__':
    main()
