# Lab 01. PySide 6 실습 : 응용 프로그램 만들어보기

import sys
import cv2
import os
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QFileDialog, QLabel, QApplication, QSizePolicy, QWidget, QStatusBar
from PySide6 import QtGui

class VideoViewer(QMainWindow) :
    def __init__(self):
        super().__init__()

        self.setWindowTitle("vieo viewer")
        self.resize(800,600)

        self.video_file_button = QPushButton("file open")
        self.video_file_button.clicked.connect(self.open_video_file_dialog)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_video)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_video)

        self.capture_button = QPushButton("capture")
        self.capture_button.clicked.connect(self.capture_frame)

        self.video_view_label = QLabel()
        self.video_view_label.setAlignment(Qt.AlignCenter)
        self.video_view_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.video_file_button)
        main_layout.addWidget(self.play_button)
        main_layout.addWidget(self.stop_button)
        main_layout.addWidget(self.capture_button)
        main_layout.addWidget(self.video_view_label)

        centerl_widget = QWidget()
        centerl_widget.setLayout(main_layout)
        self.setCentralWidget(centerl_widget)

        self.video_path = ""
        self.video_width = 720
        self.video_height = 640

        self.video_capture = None
        self.video_timer = QTimer()
        self.video_timer.timeout.connect(self.display_next_frame)

        self.paused = False
        self.current_frame = 0
        self.capture_count = 0

        os.makedirs("./data", exist_ok=True)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def open_video_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mov *.mkv)")
        if file_dialog.exec() :
            selected_files = file_dialog.selectedFiles()
            if selected_files :
                self.video_path = selected_files[0]
                self.status_bar.showMessage(f"video path >> {self.video_path}")

    def play_video(self):
        if self.video_path :
            if self.paused :
                self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
                self.paused = False
            else :
                self.video_capture = cv2.VideoCapture(self.video_path)
                self.current_frame = 0

            self.play_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.capture_button.setEnabled(True)
            self.video_timer.start(30)

    def display_next_frame(self):
        if self.video_path :
            ret, frame = self.video_capture.read()

            if ret :
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_resize = self.resize_frame(frame_rgb)
                h, w, _ = frame_resize.shape # fix -> frame_resize.shape
                if w > 0 and h > 0 :
                    frame_image = QtGui.QImage(frame_resize, w, h, QtGui.QImage.Format_RGB888)
                    pixmap = QtGui.QPixmap.fromImage(frame_image)
                    self.video_view_label.setPixmap(pixmap)
                    self.video_view_label.setScaledContents(True)

                self.current_frame += 1
            else :
                self.video_timer.stop()

    def stop_video(self) :
        self.video_timer.stop()
        self.play_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.capture_button.setEnabled(not self.paused)
        self.paused = True

    def capture_frame(self):
        ret, frame = self.video_capture.read()

        if ret :
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resize = self.resize_frame(frame_rgb)
            h, w, _ = frame_resize.shape  # fix -> frame_resize.shape
            if w > 0 and h > 0:
                file_name = os.path.splitext(os.path.basename(self.video_path))[0]
                image_name = f"{file_name}_{self.capture_count:04d}_image.png"
                image_save_path = os.path.join("./data/", image_name)
                cv2.imwrite(image_save_path, frame_resize)
                self.capture_count += 1
                self.status_bar.showMessage(f"capture ok : {image_save_path}")

    def resize_frame(self, frame):
        height, width, _ = frame.shape

        if width > self.video_width :
            ratio = self.video_width / width
            frame = cv2.resize(frame, (self.video_width, int(height * ratio)))
        if height > self.video_height :
            ratio = self.video_height / height
            frame = cv2.resize(frame, (int(width * ratio), self.video_height))

        return frame

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = VideoViewer()
    window.show()
    app.exec()