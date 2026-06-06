import sys
import uuid

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QListWidget, QTextEdit, \
    QListWidgetItem, QLineEdit, QHBoxLayout, QVBoxLayout, QMessageBox


class NoteManager:
    Notes = []

    def add_note(self, title, content):
        id = uuid.uuid4()
        title = title.strip()
        content = content.strip()
        note_obj = {
            'id': id,
            'title': title,
            'content': content
        }
        self.Notes.append(note_obj)
        return True

    def delete_note(self, note_id):
        for item in self.Notes:
            if item['id'] == note_id:
                self.Notes.remove(item)
                return True

        return False


    def update_note(self,note_id,title,content):

        for item in self.Notes:
            if item['id'] == note_id:
                item['title'] = title
                item['content'] = content
                return True

        return False


    def get_notes(self, note_id):
        for item in self.Notes:
            if item['id'] == note_id:
                return item

        return False


    def get_note_list(self):
        return self.Notes


class NoteApp(QMainWindow) :

    note_list_label = None
    note_list = None
    note_input_label = None
    note_title_label = None
    note_title_input = None
    note_text_label = None
    note_text_input = None
    note_add_btn = None
    note_delete_btn = None
    note_update_btn = None
    note_clear_btn = None
    list_items = None
    selected_note = None

    def __init__(self):
        super().__init__()

        self.manager = NoteManager()
        self.create_widgets()
        self.setup_layouts()
        self.setup_connections()
        self.reload_list()
        self.clear_selection()


    def create_widgets(self):

        ## Left side widgets
        self.note_list_label = QLabel(self)
        self.note_list_label.setText('Note List')
        self.note_list = QListWidget(self)

        ## Right side widgets
        self.note_input_label = QLabel(self)
        self.note_input_label.setText('Note Input')

        self.note_title_label = QLabel(self)
        self.note_title_label.setText('Title')
        self.note_title_input = QLineEdit(self)
        self.note_title_input.setPlaceholderText('Enter Your Note Title Here...')


        self.note_text_label = QLabel(self)
        self.note_text_label.setText('Text')
        self.note_text_input = QTextEdit(self)
        self.note_text_input.setPlaceholderText('Enter Your Note Title Here...')

        self.note_add_btn = QPushButton(self)
        self.note_add_btn.setText('Add')

        self.note_delete_btn = QPushButton(self)
        self.note_delete_btn.setText('Delete')

        self.note_update_btn = QPushButton(self)
        self.note_update_btn.setText('Update')

        self.note_clear_btn = QPushButton(self)
        self.note_clear_btn.setText('Clear Selection')


    def setup_layouts(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        left_layout.addWidget(self.note_list_label)
        left_layout.addWidget(self.note_list)
        left_widgets = QWidget()
        left_widgets.setLayout(left_layout)

        right_layout.addWidget(self.note_input_label)
        right_layout.addWidget(self.note_title_label)
        right_layout.addWidget(self.note_title_input)

        right_layout.addWidget(self.note_text_label)
        right_layout.addWidget(self.note_text_input)

        right_layout.addWidget(self.note_add_btn)
        right_layout.addWidget(self.note_delete_btn)
        right_layout.addWidget(self.note_update_btn)
        right_layout.addWidget(self.note_clear_btn)
        right_widgets = QWidget()
        right_widgets.setLayout(right_layout)

        main_layout.addWidget(left_widgets)
        main_layout.addWidget(right_widgets)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


    def setup_connections(self):

        self.note_add_btn.clicked.connect(lambda: self.add_note(self.note_title_input.text(), self.note_text_input.toPlainText()))
        self.note_list.itemClicked.connect(self.get_selected_item)
        self.note_delete_btn.clicked.connect(lambda : self.delete_note(self.selected_note['id']))
        self.note_update_btn.clicked.connect(lambda : self.update_note(self.selected_note['id'], self.note_title_input.text(), self.note_text_input.toPlainText()))
        self.note_clear_btn.clicked.connect(self.clear_selection)


    def reload_list(self):
        self.note_list.clear()
        for item in self.manager.get_note_list():
            self.list_items = QListWidgetItem()
            self.list_items.setText(item['title'])
            self.list_items.setData(1, item['id'])
            self.note_list.addItem(self.list_items)

    def add_note(self, title, content):
        title = self.note_title_input.text()
        content = self.note_text_input.toPlainText()

        if title and content:
            self.manager.add_note(title, content)
            self.reload_list()
            self.note_title_input.clear()
            self.note_text_input.clear()
        else:
            self.show_message('Input Error', 'Please Enter both title and text')

    def update_note(self, note_id, title, content):
        title = self.note_title_input.text()
        content = self.note_text_input.toPlainText()

        update = self.manager.update_note(note_id, title, content)
        if update:
            self.reload_list()
        else:
            self.show_message('Error', 'Something went wrong')

    def delete_note(self, note_id):
        delete = self.manager.delete_note(note_id)

        if delete:
            self.reload_list()
            self.clear_selection()
        else:
            self.show_message('Error', 'Something went wrong')

    def get_selected_item(self, item):
        self.selected_note = self.manager.get_notes(item.data(1))

        self.note_text_input.setText(self.selected_note['content'])
        self.note_title_input.setText(self.selected_note['title'])

        self.note_clear_btn.setEnabled(True)
        self.note_update_btn.setEnabled(True)
        self.note_delete_btn.setEnabled(True)
        self.note_add_btn.setEnabled(False)

    def clear_selection(self):
        self.note_clear_btn.setEnabled(False)
        self.note_update_btn.setEnabled(False)
        self.note_delete_btn.setEnabled(False)
        self.note_add_btn.setEnabled(True)

    def show_message(self,title ,message):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.exec_()

app = QApplication(sys.argv)

window = NoteApp()

window.show()

sys.exit(app.exec())