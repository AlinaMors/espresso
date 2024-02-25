import io
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableView" name="tableView">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>60</y>
      <width>371</width>
      <height>301</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>400</y>
      <width>121</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>посмотреть таблицу</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>30</y>
      <width>104</width>
      <height>21</height>
     </rect>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:8.14286pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:8.14286pt;&quot;&gt;КОФФФЕЕЕЕ&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
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

    def setup_button_groups(self):
        # Здесь ваш код для настройки группы кнопок, если это необходимо
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())