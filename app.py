import sys
import os
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QToolBar, QFileDialog
from PySide6.QtGui import QPalette, QColor, QAction

class MainWindow(QMainWindow):

    def __init__(self, logic):
        super(MainWindow, self).__init__()
        # Get the directory where the current script is located
        self.project_directory = os.path.dirname(os.path.abspath(__file__))
        
        self.logic = logic

        self.setWindowTitle("My App")

        # making a menu bar
        menu = self.menuBar()
        # making an option in the menu bar
        file_menu = menu.addMenu("&File")
        
        # menu bar actions
        open_action = QAction("&Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file_dialog)

        # add open action to file option in menu bar
        file_menu.addAction(open_action)
       
        



        # Layout stuff
        layout = QHBoxLayout()
        instruments = QVBoxLayout()
        preview = QVBoxLayout()

        preview.addWidget(Color('red'))
        instruments.addWidget(Color('blue'))
        
        layout.addLayout(instruments)
        layout.addLayout(preview)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_file_dialog(self):
        # ", _" means to disregard the second item in the tuple
        source_file, _ = QFileDialog.getOpenFileName(self, "Open File")
        save_folder = "midi"
        project_directory = self.project_directory
        # get the file name without the directory paths
        file_basename = os.path.basename(source_file)
        destination_path = os.path.join(project_directory,save_folder)
        destination_path = os.path.join(destination_path, file_basename)

        
        print(source_file)
        print(destination_path)
        shutil.move(source_file, destination_path)
        

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)



# app = QApplication(sys.argv)

# # window = MainWindow()
# # window.show()

# app.exec()