import cv2
from PyQt5 import QtGui, QtCore, QtWidgets


class Capture():
    def __init__(self):
        self.recording = False
        self.c = cv2.VideoCapture(1)
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

    def startCamera(self):
        print ("Start Camera")
        self.capturing = True
        cap = self.c
        while(self.capturing):
            ret, frame = cap.read()
            if (self.recording):
                self.video_writer.write(frame)
            cv2.imshow("Capture", frame)
            cv2.waitKey(5)
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
        
        self.l1 = QtWidgets.QLabel('Brightness = ')
        
        #Slider Brightness
        self.slider_brightness = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_brightness.setMinimum(0)
        self.slider_brightness.setMaximum(100)
        self.slider_brightness.setValue(60)
        self.capture.SetBrightness(self.slider_brightness.value()/100) # set value
        self.slider_brightness.setTickInterval(5)
        self.slider_brightness.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_brightness.valueChanged.connect(self.v_change)
        
        #Slider Exposure
        
        #Slider Exposure

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.camera_button)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)
        vbox.addWidget(self.l1)
        vbox.addWidget(self.slider_brightness)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()
        
    def v_change(self):
        #print(int(self.slider_brightness.value()))
        self.capture.SetBrightness(int(self.slider_brightness.value())/100)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())