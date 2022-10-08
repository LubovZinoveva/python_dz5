# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

import json

def load():
    fname = input('Выберите файл формата JSON: ') + '.json'
    with open(fname, 'r', encoding = 'utf-8') as fh:
        BD = json.load(fh)
    return BD

def save(a):
    name_file = input('Название файла для сохранения: ') + '.json'
    with open(name_file, 'w') as fh:
        fh.write(json.dumps(a))

def get_argumenrs(polinom):
    result = polinom.split()
    result = [result[i] for i in range(len(result)-2) if i % 2 == 0]
    res = []
    count = 0

    for i in result:
        res.append(i.split('*'))
        count += 1 
    result.clear()

    for i in range(len(res)): 
            result.append(int(res[i][0]))
    return result

def sum_arguments(polinom1, polinom2):
    a = get_argumenrs(polinom1)
    b = get_argumenrs(polinom2)
    n1 = len(a)
    n2 = len(b)
    n = n2-n1
    result = []
    if n < 0:
        n *= -1
        b2 = []
        for _ in range(n):
            b2.append(0)
        for i in range(n2):
            b2.append(b[i])
        result = list(map(sum, zip(a, b2)))
    else:
        a2 = []
        for _ in range(n):
            a2.append(0)
        for i in range(n1):
            a2.append(a[i])
        result = list(map(sum, zip(a, b2)))
    return result

def get_polynomial(coefficients):
    result = []
    n = len(coefficients) - 1
    count = 0
    for i in range(n, 0, -1):
        if coefficients[count] == 0:
            count += 1
            continue
        if i == 1:
            result.append(f'{coefficients[count]}*x + ')
            count += 1
        else:
            result.append(f'{coefficients[count]}*x^{i} + ')
            count += 1
            
    result.append(f'{coefficients[count]} = 0')
    return result

try:
    equation1 = load()
    print(equation1)
    equation2 = load()
    print(equation2)
    args = sum_arguments(equation1, equation2)
    total = ''.join(get_polynomial(args))
    save(total)
    print(total)
except:
    print('Ошибка, введите имя файла без расширения')