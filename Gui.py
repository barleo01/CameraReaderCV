import cv2
from PyQt5 import QtGui, QtCore, QtWidgets


class Capture():
    def __init__(self):
        self.recording = False
        self.c = cv2.VideoCapture(0)
        self.w = int(self.c.get(cv2.CAP_PROP_FRAME_WIDTH ))
        #print ("Width = ", self.w)
        self.h = int(self.c.get(cv2.CAP_PROP_FRAME_HEIGHT ))
       # print ("Height = ", self.h)
        #Define Video Writer
        self.video_writer = cv2.VideoWriter("Video.avi", cv2.VideoWriter_fourcc(*'XVID'), 10, (self.w, self.h))
        self.Config()
        
    def Config(self):
        #Get Camera Settings
        print("-----Camera Settings------")

        self.brightness = float(self.c.get(cv2.CAP_PROP_BRIGHTNESS))
        print("Brightness = " ,self.brightness)
        self.brightness = int(self.c.get(cv2.CAP_PROP_FPS))
        print("FPS = " ,self.brightness)
        self.exposure = float(self.c.get(cv2.CAP_PROP_EXPOSURE))
        print("Exposure = " ,self.exposure)
        self.contrast = int(self.c.get(cv2.CAP_PROP_CONTRAST))
        print("Contrast = " ,self.contrast)
        self.saturation = int(self.c.get(cv2.CAP_PROP_SATURATION))
        print("Saturation = " ,self.saturation)
        self.gain = int(self.c.get(cv2.CAP_PROP_GAIN))
        print("Gain = " ,self.gain)
        
        print(self.c.get(cv2.CAP_PROP_AUTO_EXPOSURE))
        self.c.set(cv2.CAP_PROP_BRIGHTNESS, 10)
        '''
        self.sharpness = int(self.c.get(cv2.CAP_PROP_SHARPNESS))
        print("Sharpnesss = " ,self.sharpness)
        self.gamma = int(self.c.get(cv2.CAP_PROP_GAMMA))
        print("Gamma = " ,self.gamma)
        self.whitebalanceblue = int(self.c.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U))
        print("White Balance Blue = " ,self.whitebalanceblue)
        self.whitebalancered = int(self.c.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V))
        print("White Balance Red = " ,self.whitebalancered)
        '''
        print("---------------------------")
        
        #Set Camera Default Values
        #self.c.set(cv2.CAP_PROP_BRIGHTNESS, 50)

    def SetBrightness(self,value):
        self.c.set(cv2.CAP_PROP_BRIGHTNESS, value)
        
    def SetConstrast(self,value):
        self.c.set(cv2.CAP_PROP_CONTRAST, value)

    def startCamera(self):
        print ("Start Camera")
        self.capturing = True
        cap = self.c
        while(self.capturing):
            ret, frame = cap.read()
            if (self.recording):
                self.video_writer.write(frame)
            cv2.imshow("Capture", frame)
            cv2.waitKey(1)
        cv2.destroyAllWindows()
        
    def startRecording(self):
        print("Start Recording")
        self.capturing = True
        self.recording = True

    def endRecording(self):
        print ("End Recording")
        self.capturing = True
        self.recording = False
        self.video_writer.release()

    def quitApp(self):
        print ("Quit")
        self.capturing = False
        cap = self.c
        self.video_writer.release()
        cv2.destroyAllWindows()
        cap.release()
        QtCore.QCoreApplication.quit()


class Window(QtWidgets.QWidget):
    
    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Control Panel')

        self.capture = Capture()
        self.camera_button = QtWidgets.QPushButton('Start Camera',self)
        self.camera_button.clicked.connect(self.capture.startCamera)

        self.start_button = QtWidgets.QPushButton('Start Record',self)
        self.start_button.clicked.connect(self.capture.startRecording)

        self.end_button = QtWidgets.QPushButton('Stop Record',self)
        self.end_button.clicked.connect(self.capture.endRecording)

        self.quit_button = QtWidgets.QPushButton('Quit',self)
        self.quit_button.clicked.connect(self.capture.quitApp)
        
        #Labels
        self.label_brightness = QtWidgets.QLabel()
        self.label_constrast = QtWidgets.QLabel()
        
        #Slider Brightness
        self.slider_brightness = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_brightness.setMinimum(0)
        self.slider_brightness.setMaximum(100)
        self.slider_brightness.setValue(60)
        self.slider_brightness.setTickInterval(5)
        self.assign_brightness_value()
        self.slider_brightness.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_brightness.valueChanged.connect(self.assign_brightness_value)
        
        #Slider constrast
        self.slider_constrast = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_constrast.setMinimum(0)
        self.slider_constrast.setMaximum(100)
        self.slider_constrast.setValue(60)
        self.slider_constrast.setTickInterval(5)
        self.assign_constrast_value()
        self.slider_constrast.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_constrast.valueChanged.connect(self.assign_constrast_value)
        
        #Vertical Box
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.camera_button)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)
        vbox.addWidget(self.label_brightness)
        vbox.addWidget(self.slider_brightness)
        vbox.addWidget(self.label_constrast)
        vbox.addWidget(self.slider_constrast)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()
        
    def assign_brightness_value(self):
        #print(int(self.slider_brightness.value()))
        self.capture.SetBrightness(int(self.slider_brightness.value())/100)
        self.label_brightness.setText('Brightness = '+ str(self.slider_brightness.value()/100))

    def assign_constrast_value(self):
        #print(int(self.slider_brightness.value()))
        self.capture.SetConstrast(int(self.slider_constrast.value())/100)
        self.label_constrast.setText('Constrast = '+ str(self.slider_constrast.value()/100))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    #cv2.destroyAllWindows()
    sys.exit(app.exec_())