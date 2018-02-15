import cv2
from PyQt5 import QtGui, QtCore, QtWidgets


class Capture():
    def __init__(self):
        self.capturing = False
        self.recording = False
        self.c = cv2.VideoCapture(0)
        
        #Get Camera Settings
        print("-----Camera Settings------")
        self.w = int(self.c.get(cv2.CAP_PROP_FRAME_WIDTH ))
        print ("Width = ", self.w)
        self.h = int(self.c.get(cv2.CAP_PROP_FRAME_HEIGHT ))
        print ("Height = ", self.h)
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
        
        
        #Set Default Values
        self.c.set(cv2.CAP_PROP_BRIGHTNESS, 50)
        
        #Define Video Writer
        self.video_writer = cv2.VideoWriter("Video.avi", cv2.VideoWriter_fourcc(*'XVID'), 10, (self.w, self.h))

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
        
        self.s1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.s1.setMinimum(0)
        self.s1.setMaximum(100)
        self.s1.setValue(50)
        self.s1.setTickInterval(5)
        self.s1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.s1.valueChanged.connect(self.v_change)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.camera_button)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)
        vbox.addWidget(self.l1)
        vbox.addWidget(self.s1)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()
        
    def v_change(self):
        #print(int(self.s1.value()))
        self.capture.SetBrightness(int(self.s1.value())/100)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())