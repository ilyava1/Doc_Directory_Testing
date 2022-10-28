# Модуль  - Профессиональная работа с Python
# Домашнее задание «Разработка тестов» (на базе одного из ранних ДЗ ниже)

# Модуль - Основы языка программирования Python
# ДЗ по теме: Функции — использование встроенных и создание собственных
# Задания-1-2, Ведение каталога документов

from doc_operations import *
from doc_directory_db import *


user_intention = True
while user_intention == True:
    command = input_command()
    if command == 'p':
        doc_num = input_doc_num()
        doc_owner_name(doc_num, documents)
    elif command == 's':
        doc_num = input_doc_num()
        doc_shelf(doc_num, directories)
    elif command == 'l':
        doc_list(documents)
    elif command == 'ls':
        doc_shelf_list(documents, directories)
    elif command == 'a':
        doc_num = input_doc_num()
        doc_type = input_doc_type()
        doc_owner = input_doc_owner()
        doc_shelf = input_doc_shelf()
        add_new_doc(doc_num, doc_type, doc_owner, doc_shelf, documents,
                    directories)
    elif command == 'd':
        doc_num = input_doc_num()
        delete_doc(doc_num, documents, directories)
    elif command == 'm':
        doc_num = input_doc_num()
        doc_shelf = input_doc_shelf()
        move_doc(doc_num, doc_shelf, directories)
    elif command == 'as':
        doc_shelf = input_doc_shelf()
        add_doc_shelf(doc_shelf, directories)
    elif command == 'h':
        help_me()
    elif command == 'x':
        user_intention = False
        print('Работа завершена')
    else:
        print('Такой команды не существует')
    print()
