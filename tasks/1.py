# /usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант - 9

if __name__ == "__main__":
    vowels = {"a", "e", "i", "o", "u"}

    try:
        with open("1.txt", "r", encoding="utf-8") as file:
            text = file.readlines()
            for line in text:
                words = line.split()
                for word in words:
                    word = word.strip(".,")
                    if (word[0].lower() in vowels) and (
                        word[-1].lower() in vowels
                    ):
                        print(word)

    except FileNotFoundError:
        print("There is no file with that name")
