import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class CarDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Car UI')
        self.showFullScreen()  # Go fullscreen

        # Top label
        self.trackLabel = QLabel("Now Playing: Track Title")
        self.trackLabel.setStyleSheet("font-size: 24px; color: white;")
        self.trackLabel.setAlignment(Qt.AlignCenter)

        # GPS Label (placeholder)
        self.gpsLabel = QLabel("GPS: Lat 0.000, Lon 0.000")
        self.gpsLabel.setStyleSheet("font-size: 18px; color: gray;")
        self.gpsLabel.setAlignment(Qt.AlignCenter)

        # Buttons
        playButton = QPushButton("Play")
        nextButton = QPushButton("Next")
        mapButton = QPushButton("Map")

        for btn in [playButton, nextButton, mapButton]:
            btn.setFixedHeight(80)
            btn.setStyleSheet("font-size: 20px;")

        playButton.clicked.connect(self.playMusic)
        nextButton.clicked.connect(self.nextTrack)
        mapButton.clicked.connect(self.launchMap)

        # Layouts
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(playButton)
        buttonLayout.addWidget(nextButton)
        buttonLayout.addWidget(mapButton)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.trackLabel)
        mainLayout.addWidget(self.gpsLabel)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setStyleSheet("background-color: black;")  # Touch UI style

    def playMusic(self):
        print("Play button pressed")

    def nextTrack(self):
        print("Next track")

    def launchMap(self):
        print("Launch map...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = CarDashboard()
    sys.exit(app.exec_())
