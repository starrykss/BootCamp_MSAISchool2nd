# Lab 02. PySide 6 실습 : DB 연동하여 로그인 / 회원 가입 / 관리자 페이지 기능이 있는 응용 프로그램 만들기 

import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QListWidget
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# DB setting
os.makedirs("db", exist_ok=True)
# engine = create_engine("sqlite:///userinfo.db", echo=True)
engine = create_engine('sqlite:///db/user.db', echo=True)
# engine = create_engine("sqlite:///path/to/folder/user.db", echo=True)

Base = declarative_base()

# user model
class User(Base) :
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)   # pk
    username = Column(String, unique=True)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

#  sessionmaker
Session = sessionmaker(bind=engine)
seesion = Session()

# Base.metadata.create_all(engine) # crate -> DB
# registerPage
class RegisterPage(QWidget) :
    def __init__(self, stacked_widget, main_window):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.username_label = QLabel("UserName : ")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password : ")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.register_button)
        self.setLayout(self.layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password :
            QMessageBox.warning(self, "Error", "Plese enter username and password.")

        # user create
        user = User(username, password)

        # DB input
        seesion.add(user)
        seesion.commit()

        QMessageBox.information(self, "Success", "Registration successful")
        self.main_window.show_login_page()

# Login Page
class LoginPage(QWidget):
    def __init__(self, stacked_widget, main_window):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.main_window = main_window

        self.username_label = QLabel("Username : ")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password : ")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)

        # layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        user = seesion.query(User).filter_by(username=username, password=password).first()
        if user :
            QMessageBox.information(self, "Success", "Login successful")
            self.main_window.show_admin_page()
        else :
            QMessageBox.warning(self, "Error" , "Invalid username or password")

    def register(self):
        self.main_window.show_register_page()

# AdminPage
class AdminPage(QWidget) :
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        self.user_list = QListWidget()

        self.show_user_list_button = QPushButton("Show User List")
        self.show_user_list_button.clicked.connect(self.show_user_list)

        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.show_user_list_button)
        self.layout.addWidget(self.user_list)
        self.layout.addWidget(self.logout_button)

        self.setLayout(self.layout)

    def show_user_list(self):
        self.user_list.clear()

        # all user
        users = seesion.query(User).all()

        for user in users :
            self.user_list.addItem(user.username)

    def logout(self):
        self.main_window.show_login_page()

# Main
class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.register_page = RegisterPage(self.stacked_widget, self)
        self.login_page = LoginPage(self.stacked_widget, self)
        self.admin_page = AdminPage(self)

        # login page setting
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.register_page)
        self.stacked_widget.addWidget(self.admin_page)

        self.show_login_page() # 1. page

    def show_login_page(self):
        self.stacked_widget.setCurrentIndex(0)
        self.login_page.username_input.clear()
        self.login_page.password_input.clear()

    def show_register_page(self):
        self.stacked_widget.setCurrentIndex(1)
        self.register_page.username_input.clear()
        self.register_page.password_input.clear()

    def show_admin_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def show_register_success_message(self):
        QMessageBox.information(self, "Success" , "Registration success")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    Base.metadata.create_all(engine)

    window = MainWindow()
    window.show()

    app.exec()