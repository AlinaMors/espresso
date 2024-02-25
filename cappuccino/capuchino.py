import io
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow,  QTableWidgetItem, QDialog
from PyQt5 import uic

class EditForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("edit_form.ui", self)
        self.setWindowTitle("Edit Coffee")
        self.ui.pushButton_save.clicked.connect(self.save_data)

    def save_data(self):
        # Получаем данные из полей ввода и сохраняем их в базу данных
        name = self.ui.lineEdit_name.text()
        # Добавьте код для получения остальных данных
        connection = sqlite3.connect('coffee.sqlite')
        cur = connection.cursor()
        cur.execute("INSERT INTO coffee (name) VALUES (?)", (name,))
        connection.commit()
        connection.close()
        self.close()

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>EditForm</class>
 <widget class="QMainWindow" name="EditForm">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Edit Coffee</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>20</y>
      <width>71</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Name:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_name">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>20</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_save">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>240</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Save</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setup_button_groups()
        self.setFixedSize(800, 800)
        self.create_data_base()
        self.pushButton.clicked.connect(self.show_table)
        # Подключаем обработчик события для кнопки добавления записи
        self.pushButton_add.clicked.connect(self.open_edit_form)

    def setup_button_groups(self):
        pass

    def create_data_base(self):
        connection = sqlite3.connect('coffee.sqlite')
        cur = connection.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS coffee(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    coffee_old TEXT NOT NULL,
                    form TEXT NOT NULL,
                    taste TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    volume REAL NOT NULL
                    )''')
        connection.commit()
        connection.close()
# НОВАЯ ЧАСТЬ КОДА,где кнопки добавляютс
    def show_table(self):
        connection = sqlite3.connect('coffee.sqlite')
        cur = connection.cursor()
        cur.execute("SELECT * FROM coffee")
        data = cur.fetchall()
        self.tableWidget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
        connection.close()

    def open_edit_form(self):
        edit_form = EditForm()
        edit_form.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())
