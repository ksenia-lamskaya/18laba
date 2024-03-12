# /usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант - 9

import random


def generate_password():
    with open("words.txt", "r") as file:
        words = file.read().split(",")

    clean_words = [word.strip() for word in words]

    word1 = random.choice(clean_words)
    word2 = random.choice(clean_words)

    while len(word1) < 3 or len(word2) < 3:
        word1 = random.choice(clean_words)
        word2 = random.choice(clean_words)

    word1 = word1.capitalize()
    word2 = word2.capitalize()

    password = word1 + word2

    return password


if __name__ == "__main__":
    password = generate_password()
    print(f"Generated Password: {password}")
