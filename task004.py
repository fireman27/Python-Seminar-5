"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных."""
"""Входные и выходные данные хранятся в отдельных текстовых файлах."""

with open('text.txt', 'w') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('text.txt', 'r') as file:
    text = file.readline()
    txt_compr = text.split()

def rle_encod(text):
    encond = ''
    prev_char = '' 
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_compr = rle_encod(text)

with open('text__words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')
print(txt_compr)