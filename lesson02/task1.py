# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
# файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого: Создать
# функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В
# этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
# поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
# «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
# каждого файла); Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
#  получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий
# CSV-файл; Проверить работу программы через вызов функции write_to_csv().

import glob
import re
import csv


def get_data():
    info_files = glob.glob('info_?.txt')

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    os_lists = [os_prod_list, os_name_list, os_code_list, os_type_list]

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

    for file in info_files:
        with open(file, 'r', encoding='utf-8') as info_file:
            for line in info_file:
                for index in range(len(headers)):
                    match = re.search('({}:\s+)(.*)'.format(headers[index]), line)
                    if match:
                        os_lists[index].append(match.group(2))

    main_data = list(map(list, zip(*os_lists)))
    main_data.insert(0, headers)
    return main_data


def write_to_csv(link):
    with open(link, 'w', newline='') as data:
        data_writer = csv.writer(data, quoting=csv.QUOTE_NONNUMERIC)
        data_writer.writerows(get_data())


write_to_csv("test.csv")
