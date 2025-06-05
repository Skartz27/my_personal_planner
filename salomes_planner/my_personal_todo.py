import sys
from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox
from my_todo import Ui_Dialog


class ToDoApp(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.pushButton.clicked.connect(self.add_task)

        self.progressBar.setValue(0)


        self.task_checkboxes = []

        self.task_checkboxes.extend([
            self.checkBox,
            self.checkBox_2,
            self.checkBox_3
        ])

        for cb in self.task_checkboxes:
            cb.stateChanged.connect(self.update_progress)

    def add_task(self):
        task_text = self.lineEdit.text()
        if not task_text:
            return

        new_checkbox = QCheckBox(task_text, self)
        new_checkbox.move(10, 3 + 30 * len(self.task_checkboxes))
        new_checkbox.stateChanged.connect(self.update_progress)
        new_checkbox.show()

        self.task_checkboxes.append(new_checkbox)
        self.lineEdit.clear()

        self.update_progress()


    def update_progress(self):

        total = len(self.task_checkboxes)
        if total == 0:
            self.progressBar.setValue(0)
            return

        completed = sum(1 for cb in self.task_checkboxes if cb.isChecked())
        percent = int((completed / total) * 100)
        self.progressBar.setValue(percent)



app = QApplication(sys.argv)
window = ToDoApp()
window.show()
sys.exit(app.exec_())
