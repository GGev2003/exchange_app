from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIntValidator
import requests

class Currency_getting:
    def __init__(self):
         self.curency = None
         self.amount = None
         self.to_currency = None
        

    def getting_currency(self):
        try:
            response = requests.get(f"https://v6.exchangerate-api.com/v6/631f93d5f0d4476da4931609/latest/{self.curency}")
            data = response.json()
           
            return round(data['conversion_rates'][self.to_currency] * float(self.amount),2),data
        except Exception as e:
            raise Exception(f"Failed to fetch currency data: {e}")


class Currency_app(Currency_getting):
    def __init__(self):
       super().__init__()
       self.label = None
       self.select = None
       self.select1 = None
       self.amount_input = None
       self.result =None
        
    def on_button_click(self):
       # Get choosen option for using in currency app 
        self.curency = self.select.currentText()
        self.to_currency = self.select1.currentText()
        self.amount = self.amount_input.text()

       
        try:
            if not self.amount:
                raise ValueError("Please enter an amount")
            
            try:
                amount_float = float(self.amount)
            except ValueError:
                raise ValueError("Please enter a valid amount")
            
            if  amount_float < 0:
                raise ValueError("Please enter a positive amount")
            
            self.result = self.getting_currency()
            self.label.setText(f"Result: {self.amount} {self.curency} = {self.result[0]} {self.to_currency}")
            self.label.setStyleSheet("color: black;")

        except ValueError as e:
            self.label.setText(str(e))
            self.label.setStyleSheet("color: red;")  # Make error message red
            

            self.amount_input.clear()
            self.amount_input.setFocus()
        
        except Exception as e:
            # Handle other exceptions (like API errors)
            self.label.setText(f"Error: {str(e)}")
            self.label.setStyleSheet("color: red;")
        

        


    def creating_app(self):
        # Initialize the QApplication instance (required for any Qt application)
        app = QApplication([])

        # Create the main application window
        window = QMainWindow()

        # Create a central widget that will contain other UI elements 
        widget = QWidget()
        
        # Set the title of the main window
        window.setWindowTitle("Currency Converter")

        # Set the window position (x, y) and dimensions (width, height)
        window.setGeometry(100, 100, 400, 300)

        # Creating layout
        layout = QVBoxLayout()

        # First selection
        self.select = QComboBox()
        self.select.addItems(["USD", "EUR", "GBP", "JPY","RUB","AMD"])

        # Second selection
        self.select1 = QComboBox()
        self.select1.addItems(["USD", "EUR", "GBP", "JPY","RUB","AMD"])

        # Amount input
        self.amount_input  = QLineEdit()
        self.amount_input .setPlaceholderText("Enter your name")
        # self.amount_input .setValidator(QIntValidator())

        # Converting button
        button = QPushButton("Convert!")
        button.clicked.connect(self.on_button_click)

        # Converted amount and style for element
        self.label = QLabel("Select currencies", parent=window)
        self.label.setFixedWidth(300)
        self.label.setFixedHeight(30)

        # Adding widgets in layout

        # Add "From Currency:" label to the layout
        layout.addWidget(QLabel("From Currency:"))

        # Add the first currency dropdown (self.select)
        layout.addWidget(self.select)

        # Add "To Currency:" label  
        layout.addWidget(QLabel("To Currency:"))

        # Add the second currency dropdown (self.select1)
        layout.addWidget(self.select1)

        # Add "Amount:" label
        layout.addWidget(QLabel("Amount:"))

        # Add the input field for the amount
        layout.addWidget(self.amount_input)

        # Add the convert button
        layout.addWidget(button)

        # Add the result display label  
        layout.addWidget(self.label)

        # Set the layout for the main widget
        widget.setLayout(layout)

        # Set the widget as the central widget of the main window  
        window.setCentralWidget(widget)

        # Giving elements styles
        app.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 16px;
                color: #333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 14px;
            }
            QComboBox {
                padding: 5px;
                font-size: 14px;
            }
             QLineEdit {
                margin-top:10px;
                padding: 5px;
                font-size: 14px;
                font-size: 16px;
                color: #333;
            }
        """)  

        # Display the main window
        window.show()

        # Start the Qt application event loop
        app.exec()
    

# 

if __name__ == "__main__":
    app = Currency_app()  
    app_show = app.creating_app()