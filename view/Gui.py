'''
from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed
import cv2
import time
from threading import Thread
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Gui:
    def __init__(self):
        self.initializeGUI()
        self.connectHandlers()
        self.tabs.show()
        sys.exit(self.app.exec_()) 
        
    def initializeGUI(self):
        self.app = QApplication(sys.argv)
        self.tabs = QTabWidget()
        # Create tabs
        self.tab1    = QWidget()    
        self.tab2    = QWidget()
        self.tab3    = QWidget()
        self.tab4    = QWidget()
        
        # Set Layout of Tab 1
        self.vBoxLayout1 = QVBoxLayout()
        self.checkBox1 = QCheckBox("Preview")
        self.checkBox2 = QCheckBox("Final screen")
        self.checkBox3 = QCheckBox("Phase 1 - Black and white")
        self.checkBox4 = QCheckBox("Phase 2 - Difference")
        self.checkBox5 = QCheckBox("Phase 3 - Binarize")
        self.checkBox6 = QCheckBox("Phase 4 - Blur")
        self.checkBox7 = QCheckBox("Phase 5 - Binarize")
        
        self.vBoxLayout1Sub = QVBoxLayout()
        self.vBoxLayout1Sub.setContentsMargins(25, 0,0,0)
        self.vBoxLayout1Sub.addWidget(self.checkBox2)
        self.vBoxLayout1Sub.addWidget(self.checkBox3)
        self.vBoxLayout1Sub.addWidget(self.checkBox4)
        self.vBoxLayout1Sub.addWidget(self.checkBox5)
        self.vBoxLayout1Sub.addWidget(self.checkBox6)
        self.vBoxLayout1Sub.addWidget(self.checkBox7)
        self.checkBox1.setChecked(False)
        
        self.vBoxLayout1.addWidget(self.checkBox1)
        self.vBoxLayout1.addLayout(self.vBoxLayout1Sub)
        self.tab1.setLayout(self.vBoxLayout1)   
        
        
        # Set Layout of Tab 2
        self.vBoxLayout2 = QVBoxLayout()
        self.checkBox8 = QCheckBox("Record video")
        self.checkBox8.setChecked(False)
        self.label1 = QLabel("Destination folder: ")
        
        self.hBoxLayout1 = QHBoxLayout()
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setText("/")
        self.pushButton1 = QPushButton("Browse")
        self.hBoxLayout1.addWidget(self.lineEdit1)
        self.hBoxLayout1.addWidget(self.pushButton1)
        
        self.pushButton1.clicked.connect(self.selectFolderDialog)
        self.checkBox9 = QCheckBox("Put timecode on video")
        
        self.hBoxLayout2 = QHBoxLayout()
        self.label2 = QLabel("Font scale: ")
        self.spinBox1 = QSpinBox()
        self.spinBox1.setValue(1)
        self.hBoxLayout2.addWidget(self.label2)
        self.hBoxLayout2.addWidget(self.spinBox1)
        
        self.buttonGroup1 = QButtonGroup()
        self.radioButton1 = QRadioButton("Record continuously")
        self.radioButton2 = QRadioButton("Record movement only")
        self.buttonGroup1.addButton(self.radioButton1)
        self.buttonGroup1.addButton(self.radioButton2)
        
        self.buttonGroup2 = QButtonGroup()
        self.radioButton3 = QRadioButton("Into a single file")
        self.radioButton4 = QRadioButton("Separate files")
        self.buttonGroup2.addButton(self.radioButton3)
        self.buttonGroup2.addButton(self.radioButton4)
        self.radioButton1.setChecked(True)
        self.radioButton3.setChecked(True)
        
        
        self.checkBox8.setContentsMargins(25, 0, 0, 0)
        self.label1.setContentsMargins(25, 0, 0, 0)
        self.hBoxLayout1.setContentsMargins(25, 0, 0, 0)
        self.hBoxLayout2.setContentsMargins(25, 0, 0, 0)
        self.vBoxLayout2.addWidget(self.checkBox8)
        self.vBoxLayout2.addWidget(self.label1)
        self.vBoxLayout2.addLayout(self.hBoxLayout1)
        self.vBoxLayout2.addWidget(self.checkBox9)
        self.vBoxLayout2.addLayout(self.hBoxLayout2)
        self.vBoxLayout2.addWidget(self.radioButton1)
        self.vBoxLayout2.addWidget(self.radioButton2)
        self.vBoxLayout2.addWidget(self.radioButton3)
        self.vBoxLayout2.addWidget(self.radioButton4)
        
        
        self.tab2.setLayout(self.vBoxLayout2)
        
        # Set Layout of Tab 3
        self.vBoxLayout3 = QVBoxLayout()
        
        self.hBoxLayout3 = QHBoxLayout()
        self.label3 = QLabel("Resolution: ")
        self.comboBox1 = QComboBox()
        self.comboBox1.addItem("432 x 368")
        self.hBoxLayout3.addWidget(self.label3)
        self.hBoxLayout3.addWidget(self.comboBox1)
        
        self.checkButton9 = QCheckBox("Aim towards motion")
        self.checkButton10 = QCheckBox("Aim with arrow keys")
        
        self.hBoxLayout4 = QHBoxLayout()
        self.label4 = QLabel("Blur value:")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setValidator(QIntValidator())
        self.lineEdit2.setText("40")
        self.hBoxLayout4.addWidget(self.label4)
        self.hBoxLayout4.addWidget(self.lineEdit2)
        
        self.hBoxLayout5 = QHBoxLayout()
        self.label5 = QLabel("Noise threshold:")
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setValidator(QIntValidator())
        self.lineEdit3.setText("20")
        self.hBoxLayout5.addWidget(self.label5)
        self.hBoxLayout5.addWidget(self.lineEdit3)
        
        self.hBoxLayout6 = QHBoxLayout()
        self.label6 = QLabel("Standby between movements (ms):")
        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setValidator(QIntValidator())
        self.lineEdit4.setText("500")
        self.hBoxLayout6.addWidget(self.label6)
        self.hBoxLayout6.addWidget(self.lineEdit4)
        
        self.hBoxLayout7 = QHBoxLayout()
        self.label7 = QLabel("Camera field of view (angle):")
        self.lineEdit5 = QLineEdit()
        self.lineEdit5.setValidator(QIntValidator())
        self.lineEdit5.setText("180")
        self.hBoxLayout7.addWidget(self.label7)
        self.hBoxLayout7.addWidget(self.lineEdit5)
        
        self.hBoxLayout8 = QHBoxLayout()
        self.label8 = QLabel("Movement trigger angular diff:")
        self.lineEdit6 = QLineEdit()
        self.lineEdit6.setValidator(QIntValidator())
        self.lineEdit6.setText("75")
        self.hBoxLayout8.addWidget(self.label8)
        self.hBoxLayout8.addWidget(self.lineEdit6)
        
        self.vBoxLayout3.addLayout(self.hBoxLayout3)
        self.vBoxLayout3.addWidget(self.checkButton9)
        self.vBoxLayout3.addWidget(self.checkButton10)
        self.vBoxLayout3.addLayout(self.hBoxLayout4)
        self.vBoxLayout3.addLayout(self.hBoxLayout5)
        self.vBoxLayout3.addLayout(self.hBoxLayout6)
        self.vBoxLayout3.addLayout(self.hBoxLayout7)
        self.vBoxLayout3.addLayout(self.hBoxLayout8)
        self.tab3.setLayout(self.vBoxLayout3)
        
        # Add start and close buttons to all tabs
        self.hBoxLayout9 = QHBoxLayout()
        self.pushButton3 = QPushButton("Start application")
        self.hBoxLayout9.setContentsMargins(0,15,0,0)
        self.hBoxLayout9.addSpacerItem(QSpacerItem(100, 0, QSizePolicy.Maximum))
        self.hBoxLayout9.addWidget(self.pushButton3)
        self.hBoxLayout9.addSpacerItem(QSpacerItem(100, 0, QSizePolicy.Maximum))
        
        self.hBoxLayout10 = QHBoxLayout()
        self.pushButton5 = QPushButton("Start application")
        self.hBoxLayout10.setContentsMargins(0,15,0,0)
        self.hBoxLayout10.addSpacerItem(QSpacerItem(100, 0, QSizePolicy.Maximum))
        self.hBoxLayout10.addWidget(self.pushButton5)
        self.hBoxLayout10.addSpacerItem(QSpacerItem(100, 0, QSizePolicy.Maximum))
        
        self.hBoxLayout11 = QHBoxLayout()
        self.pushButton7 = QPushButton("Start application")
        self.hBoxLayout11.setContentsMargins(0,15,0,0)
        self.hBoxLayout11.addSpacerItem(QSpacerItem(100, 0, QSizePolicy.Maximum))
        self.hBoxLayout11.addWidget(self.pushButton7)
        self.hBoxLayout11.addSpacerItem(QSpacerItem(100, 0, QSizePolicy.Maximum))
        
        self.vBoxLayout1.addLayout(self.hBoxLayout9)
        self.vBoxLayout2.addLayout(self.hBoxLayout10)
        self.vBoxLayout3.addLayout(self.hBoxLayout11)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Preview")
        self.tabs.addTab(self.tab2,"Recording")
        self.tabs.addTab(self.tab3,"Advanced")
        
        self.tabs.setWindowTitle('Motion Tracking')

    def startButtonClicked(self):
        self.__preview = self.checkBox1.isChecked()
        self.__finalScreen = self.checkBox2.isChecked()
        self.__phase1 = self.checkBox3.isChecked()
        self.__phase2 = self.checkBox4.isChecked()
        self.__phase3 = self.checkBox5.isChecked()
        self.__phase4 = self.checkBox6.isChecked()
        self.__phase5 = self.checkBox7.isChecked()
        self.__recordVideo = self.checkBox8.isChecked()
        self.__destinationFolder = self.lineEdit.getText()
        self.__putTimecode = self.checkBox9.isChecked()
        self.__fontScale = self.spinBox1.getValue()
        self.__recordContinously = self.radioButton1.isChecked()
        self.__recordMovement = self.radioButton2.isChecked()
        self.__intoASingleFile = self.radioButton3.isChecked()
        self.__separateFiles = self.radioButton4.isChecked()
        self.__resolution = self.comboBox1.currentText()
        self.__aimTowardsMotion = self.checkButton9.isChecked()
        self.__aimWithArrowKeys = self.checkButton10.isChecked()
        self.__blur = self.lineEdit2.getText()
        self.__threshold = self.lineEdit3.getText()
        self.__standbyBetweenMovements = self.lineEdit4.getText()
        self.__cameraFieldOfView = self.lineEdit5.getText()
        self.__minTrigger = self.lineEdit6.getText()
        print(        "preview): " + (str)(self.__preview))
        print(        "finalScreen): " + (str)(self.__finalScreen))
        print(        "phase1): " + (str)(self.__phase1))
        print(        "phase2): " + (str)(self.__phase2))
        print(        "phase3): " + (str)(self.__phase3))
        print(        "phase4): " + (str)(self.__phase4))
        print(        "phase5): " + (str)(self.__phase5))
        print(        "recordVideo): " + (str)(self.__recordVideo))
        print(        "destinationFolder): " + (str)(self.__destinationFolder))
        print(        "putTimecode): " + (str)(self.__putTimecode))
        print(        "fontScale): " + (str)(self.__fontScale))
        print(        "recordContinously): " + (str)(self.__recordContinously))
        print(        "recordMovement): " + (str)(self.__recordMovement))
        print(        "intoASingleFile): " + (str)(self.__intoASingleFile))
        print(        "separateFiles): " + (str)(self.__separateFiles))
        print(        "resolution): " + (str)(self.__resolution))
        print(        "aimTowardsMotion): " + (str)(self.__aimTowardsMotion))
        print(        "aimWithArrowKeys): " + (str)(self.__aimWithArrowKeys))
        print(        "blur): " + (str)(self.__blur))
        print(        "threshold): " + (str)(self.__threshold))
        print(        "standbyBetweenMovements): " + (str)(self.__standbyBetweenMovements))
        print(        "cameraFieldOfView): " + (str)(self.__cameraFieldOfView))
        print(        "minTrigger): " + (str)(self.__minTrigger))
        
    
    def togglePreviewEnabled(self):
        newState = self.checkBox1.isChecked()
        self.checkBox2.setEnabled(newState)
        self.checkBox3.setEnabled(newState)
        self.checkBox4.setEnabled(newState)
        self.checkBox5.setEnabled(newState)
        self.checkBox6.setEnabled(newState)
        self.checkBox7.setEnabled(newState)
    
    def toggleSeparateFilesEnabled(self):
        newState = self.radioButton2.isChecked()
        self.radioButton3.setEnabled(newState)
        self.radioButton4.setEnabled(newState)
        
    def toggleRecordEnabled(self):
        newState = self.checkBox8.isChecked()
        self.label1.setEnabled(newState)
        self.label2.setEnabled(newState)
        self.lineEdit1.setEnabled(newState)
        self.pushButton1.setEnabled(newState)
        self.spinBox1.setEnabled(newState)
        self.radioButton1.setEnabled(newState)
        self.radioButton2.setEnabled(newState)
        self.radioButton3.setEnabled(newState)
        self.radioButton4.setEnabled(newState)
        self.toggleSeparateFilesEnabled()

    def toggleTimecodeEnabled(self):
        newState = self.checkBox9.isChecked()
        self.spinBox1.setEnabled(newState)

    def connectHandlers(self):
        self.checkBox1.clicked.connect(self.togglePreviewEnabled)
        self.checkBox8.clicked.connect(self.toggleRecordEnabled)
        self.radioButton1.clicked.connect(self.toggleSeparateFilesEnabled)
        self.radioButton2.clicked.connect(self.toggleSeparateFilesEnabled)
        self.checkBox9.clicked.connect(self.toggleTimecodeEnabled())
        self.togglePreviewEnabled()1
        self.toggleRecordEnabled()
        self.toggleSeparateFilesEnabled()
        self.toggleTimecodeEnabled()

    def selectFolderDialog(self):
        filename = QFileDialog.getExistingDirectory(self.tab2, "Select directory")
        self.lineEdit1.setText(filename)
    
    def runApp(self):
        '''
        WIDTH = 432
        HEIGHT = 368
        FRAMERATE = 20
        ROTATION = 180
        camFeed = CameraFeed(WIDTH, HEIGHT, ROTATION, FRAMERATE)
        #print(self.__destinationFolder[7:])
        mt = MotionTracking(camFeed, self.__destinationFolder)
        t = time.time()
        while True:
            image = mt.getFinal()
            if image is not None:
                #cv2.imshow("asd", image)
                fps = 1/(time.time() - t)
                print("fps: " + str(int(fps)))
                t = time.time()
    '''


