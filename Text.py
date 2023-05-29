"""
Text.py: první projekt do Engeto Online Python Akademie
author: David Novotný
email: ahodak@seznam.cz
discord: David N.#7946
"""
from task_template import TEXTS

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# přihlášení uživatele
username = input("Enter a username: ")
password = input("Enter password: ")

if users.get(username) != password:
    print("Uregistered user, terminating the program....")
    exit()

print("-" * 30, f"Welcome to the app, {username}", "We have 3 texts to be analyzed.", "-" * 30, sep="\n")

# výběr textu k analýze
selected_text = input("Select the text to analyze (1, 2, 3): ")
print("-" * 30)

if not selected_text.isdigit() or int(selected_text) not in range(1, 4):
    print("Invalid text selection, terminating the program..")
    exit()

words = TEXTS[int(selected_text) - 1].split(" ")
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

print(f"There are {word_count} words in the selected text.")
print(f"There are {title_count} titlecase words.")
print(f"There are {upper_count} uppercase words.")
print(f"There are {lower_count} lowercase words.")
print(f"There are {digit_count} numeric strings.")
print(f"The sum of all the numbers are {sum_numbers}")

word_lengths = {}

# projdeme slova a spočítáme jejich délky
for word in words:
    length = len(word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

# projdeme všechny délky slov a vytvoříme řetězec s délkou slov a hvězdičkami
output = ""
for length in sorted(word_lengths.keys()):
    output += f'{length:2}|{"*" * word_lengths[length]:16}|{word_lengths[length]:2}\n'

# vytiskneme hlavičku a oddělovací čáru
print("-" * 30)
print("EN|  OCCURENCES    |NR.")
print("-" * 30)

# vytiskneme řetězec s délkou slov a hvězdičkami
print(output)










