import random

uchars = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
lchars = [chr(x) for x in range(ord('a'), ord('z') + 1)]
digits = [chr(x) for x in range(ord('0'), ord('9') + 1)]
special = [x for x in '!@#$%^&*()']
all = uchars + lchars + digits + special


def main():
    sample = random.sample(all, 10)
    print(''.join(sample))


if __name__ == '__main__':
    main()
