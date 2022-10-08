# Напишите программу, удаляющую из текста все слова, содержащие "абв"

data = "Привет, как абвдела дела? Яабв Я нормально нормаабвльно."
print(f'Исходный текст: {data}')
list_data = data.split()
list_data = list(filter(lambda x: 'абв' not in x, list_data))
data = " ".join(list_data)
print(f'Исправленный текст: {data}')

