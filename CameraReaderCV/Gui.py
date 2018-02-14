import cv2
from PyQt5 import QtGui, QtCore, QtWidgets


class Capture():
    def __init__(self):
        self.capturing = False
        self.recording = False
        self.c = cv2.VideoCapture(0)
        
        self.w=int(self.c.get(cv2.CAP_PROP_FRAME_WIDTH ))
        self.h=int(self.c.get(cv2.CAP_PROP_FRAME_HEIGHT ))
        self.video_writer = cv2.VideoWriter("Video.avi", cv2.VideoWriter_fourcc(*'XVID'), 10, (self.w, self.h))

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

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.camera_button)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())