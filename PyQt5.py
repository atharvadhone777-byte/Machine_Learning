import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QIcon, QLabel, QFont, QPixmap, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,QCheckBox,QRadioButton,QButtonGroup,QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")    #Window ka title set hoga
        self.setGeometry(0,0,500,500)   #First 2 are for position of window and second 2 are for width and height of window
        self.setWindowIcon(QIcon("image.jpg"))  #Window ka icon diye hue image se replace ho jayega and naya img as icon dikhega

        #labels
        label_obj=QLabel("Hello")          #Label laga dega window pe 
        label_obj.setFont(QFont("Arial",30))    #First is font-family and second is font size
        label_obj.setGeometry(0,0,500,100)      #First 2 sets position of label and later 2 sets width and height
        label_obj.setStyleSheet("background-color: blue;")  #It is CSS property to give font color & their are some other properties

        #images
        pixmap=QPixmap("image.jpg")             #Used to add image
        label_obj.setPixmap(pixmap)
        label_obj.setScaledContents(True)       #Fits(adjusts) the image in labels size  
        label_obj.setGeometry((self.height()-label_obj.height())//2, (self.width()-label_obj.width())//2, label_obj.height(), label_obj.width())
        #This above line sets label in mid of the window with image width and height being clear
        self.initUI()

        #Buttons
        #Makes a button with message written on it      #By adding self before button it can be now used by any function in that class  
        self.button = QPushButton("Click me!", self) 
        self.button.clicked.connected(self.on_click) #Each time you press button a function is called

        #Checkboxes
        self.checkbox=QCheckBox("Do you play",self)
        self.checkbox.stateChanged.connect(self.checked)

        #Radio buttons - clicked only one at a time
        self.radio1=QRadioButton("Visa",self)
        self.radio2=QRadioButton("Mastercard",self)

        self.radio1.toggled.connect(self.fuunc)        
        self.radio2.toggled.connect(self.fuunc)

        #line edit #A line edit along with a button is created
        self.line_edit=QLineEdit(self)  #An input in window has been created

        #CSS
        self.button1=QPushButton("#1")
        self.button2=QPushButton("#2")
        self.button3=QPushButton("#3")
 
    def initUI(self):   #initUI is used to make UI better in looks
        #Layout Manager
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        label1=QLabel("#1",self)
        label2=QLabel("#2",self)
        label3=QLabel("#3",self)

        vbox=QVBoxLayout()      #By using it lables ek ke upar ek nhi honge, seperate rahenge vertically =
        hbox=QHBoxLayout()      #Seperates horizontally ||
        vbox.addWidget(label1)  
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        central_widget.setLayout(vbox)

        grid=QGridLayout()      #Sets layout as grid
        grid.addWidget(label1,0,0)      #along with object name we have set its position also
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,1,0)
        central_widget.setLayout(grid) 
        
         #We can select a complete class of QPushButton by below    #CSS is same as plain CSS
        self.setStyleSheet("""
            QPushButton{
                    font-size:40px;                
                    border:3px;
                    } 
            QPushButton#button1{                #To apply CSS to single element use # after its Q class
                                font-size:30px;
                                }  
            QPushButton#button1:hover{          #Hover pseudo class is applied
                                     background-color:#fffff 
                                    }  
        
       """)
    
    def on_click(self):     #Created for buttons
        print("Button clicked")
        self.button.setText("Clicked!") #setText is used to change text after some action
        self.button.setDisabled(True)   #After one click button gets disabled  

    def checked(self,state):    #Created for checkbox
        print(state)    #2 if checked and 0 if not checked
        if state==2:    #Agar checked hoga tb hi ye pass hoga
            print("Checked the checkbox")   
        
    def fuunc(self):
        print("You selected something")
        radio_b=self.sender()
        if radio_b.isChecked():
            print(f"{radio_b.text()} is selected")  #This shoes which radio button is selected
    
    def submit(self):
        text = self.line_edit.text()    #Used to get data of that input
        print(f"{text}")                #Prints that input data

if __name__=="__main__":
    app=QApplication(sys.argv)  #Used to future proof our code
    window=MainWindow()     #Used to create window
    window.show()           #Used to show a window for a while
    sys.exit(app.exec_())   #Used to execute that objcet and shows window for long time

