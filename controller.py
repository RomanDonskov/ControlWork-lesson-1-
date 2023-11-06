class Controller(object):

    def __init__(self, model):
        self.model = model


    def show_notes(self):
        notes = self.model.read_notes()
        for note in notes:
            print(note)

    def show_note(self, note_id):
        try:
            note = self.model.read_note(note_id)
            print(note)
        except ValueError:
            print(f'Заметка с id: {note.note_id} не найдена!')

    def create_note(self, note):
        self.model.create_note(note)
        print('Заметка добавлена!')

    def update_note(self, note_id, note):
        self.model.update_note(note_id, note)
        print(f'Заметка с id:{note_id} обновлена!')

    def delete_note(self, note_id):
        try:
            self.model.delete_note(note_id)
            print(f'Заметка с id: {note_id} удaлена!')
        except ValueError:
            print(f'Заметка с id: {note_id} не найдена!')

    def delete_all_notes(self):
        self.model.delete_all_notes()
        print('Все заметки удалены!')

    def notes_exist(self):
        notes = self.model.read_notes()
        if len(notes) == 0:
            print('Cписок заметок пуст!')
            return False
        else:
            return True

    def note_id_exist(self, search_id):
        notes = self.model.read_notes()
        for note in notes:
            if note.note_id == search_id:
                return True
        else:
            print(f'Заметка с id: {search_id} не найдена!')
            return False