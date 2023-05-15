"""
Text.py: první projekt do Engeto Online Python Akademie
author: David Novotný
email: ahodak@seznam.cz
discord: David N.#7946
"""
import task_template

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# přihlášení uživatele
username = input("Zadejte uživatelské jméno: ")
password = input("Zadejte heslo: ")

if users.get(username) == password:
    print("-" * 30, f"Welcome to the app, {username}", "We have 3 texts to be analyzed.", "-" * 30, sep="\n")

    # výběr textu k analýze
    selected_text = input("Vyberte text k analýze (1, 2, nebo 3): ")
    print("-" * 30)

    if selected_text.isdigit() and int(selected_text) in range(1, 4):
        words = task_template.TEXTS[int(selected_text) - 1].split()
        word_count = len(words)
        title_count = 0
        upper_count = 0
        lower_count = 0
        digit_count = 0
        sum_numbers = 0

        for word in words:
            if word.istitle():
                title_count += 1
            elif word.isupper():
                upper_count += 1
            elif word.islower():
                lower_count += 1
            elif word.isdigit():
                digit_count += 1
                sum_numbers += int(word)

        print(f"Počet slov: {word_count}")
        print(f"Počet slov začínajících velkým písmenem: {title_count}")
        print(f"Počet slov psaných velkými písmeny: {upper_count}")
        print(f"There are {lower_count} lowercase words.")
        print(f"There are {digit_count} numeric strings.")
        print(f"The sum of all the numbers are {sum_numbers}")

        word_lengths = {}

        # projdeme všechna slova a spočítáme jejich délky
        for word in words:
            length = len(word)
            if length in word_lengths:
                word_lengths[length] += 1
            else:
                word_lengths[length] = 1

        # inicializujeme řetězec pro výstup
        output = ""

        # projdeme všechny délky slov a vytvoříme řetězec s délkou slov a hvězdičkami
        for length in sorted(word_lengths.keys()):
            output += f'{length}| {"*" * word_lengths[length]} {word_lengths[length]}\n'

        # vytiskneme řetězec s délkou slov a hvězdičkami
        print("-" * 30)
        print(f"LEN |OCCURENCES |NR.")
        print("-" * 30, output, sep="\n")

    else:
        print("incorrect values, terminating the program..")







else:
    print("unregistered user, terminating the program..")
