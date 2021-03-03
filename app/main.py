import random

uchars = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
lchars = [chr(x) for x in range(ord('a'), ord('z') + 1)]
digits = [chr(x) for x in range(ord('0'), ord('9') + 1)]
special = [x for x in '!@#$%^&*()']
all = uchars + lchars + digits + special


def ask_password_count():
    while True:
        try:
            count = int(input('Password length (1..50): '))
            if not 0 < count < 50:
                print('Length must be between 1 and 50.')
            else:
                return count
        except ValueError:
            print('Please enter a number.')




def main():
    count = ask_password_count()
    sample = random.sample(all, count)
    print(''.join(sample))


if __name__ == '__main__':
    main()
