# Написать программу сравнения текстовых файлов:
# 1.Сравнение файла, вывод различий между файлами
# 2.Перезапись старого файла со всеми изменениями


#Класс для выделения изменений в тексте
class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   YELLOW = '\033[93m'
   BOLD = '\033[1m'
   END = '\033[0m'

#Функция получения данных из текстового файла
def open_text_file (text_file):
    with open (text_file, 'r') as file:
        text = file.readlines()
    return text

#Функция сравнения строк в двух текстах
def compare_strings (string_one, string_two):
    if string_one != string_two:
        print(color.RED + '- ' + string_one + color.END)
        print(color.GREEN + '+ ' + string_two + color.END)

#Функция сравнения строк, при добавлении/удалении пустой строки
def compare_empty_strings(text_one, text_two):
    step = 0            #Шаг цикла
    counter_one = 0     #Счетчик для первого текста
    counter_two = 0     #Счетчик для второго текста
    #Цикл для сравнения строк (если имеется пустая строка в одном из файлов)
    while step < min(len(text_one) - 1, len(text_two) - 1):
        if text_one[counter_one] == '\n' and text_two[counter_two] != '\n':
            print(color.RED + color.BOLD + '- Deleted empty line. Line ' + (str(counter_one + 1)) + color.END + '\n')
            counter_one +=1
            compare_strings(text_one[counter_one], text_two[counter_two])
        elif text_two[counter_two] == '\n' and text_one[counter_one] != '\n':
            print(color.GREEN + color.BOLD + '+ Added empty line. Line ' + (str(counter_two + 1)) + color.END + '\n')
            counter_two += 1 
            compare_strings(text_one[counter_one], text_two[counter_two])
        else:
            compare_strings(text_one[counter_one], text_two[counter_two])
        counter_one += 1
        counter_two +=1
        step = max(counter_one, counter_two)
    #Если длинная массива у файлов разная, добавлен обработчик, выдающий добавленный в конце текст, которого нет 
    # (или он сдвинулся из-за удаления) в другом тексте
    if len(text_one) > len(text_two):
        print(color.RED + color.BOLD + 'End of file. Text deleted' + color.END)
        for string in text_one[counter_one:]:
            print(color.RED + string + color.END, end = '')
    elif len(text_one) < len(text_two):
        print(color.GREEN + color.BOLD + 'End of file. Text added' + color.END)
        for string in text_two[counter_one:]:
            print(color.GREEN + string + color.END, end = '')

#Функция перезаписи текста в старом файле
def rewrite_text(url_text_one, text_two):
    text_overwriting = input('\n' + color.YELLOW + 'Do you want to rewrite first file? (y = yes, n = no): ' + color.END)
    if text_overwriting.lower() == 'y':
        with open (url_text_one, 'w') as file:
            file.writelines(text_two)


#Ссылки на файлы в папке
url_text_one = 'texts/text_before.txt'
url_text_two = 'texts/text_after.txt'

#Вызов функций для обработки текстов
first_text = open_text_file(url_text_one)
second_text = open_text_file(url_text_two)
compare_empty_strings(first_text, second_text)
rewrite_text(url_text_one, second_text)


