import cv2
from PyQt5 import QtGui, QtCore, QtWidgets


class Capture():
    def __init__(self):
        self.recording = False
        self.c = cv2.VideoCapture(0)
        self.w = int(self.c.get(cv2.CAP_PROP_FRAME_WIDTH ))
        print ("Width = ", self.w)
        self.h = int(self.c.get(cv2.CAP_PROP_FRAME_HEIGHT ))
        print ("Height = ", self.h)
        
        #Define Video Writer
        self.video_writer = cv2.VideoWriter("Video.avi", cv2.VideoWriter_fourcc(*'XVID'), 30, (self.w, self.h))
        


    def SetBrightness(self,value):
        self.c.set(cv2.CAP_PROP_BRIGHTNESS, value)
        
    def SetConstrast(self,value):
        self.c.set(cv2.CAP_PROP_CONTRAST, value)
    
    def SetExposure(self,value):
        self.c.set(cv2.CAP_PROP_EXPOSURE, value)
        
    def SetSaturation(self,value):
        self.c.set(cv2.CAP_PROP_SATURATION, value)
        
    def SetGain(self,value):
        self.c.set(cv2.CAP_PROP_GAIN, value)
        
    def SetFPS(self,value):
        self.c.set(cv2.CAP_PROP_FPS, value)
        

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
        
        #Get Camera Settings
        print("-----Camera default Settings------")
        print('Brightness = ' + str(self.capture.c.get(cv2.CAP_PROP_BRIGHTNESS)))
        print('Contrast = ' + str(self.capture.c.get(cv2.CAP_PROP_BRIGHTNESS)))
        print('Exposure = ' + str(self.capture.c.get(cv2.CAP_PROP_BRIGHTNESS)))
        print('Saturation = ' + str(self.capture.c.get(cv2.CAP_PROP_BRIGHTNESS)))
        print('Gain = ' + str(self.capture.c.get(cv2.CAP_PROP_BRIGHTNESS)))
        print('FPS = ' + str(self.capture.c.get(cv2.CAP_PROP_BRIGHTNESS)))
        
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
        self.label_exposure = QtWidgets.QLabel()
        self.label_saturation = QtWidgets.QLabel()
        self.label_gain = QtWidgets.QLabel()
        self.label_fps = QtWidgets.QLabel()
        
        #Slider Brightness
        self.slider_brightness = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_brightness.setMinimum(0)
        self.slider_brightness.setMaximum(100)
        self.slider_brightness.setTickInterval(5)
        self.slider_brightness.setValue(self.capture.c.get(cv2.CAP_PROP_BRIGHTNESS))
        self.assign_brightness_value()
        self.slider_brightness.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_brightness.valueChanged.connect(self.assign_brightness_value)
        
        #Slider constrast
        self.slider_constrast = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_constrast.setMinimum(0)
        self.slider_constrast.setMaximum(100)
        self.slider_constrast.setTickInterval(5)
        self.slider_constrast.setValue(self.capture.c.get(cv2.CAP_PROP_CONTRAST))
        self.assign_constrast_value()
        self.slider_constrast.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_constrast.valueChanged.connect(self.assign_constrast_value)
        
        #Slider exposure
        self.slider_exposure = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_exposure.setMinimum(0)
        self.slider_exposure.setMaximum(100)
        self.slider_exposure.setTickInterval(5)
        self.slider_exposure.setValue(self.capture.c.get(cv2.CAP_PROP_EXPOSURE))
        self.assign_exposure_value()
        self.slider_exposure.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_exposure.valueChanged.connect(self.assign_exposure_value)
        
        #Slider saturation
        self.slider_saturation = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_saturation.setMinimum(0)
        self.slider_saturation.setMaximum(100)
        self.slider_saturation.setTickInterval(5)
        self.slider_saturation.setValue(self.capture.c.get(cv2.CAP_PROP_SATURATION))
        self.assign_saturation_value()
        self.slider_saturation.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_saturation.valueChanged.connect(self.assign_saturation_value)
        
        #Slider gain
        self.slider_gain = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_gain.setMinimum(0)
        self.slider_gain.setMaximum(100)
        self.slider_gain.setTickInterval(5)
        self.slider_gain.setValue(self.capture.c.get(cv2.CAP_PROP_GAIN))
        self.assign_gain_value()
        self.slider_gain.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_gain.valueChanged.connect(self.assign_gain_value)
        
        #Slider fps
        self.slider_fps = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_fps.setMinimum(1)
        self.slider_fps.setMaximum(30)
        self.slider_fps.setTickInterval(1)
        self.slider_fps.setValue(self.capture.c.get(cv2.CAP_PROP_FPS))
        self.assign_fps_value()
        self.slider_fps.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_fps.valueChanged.connect(self.assign_fps_value)
        
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
        vbox.addWidget(self.label_exposure)
        vbox.addWidget(self.slider_exposure)
        vbox.addWidget(self.label_saturation)
        vbox.addWidget(self.slider_saturation)
        vbox.addWidget(self.label_gain)
        vbox.addWidget(self.slider_gain)
        vbox.addWidget(self.label_fps)
        vbox.addWidget(self.slider_fps)

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
    
    def assign_exposure_value(self):
        #print(int(self.slider_brightness.value()))
        self.capture.SetExposure(int(self.slider_exposure.value()))
        self.label_exposure.setText('Exposure = '+ str(self.slider_exposure.value()))
    
    def assign_saturation_value(self):
        #print(int(self.slider_brightness.value()))
        self.capture.SetSaturation(int(self.slider_saturation.value())/100)
        self.label_saturation.setText('Saturation = '+ str(self.slider_saturation.value()/100))
    
    def assign_gain_value(self):
        #print(int(self.slider_brightness.value()))
        self.capture.SetGain(int(self.slider_gain.value())/100)
        self.label_gain.setText('Gain = '+ str(self.slider_gain.value()/100))
        
    def assign_fps_value(self):
        #print(int(self.slider_brightness.value()))
        self.capture.SetFPS(int(self.slider_fps.value()))
        self.label_fps.setText('FPS = '+ str(self.slider_fps.value()))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    #cv2.destroyAllWindows()
    sys.exit(app.exec_())