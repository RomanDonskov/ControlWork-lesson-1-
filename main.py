import datetime
from controller import Controller
from model import Model
from note import Note



c = Controller(Model("notes.json"))

def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Введите заголовок заметки: ')
    text = input('Введите тело заметки: ')
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input('Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print('Введите целое положительное число!')
while True:
    print("\033c", end="")
    command = input('1 - создать заметку\n'
                    '2 - прочитать заметку\n'
                    '3 - редактировать заметку\n'
                    '4 - удалить заметку\n'
                    '5 - удалить все заметки\n'
                    '6 - прочитать все заметки\n'
                    '7 - выход\n'
                    )
    if command == '7':
            break

    if command == '1':
          print('\nСоздать заметку:')
          c.create_note(get_note_data())

    elif command == '2':
         print('\nПрочитать заметку:')
         if c.notes_exist():
             c.show_note(int(get_number()))
    elif command == '3':
         if c.notes_exist():
             print('\nРедактировать заметку:')
             updated_id = int(get_number())
             if c.note_id_exist(updated_id):
                c.update_note(updated_id, get_note_data())

    elif command == '4':
         if c.notes_exist():
            print('\nУдалить заметку:')
            delete_id = int(get_number())
            if c.note_id_exist(delete_id):
               c.delete_note(delete_id)

    elif command == '5':
            if c.notes_exist():
                print('\nУдалить все заметки:')
                if input('Вы точно хотите удалить все заметки? (Y/N): ').capitalize() == 'Y':
                 if c.notes_exist():
                   c.delete_all_notes()

    elif command == '6':
           if c.notes_exist():
                print('\nСписок всех заметок:')
                c.show_notes()
           else:
            print('Не верная команда!')


