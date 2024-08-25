from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QScrollArea, QFrame

app = QApplication([])

# Main widget
main_widget = QWidget()
main_layout = QVBoxLayout(main_widget)

# Create a container widget for the scroll area
scroll_container = QWidget()
scroll_layout = QVBoxLayout()

# Add multiple child layouts or widgets to the scrollable container
for i in range(10):  # Example: 20 rows of child layouts
    child_layout = QHBoxLayout()
    child_layout.addWidget(QPushButton(f"Button {i+1}A"))
    child_layout.addWidget(QPushButton(f"Button {i+1}B"))
    child_layout.addWidget(QPushButton(f"Button {i+1}C"))
    
    # Add each child layout to a container widget
    child_widget = QWidget()
    child_widget.setLayout(child_layout)
    
    # Add the child widget to the scroll layout
    scroll_layout.addWidget(child_widget)

# Set the layout for the scrollable container
scroll_container.setLayout(scroll_layout)

# Create the scroll area and set the container widget as its widget
scroll_area = QScrollArea()
scroll_area.setWidget(scroll_container)
scroll_area.setWidgetResizable(True)

# Add the scroll area to the main layout
main_layout.addWidget(scroll_area)

# Set the main layout to the main widget
main_widget.setLayout(main_layout)
main_widget.setWindowTitle("Scrollable Layout Example")
main_widget.resize(400, 300)  # Set an initial size
main_widget.show()

app.exec()