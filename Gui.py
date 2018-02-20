import cv2
from PyQt5 import QtGui, QtCore, QtWidgets
import Configuration
from PyQt5.QtCore import QSettings
import CameraParam


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

    def SetValueToCam(self,value, cam_property):
        if cam_property == 'Brightness':
            self.c.set(cv2.CAP_PROP_BRIGHTNESS, value)
        if cam_property == 'Contrast':
            self.c.set(cv2.CAP_PROP_CONTRAST, value)
        if cam_property == 'Exposure':
            self.c.set(cv2.CAP_PROP_EXPOSURE, value)
        if cam_property == 'Saturation':
            self.c.set(cv2.CAP_PROP_SATURATION, value)
        if cam_property == 'Gain':
            self.c.set(cv2.CAP_PROP_GAIN, value)
        if cam_property == 'FPS':
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
            cv2.waitKey(2)
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
        Configuration.SaveConfig(CameraParameters)
        
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
        self.label_exposure = QtWidgets.QLabel()
        self.label_saturation = QtWidgets.QLabel()
        self.label_gain = QtWidgets.QLabel()
        self.label_fps = QtWidgets.QLabel()
        
        #Slider Brightness
        self.slider_brightness = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_brightness.setMinimum(0)
        self.slider_brightness.setMaximum(100)
        self.slider_brightness.setTickInterval(5)
        self.slider_brightness.setValue(int(CameraParameters['Brightness']))
        self.AssignNewSliderValue(self, 'Brightness')
        self.slider_brightness.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_brightness.valueChanged.connect(lambda: self.AssignNewSliderValue(self.slider_brightness, 'Brightness'))
        
        #Slider constrast
        self.slider_contrast = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_contrast.setMinimum(0)
        self.slider_contrast.setMaximum(100)
        self.slider_contrast.setTickInterval(5)
        self.slider_contrast.setValue(int(CameraParameters['Contrast']))
        self.AssignNewSliderValue(self, 'Contrast')
        self.slider_contrast.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_contrast.valueChanged.connect(lambda: self.AssignNewSliderValue(self.slider_contrast, 'Contrast'))
        
        #Slider exposure
        self.slider_exposure = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_exposure.setMinimum(0)
        self.slider_exposure.setMaximum(100)
        self.slider_exposure.setTickInterval(5)
        self.slider_exposure.setValue(int(CameraParameters['Exposure']))
        self.AssignNewSliderValue(self, 'Exposure')
        self.slider_exposure.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_exposure.valueChanged.connect(lambda: self.AssignNewSliderValue(self.slider_exposure, 'Exposure'))
        
        #Slider saturation
        self.slider_saturation = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_saturation.setMinimum(0)
        self.slider_saturation.setMaximum(100)
        self.slider_saturation.setTickInterval(5)
        self.slider_saturation.setValue(int(CameraParameters['Saturation']))
        self.AssignNewSliderValue(self, 'Saturation')
        self.slider_saturation.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_saturation.valueChanged.connect(lambda: self.AssignNewSliderValue(self.slider_saturation, 'Saturation'))
        
        #Slider gain
        self.slider_gain = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_gain.setMinimum(0)
        self.slider_gain.setMaximum(100)
        self.slider_gain.setTickInterval(5)
        self.slider_gain.setValue(int(CameraParameters['Gain']))
        self.AssignNewSliderValue(self, 'Gain')
        self.slider_gain.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_gain.valueChanged.connect(lambda: self.AssignNewSliderValue(self.slider_gain, 'Gain'))
        
        #Slider fps
        self.slider_fps = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_fps.setMinimum(1)
        self.slider_fps.setMaximum(30)
        self.slider_fps.setTickInterval(1)
        self.slider_fps.setValue(int(CameraParameters['FPS']))
        self.AssignNewSliderValue(self, 'FPS')
        self.slider_fps.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_fps.valueChanged.connect(lambda: self.AssignNewSliderValue(self.slider_fps, 'FPS'))
 
        #Vertical Box
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.camera_button)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)
        vbox.addWidget(self.label_brightness)
        vbox.addWidget(self.slider_brightness)
        vbox.addWidget(self.label_constrast)
        vbox.addWidget(self.slider_contrast)
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
        
    def AssignNewSliderValue(self, obj, string):
        self.capture.SetValueToCam(int(self.slider_brightness.value())/100, 'Brightness')
        CameraParameters['Brightness'] = self.slider_brightness.value() # Update Value in Dictionary
        if string == 'Brightness':
            self.capture.SetValueToCam(self.slider_brightness.value()/100, 'Brightness')
            self.label_brightness.setText('Brightness = '+ str(self.slider_brightness.value()/100))
        if string == 'Contrast':
            self.capture.SetValueToCam(self.slider_contrast.value()/100, 'Contrast')
            self.label_constrast.setText('Constrast = '+ str(self.slider_contrast.value()/100))
        if string == 'Exposure':
            self.capture.SetValueToCam(self.slider_exposure.value()/100, 'Exposure')
            self.label_exposure.setText('Exposure = '+ str(self.slider_exposure.value()))
        if string == 'Saturation':
            self.capture.SetValueToCam(self.slider_saturation.value()/100, 'Saturation')
            self.label_saturation.setText('Saturation = '+ str(self.slider_saturation.value()/100))
        if string == 'Gain':
            self.capture.SetValueToCam(self.slider_gain.value()/100, 'Gain')
            self.label_gain.setText('Gain = '+ str(self.slider_gain.value()/100))
        if string == 'FPS':
            self.capture.SetValueToCam(self.slider_fps.value()/100, 'FPS')
            self.label_fps.setText('FPS = '+ str(self.slider_fps.value()))
            
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    settings = QSettings('foo')
    print(settings.value('int_value', type=int))

    print("2")
    #Get Camera Settings from Config file
    CameraParameters = Configuration.ReadConfig()

    
    window = Window()
    #cv2.destroyAllWindows()
    sys.exit(app.exec_())