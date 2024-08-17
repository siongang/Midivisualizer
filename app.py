import sys
import os
import shutil
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QLabel,QDialog, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QToolBar, QPushButton, QFileDialog
from PySide6.QtGui import QPalette, QColor, QAction
from app_logic import AppLogic
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # Get the directory where the current script is located
        self.project_directory = os.path.dirname(os.path.abspath(__file__))
        
    

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
        self.main_window = QHBoxLayout()
        self.instruments_panel = QVBoxLayout()
        self.preview_panel = QVBoxLayout()

        self.preview_panel.addWidget(Color('red'))
        # self.instruments_panel.addWidget(Color('blue'))
        
        self.main_window.addLayout(self.instruments_panel)
        self.main_window.addLayout(self.preview_panel)

        self.widget = QWidget()
        self.widget.setLayout(self.main_window)
        self.setCentralWidget(self.widget)

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
        shutil.move(source_file, destination_path) #Moving the file to database
        self.current_project = AppLogic(destination_path)
        self.current_project.process_midi()

        for instr in self.current_project.instruments:
            # self.instruments_panel.addLayout(QVBoxLayout())
            self.instruments_panel.addWidget(Instrument(instr.name, instr))

        # self.current_project.generate_vid()
        # self.instruments_panel.update()    
        # self.setLayout(self.instruments_panel)
            # self.instruments_panel.addWidget(Color('red'))


class Instrument(QWidget):
    def __init__(self, name, instrument):
        super().__init__()

         # Setting Background Colour
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#C5C5C5"))  #  grey background
        self.setPalette(palette)


        self.instrument_wrapper = QVBoxLayout()
        
        self.name_label = QLabel(f"{name.strip()}")
        self.instrument_wrapper.addWidget(self.name_label)


        self.button_wrapper = QHBoxLayout()

        self.colour_button = QPushButton("colour")
        self.colour_button.clicked.connect(self.set_instrument_colour)
        self.button_wrapper.addWidget(self.colour_button)
        
        self.speed_button = QPushButton("speed")
        self.speed_button.clicked.connect(self.set_instrument_speed)
        self.button_wrapper.addWidget(self.speed_button)
        self.instrument = instrument

        

        
        self.instrument_wrapper.addLayout(self.button_wrapper)
        self.setLayout(self.instrument_wrapper)
        # self.setLayout(self.layout)

        
    def set_instrument_speed(self):
       
        pass
    def set_instrument_colour(self):
        dlg = QtWidgets.QColorDialog(self)
        if self.instrument.colour:
            print(self.instrument.colour)
            dlg.setCurrentColor(QtGui.QColor(*self.instrument.colour)) #* is for unpacking into seperate arguments
        if dlg.exec(): # returns true when user confirms selection
            colour = dlg.currentColor()
            rgb = (colour.red(), colour.green(), colour.blue())
            self.instrument.colour = rgb
            print(self.instrument.colour)

        pass



class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        self.layout = QHBoxLayout()

        self.name_label = QLabel("f{name}")
        
        self.layout.addWidget(self.name_label)
        self.setLayout(self.layout)

       

# app = QApplication(sys.argv)

# # window = MainWindow()
# # window.show()

# app.exec()