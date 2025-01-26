import unittest
from ..database import setup_database

class TestNoteDatabase(unittest.TestCase):
    def test_notes_database_functions(self):
        setup_database.setup_database('test.db')#создаём тестовую базу данных если её ещё нет
        notes = [{'id' : 1, 'username': 'Test', 'title': 'Test Note', 'content': 'Test Content', 'status': 'Test Status',
                  'created_date': '22-12-2222', 'issue_date': '23-12-2222'}] #создаём список с тестовой заметкой
        setup_database.save_note_to_db(notes[0], 'test.db') #сохраняем тестовую заметку в базу данных
        loaded_notes = setup_database.load_notes_from_db('test.db') #загружаем все сохранённые заметки
        self.assertEqual(notes, loaded_notes) #сравниваем результаты до загрузки и после неё
        setup_database.delete_note_from_db(notes[0]['id'], 'test.db')#удаляем тестовую заметку чтобы проверить
                                                                            #работает ли удаление из базы данных а заодно
                                                                            #делаем наш тест пригодным для последующего воспроизведения

if __name__ == '__main__':#запускаем все тесты
    unittest.main()
