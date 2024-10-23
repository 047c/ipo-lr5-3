with open("text.txt", 'r') as file:  # Открываем файл, выдав имя file
    stroka = file.read()  # Получаем строку
slova = stroka.split()  # Разделяем ее на слова, записав в список
print(f'Количество слов в файле "text.txt" {len(slova)}')  # Выдаем сообщение с количеством слов
