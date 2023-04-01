# Zestaw 3. Napisz funkcję szyfrującą wiadomość szyfrem cezara. Dla ułatwienia należy przekształcić wiadomość tak aby zawierała tylko wielkie lub małe litery.
# Funkcja przyjmuje:
# wiadomość - tekst do zaszyfrowania
# klucz – liczbę o ile należy przesunąć litery w alfabecie
# zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. (40%)
# Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej zaszyfrowanej wiadomości bez zmian(10%)
# Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres listy  z alfabetem oraz problem podania klucza o dowolnej wielkości(20%).
# Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego(10%).


def caesar_cipher(message, key, alphabet='abcdefghijklmnopqrstuvwxyz'):
    message = message.lower()
    result = ''
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + key) % len(alphabet)
            result += alphabet[shifted_index]
        else:
            result += char
    return result

print(caesar_cipher("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 5))

