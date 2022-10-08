# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import json

def rle_compression(text):
    letters = [text[0]]
    repit = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
            if i == len(text) - 1:
                repit.append(count)
        else:
            repit.append(count)
            letters.append(text[i])
            count = 1
            if i == len(text) - 1:
                repit.append(count)    
    result = []
    for i in range(len(letters)):
        result.append(f'{repit[i]}')
        result.append(letters[i])
    press_text = "".join(result)
    return press_text

def data_recovery(data_text):
    counter = [int(data_text[i]) for i in range(0, len(data_text), 2)]
    letters = [data_text[i] for i in range(1, len(data_text), 2)]
    result = []
    for i in range(len(counter)):
        for j in range(counter[i]):
            result.append(letters[i])
    return ''.join(result)

def load():
    fname = input('Выберите файл формата JSON: ') + '.json'
    with open(fname, 'r', encoding = 'utf-8') as fh:
        BD = json.load(fh)
    return BD

def save(a):
    name_file = input('Название файла для сохранения: ') + '.json'
    with open(name_file, 'w') as fh:
        fh.write(json.dumps(a))

try:
    data = load()
    print(f'Исходный текст: {data}')
    my_compession = rle_compression(data)
    print(f'Сжатый текст: {my_compession}')
    save(my_compession)
    recovery_text = data_recovery(my_compession)
    print(f'Распакованный текст: {recovery_text}')
except: 
    print('Ошибка, введите имя файла без расширения')
