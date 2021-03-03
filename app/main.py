import random

# Dictionary containing possible symbols
SYMBOLS = {
    "U": [chr(x) for x in range(ord('A'), ord('Z') + 1)],  # uppercase
    "L": [chr(x) for x in range(ord('a'), ord('z') + 1)],  # lowercase
    "D": [chr(x) for x in range(ord('0'), ord('9') + 1)],  # digits
    "S": [x for x in '!@#$%^&*()']  # special characters
}


def ask_password_count():
    """Asks user for a password count. Handles non-numeric
    input gracefully and validates input so it only accepts
    numbers between 1 and 50.

    :return: the password count
    """
    while True:
        try:
            count = int(input('Password length (1..50): '))
            if not 1 <= count <= 50:
                print('Length must be between 1 and 50.')
            else:
                return count
        except ValueError:
            print('Please enter a number.')


def ask_symbol_types():
    """Asks user which symbols should be used. The types of
    symbols can be toggled by entering the letter of the type,
    e.g., U for uppercase, D for digits, etc.
    """
    symbols = list(SYMBOLS.keys())
    while True:
        print('Use: (Press <enter> to accept selection)')
        print('  U)ppercase:', 'Y' if 'U' in symbols else 'N')
        print('  L)owercase:', 'Y' if 'L' in symbols else 'N')
        print('  D)igits:', 'Y' if 'D' in symbols else 'N')
        print('  S)ymbols:', 'Y' if 'S' in symbols else 'N')
        data = input('> ')
        if data == '':
            if symbols:
                return symbols
            else:
                print('You must select at least one group!')

        s = data[0].upper()
        if s in symbols:
            symbols.remove(s)
        else:
            symbols.append(s)


def generate_password(count, symbols):
    """Generate the password based on the count and the
    list of symbol types.
    """
    selected_symbols = []
    for x in SYMBOLS.keys():
        if x in symbols:
            selected_symbols += SYMBOLS[x]

    sample = random.choices(selected_symbols, k=count)
    return ''.join(sample)


def main():
    count = ask_password_count()
    symbols = ask_symbol_types()
    print(generate_password(count, symbols))


if __name__ == '__main__':
    main()
