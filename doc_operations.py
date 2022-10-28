def input_command():
    command = input('Введите команду (h - справка по списку команд, '
          'x - выход): ')
    return command


def input_doc_num():
    """
    Функция пользовательского ввода номера документа.

    :return: введенный пользователем номер документа
    """
    doc_number = input('Введите номер документа: ')
    return doc_number


def input_doc_type():
    """
    Функция пользовательского ввода типа документа

    :return: введенный пользователем тип документа
    """
    doc_type = input('Введите тип документа: ')
    return doc_type


def input_doc_owner():
    """
    Функция пользовательского ввода владельца документа.

    :return: введенный пользователем владелец документа
    """
    doc_owner = input('Введите фамилию и имя владельца документа: ')
    return doc_owner


def input_doc_shelf():
    """
    Функция пользовательского ввода полки хранения документа

    :return: введенная пользователем полка хранения документа
    """
    doc_shelf = input('Введите номер полки хранения документа: ')
    return doc_shelf


def doc_owner_name(doc_num, documents):
    """
    Вывод имени владельца документа.

    Функция запрашивает номер документа и на основании введенного номера
    находит в  каталоге и выводит имя его владельца
    """

    print()
    print('Определение владельца документа:')
    name = 'Документ с таким номером в каталоге отсутствует'
    for document in documents:
        if doc_num in document.values():
            name = document['name']
            print('Документ принадлежит человеку: ', end='')
    print(name)
    return name


def doc_shelf(doc_number, directories):
    """
    Вывод номера полки хранения документа.

    Функция запрашивает номер документа и на основании введенного номера
    находит в каталоге и выводит номер полки хранения докумета.
    """

    print()
    print('Определение места хранения документа:')
    shelf = 'Документ с таким номером в каталоге отсутствует'
    for key, value in directories.items():
        if doc_number in value:
            shelf = key
            print('Указанный документ находится на полке ', end='')
    print(shelf)
    return shelf


def doc_list(documents):
    """
    Вывод каталога всех документов.

    Документы выводятся в формате^
    passport "2207 876234" "Василий Гупкин".
    """

    print()
    print('Документы:')
    new_documents = []
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" '
              f'"{document["name"]}"')
        new_documents.append(document)
    return new_documents

def doc_shelf_list(documents, directories):
    """
    Вывод каталога всех документов и полок.

    В зависимости от параметра commamd функция выведет каталог всех документов
    или каталог всех докментов и каталог всех полок. Документы выводятся
    в формате passport "2207 876234" "Василий Гупкин".
    """

    print()
    print('Документы:')
    new_documents = []
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" '
              f'"{document["name"]}"')
        new_documents.append(document)

    print()
    new_directories = {}
    print('Размещение на полках:')
    for shelf, documents in directories.items():
        print(f'полка: {shelf}, докyменты: {documents}')
        new_directories[shelf] = documents
    return new_documents, new_directories


def add_new_doc(new_doc_number, new_doc_type, new_doc_owner, new_doc_shelf,
                documents, directories):
    """
    Добавление нового документа в каталог.

    Функция выведет список всех документов в формате
    passport "2207 876234" "Василий Гупкин".
    """

    print()
    print('Добавление нового документа:')
    new_doc = {'number': new_doc_number, 'type': new_doc_type,
               'name': new_doc_owner}
    if new_doc_shelf in directories:
        documents.append(new_doc)
        directories[new_doc_shelf].append(new_doc_number)
        result = f'Документ {new_doc_type} номер {new_doc_number} добавлен на' \
                 f' полку {new_doc_shelf}'
        print(result)
        return result
    else:
        result = f'Полки номер {new_doc_shelf} не существует'
        print(result)
        return result


def delete_doc(doc_number, documents, directories):
    """
    Удаление документа из каталога.

    Функция спросит номер документа и удалит его из каталога
    и из перечня полок.
    """

    print()
    print('Удаление документа:')
    temporary_docs = documents
    temporary_directory = None
    temporary_shelf = None
    for document in documents:
        if doc_number in document.values():
            temporary_docs.remove(document)
            for shelf, numbers in directories.items():
                if doc_number in numbers:
                    temporary_directory = numbers
                    temporary_shelf = shelf
                    temporary_directory.remove(doc_number)
                    break
            break

    if temporary_directory != None:
        documents = temporary_docs
        directories[temporary_shelf] = temporary_directory
        result = f'Документ номер {doc_number} удален из каталога ' \
                 f'и с полки {temporary_shelf}'
        print(result)
    else:
        result = 'Документ с таким номером в каталоге отсутствует'
        print(result)
    return result


def move_doc(doc_number, shelf_number, directories):
    """
    Перемещение документа между полками каталога.

    Функция спросит номер документа и целевую полку и переместит его с текущей
    полки на целевую.
    """

    print()
    print('Перемещение документа:')

    if shelf_number in directories:
        for self, docs in directories.items():
            if doc_number in docs:
                docs.remove(doc_number)
                directories[shelf_number].append(doc_number)
                result = f'Документ номер {doc_number} ' \
                         f'перемещен на полку {shelf_number}'
                print(result)
                return result
    else:
        result = f'Полки номер {shelf_number} нет в каталоге'
        print(result)
        return result


def add_doc_shelf(shelf_number, directories):
    """
    Добавление новой полки.

    Функция запрашивает номер новой полки и добавит ее в перечень.
    """

    print()
    print('Добавление новой полки:')
    if shelf_number not in directories.keys():
        directories[shelf_number] = []
        result = f'Полка {shelf_number} добавлена'
        print(result)
        return result
    else:
        result = 'Полка с таким номером уже существует'
        print(result)
        return result


def help_me():
    print()
    print('Список команд для работы с каталогом документов:')
    print('p - people - команда, которая спросит номер документа и выведет имя'
          ' человека, которому он принадлежит;')
    print('s - shelf - команда, которая спросит номер документа и выведет'
          ' номер полки, на которой он находится;')
    print('l (ls) - list - команда, которая выведет список всех документов'
          ' (ls - документов и полок c размещением) в формате'
          ' passport "2207 876234" "Василий Гупкин";')
    print('a - add - команда, которая добавит новый документ в каталог'
          ' и в перечень полок, спросив его номер, тип, имя владельца'
          ' и номер полки, на котором он будет храниться.')
    print('d - delete - команда, которая спросит номер документа и удалит его'
          ' из каталога и из перечня полок;')
    print('m - move - команда, которая спросит номер документа и целевую полку'
          ' и переместит его с текущей полки на целевую;')
    print('as - add shelf - команда, которая спросит номер новой полки'
          ' и добавит ее в перечень;')
    print('x - exit - команда, которая завершает работу программы')
    print()
    return
