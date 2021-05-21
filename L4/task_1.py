# 1. перечень всех документов
documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

# 2.перечень полок, на которых хранятся документы 
# (если документ есть в documents, то он обязательно должен быть и в directories)

directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}

# bonus: список доступных команд
avl_cmds = [
  ( 'p', 'найти владельца документа по его номеру')
, ( 's', 'по номеру документа узнать полку хранения')
, ( 'l', 'полная информация по всем документам')
, ('as', 'добавить новую полку')
, ('ds', 'удалить существующую полку')
, ('ad', 'добавить новый документ')
, ( 'd', 'удалить существующий документ')
, ( 'm', 'переместить документ на другую полку')
, ('h|?', 'помощь')
, ( 'q', 'выход из программы')
]


def help():
    print('Список доступных команд:')
    for c in avl_cmds:
        print(f'{c[0]} - {c[1]}')
    print()


def det_shelf_by_doc(doc_num):
    for x in directories.items():
        if doc_num in x[1]:
            return x[0]


def show_all_shelves():
    print('Текущий перечень полок: ', *directories)


def show_name_by_doc():
    x = input('Введите номер документа: ')
    for d in documents:
        if d['number'] == x:
            print(f'Владелец документа: {d["name"]}')
            return
    print('Документ не найден в базе.')


def show_shelf_by_doc():
    x = input('Введите номер документа: ')
    y = det_shelf_by_doc(x)
    if not y is None:
        print(f'Документ хранится на полке: {y}')
    else:
        print('Документ не найден в базе.')


def show_all():
    print('Текущий список документов:')
    for d in documents:
        print(f'№: {d["number"]}, тип: {d["type"]}, владелец: {d["name"]}, полка хранения: {det_shelf_by_doc(d["number"])}' )


def add_new_shelf():
    x = input('Введите номер полки: ')
    if x in directories:
        print('Такая полка уже существует.', end = '')
    else:
        directories[x] = []
        print('Полка добавлена.', end = '')
    show_all_shelves()


def del_empty_shelf():
    x = input('Введите номер полки: ')
    y = directories.get(x, 'xz')
    if y == 'xz':
        print('Такой полки не существует.', end = '')
    elif len(y) != 0:
        print('На полке есть документы, удалите их перед удалением полки.', end = '')
    else:
        del(directories[x])
        print('Полка удалена.')
    show_all_shelves()


def drop_doc(dd):
    for d in documents:
        if d['number'] == dd:
            documents.remove(d)
            y = det_shelf_by_doc(dd)
            directories[y].remove(dd)
            return True


def del_doc():
    x = input('Введите номер документа: ')
    if drop_doc(x):
        print('Документ удален.')
    else:
        print('Документ не найден в базе.')
    show_all()


def move_doc():
    x = input('Введите номер документа: ')
    y = input('Введите номер полки: ')

    z = directories.get(y, 'xz')
    if z == 'xz':
        print('Такой полки не существует.', end = '')
        show_all_shelves()
    elif det_shelf_by_doc(x) is None:
        print('Документ не найден в базе.', end = '')
        show_all()
    elif det_shelf_by_doc(x) == y:
        print('Документ и так уже находится на этой полке.')
        show_all()
    else:
        # удаляем документ из одной полки
        directories[det_shelf_by_doc(x)].remove(x)
        # ставим документ на другую полку
        directories[y].append(x)
        print('Документ перемещен.')
        show_all()


def add_doc():
    d = input('Введите номер документа: ')
    t = input('Введите тип документа: ')
    n = input('Введите владельца документа: ')
    s = input('Введите полку для хранения: ')
    
    z = directories.get(s, 'xz')
    if z == 'xz':
        print('Такой полки не существует.', end = '')
        show_all_shelves()
    else:
        documents.append({'type': t, 'number': d, 'name': n})
        directories[s].append(d)
        print('Документ добавлен. ', end = '')
        show_all()


def main():
    help()
    cmd = input('Введите команду: ')
    while  cmd != 'q':
        if cmd == 'p':
            show_name_by_doc()
        elif cmd == 's':
            show_shelf_by_doc()
        elif cmd == 'l':
            show_all()
        elif cmd == 'as':
            add_new_shelf()
        elif cmd == 'ds':
            del_empty_shelf()
        elif cmd == 'ad':
            add_doc()
        elif cmd == 'd':
            del_doc()
        elif cmd == 'm':
            move_doc()
        elif cmd in ['h','?']:
            help()
        else:
            print(f'{cmd} - неизвестная команда')
        cmd = input('Введите команду: ')


main()

print('Happy End!')
