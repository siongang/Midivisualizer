import sys
import os
import shutil
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QLabel,QDialog, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QToolBar, QPushButton, QFileDialog
from PySide6.QtGui import QPalette, QColor, QAction
from app_logic import AppLogic


file_opened = False
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

        self.preview_layout = QVBoxLayout()
        self.control_layout = QHBoxLayout()
        
        self.generate_button = QPushButton("generate")
        
        self.control_layout.addWidget(self.generate_button)
        self.preview_panel.addLayout(self.preview_layout)
        self.preview_panel.addLayout(self.control_layout)

        # self.preview_panel.addWidget(Color('red'))

        self.preview_panel.addLayout(self.preview_layout)
        
        self.preview_panel.addLayout(self.control_layout)
        # self.preview_panel.setLayout(self.preview_panel)

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

        self.generate_button.clicked.connect(self.current_project.generate_vid)
        
        file_opened = True
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

        self.speed_slider = Speed_Slider(instrument)


        self.instrument_wrapper = QVBoxLayout()
        
        self.name_label = QLabel(f"{name.strip()}")
        self.instrument_wrapper.addWidget(self.name_label)


        self.button_wrapper = QHBoxLayout()

        self.colour_button = QPushButton("colour")
        self.colour_button.clicked.connect(self.set_instrument_colour)
        self.button_wrapper.addWidget(self.colour_button)
        
        self.speed_button = QPushButton("speed")
        self.speed_button.clicked.connect(lambda: self.speed_slider.show_slider(self.speed_button)) # another lambda function
        self.button_wrapper.addWidget(self.speed_button)
        self.instrument = instrument

        
   
        
        
        self.instrument_wrapper.addLayout(self.button_wrapper)
        self.setLayout(self.instrument_wrapper)
        # self.setLayout(self.layout)

        
    # def set_instrument_speed(self):

    #     self.speed_popup = QWidget(self, Qt.Popup) # making the popup widget
    #     self.speed_popup.setWindowFlags(self.speed_popup.windowFlags() | Qt.Popup)
    #     self.speed_popup.setLayout(QVBoxLayout())

    #     self.speed_slider = QtWidgets.QSlider(Qt.Horizontal)
    #     self.speed_popup.layout().addWidget(self.speed_slider) # you can only add widgets to layouts
        
    #     self.speed_popup.show()
        

        

            

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


class Speed_Slider(QWidget):
    def __init__(self, instrument):
        super().__init__()


        self.speed_popup = QWidget(self, Qt.Popup) # making the popup widget
        self.speed_popup.setWindowFlags(self.speed_popup.windowFlags() | Qt.Popup)
        self.speed_popup.setLayout(QVBoxLayout())
        self.speed_slider = QtWidgets.QSlider(Qt.Horizontal)
        self.speed_popup.layout().addWidget(self.speed_slider) # you can only add widgets to layouts


        self.slider_values = [0.4, 0.6, 0.8, 1, 2, 3, 4]

        # setting range of the slider [indices]
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(len(self.slider_values) - 1)
        
        # default value is 1
        self.speed_slider.setValue(self.slider_values.index(1))
        self.speed = 1
        instrument.speed = self.speed

        self.speed_slider.sliderMoved.connect(lambda p: self.set_slider(p, instrument)) # lambda function to take in multipel arguments still a bit confused
    
    def set_slider(self, p, instrument):
        self.speed = self.slider_values[p]
        instrument.speed = self.speed
        print(self.speed)
        

    def show_slider(self, button):
        # print("show slider")
        self.speed_slider.value = self.speed
        slider_pos = button.mapToGlobal(button.rect().bottomLeft())
        self.speed_popup.move(slider_pos)
        self.speed_popup.show()



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