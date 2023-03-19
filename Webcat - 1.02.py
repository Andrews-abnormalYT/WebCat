# Import necessary libraries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
import sys
import wget
import random



# Create a main window class
class MainWindow(QMainWindow):
    # Constructor of this class
    def __init__(self):
        super(MainWindow, self).__init__()
        # To provide a widget for viewing and editing web documents:
        self.browser = QWebEngineView()
        # To set default browser homepage as google homepage:
        self.browser.setUrl(QUrl("http://CatWeb.rf.gd"))
        # To set browser as central widget of main window:
        self.setCentralWidget(self.browser)
        # To open browser in a maximized window:
        self.showMaximized()
        
        self.setWindowIcon(QIcon('Untitled.png'))
        # To create a navigation bar:
        navbar = QToolBar()
        navbar.adjustSize()
        # To add the navigation bar to the browser:
        self.addToolBar(navbar)

        # To add back button within navigation bar:
        back_btn = QAction('⮜', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # To add forward button within navigation bar:
        forward_btn = QAction('⮞', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # To add reload button within navigation bar:
        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # To add Homepage button
        homepage_btn = QAction('⌂', self)
        homepage_btn.triggered.connect(self.go_to_home)
        navbar.addAction(homepage_btn)
        # To add URL bar within navigation bar:
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.open_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

        self.addToolBarBreak()
        # Adding another toolbar which contains the bookmarks
        bookmarks_toolbar = QToolBar('Bookmarks', self)
        self.addToolBar(bookmarks_toolbar)
        pythongeeks = QAction("Google", self)
        pythongeeks.setStatusTip("Go to google website")
        pythongeeks.triggered.connect(lambda: self.browser.setUrl(QUrl("https://google.com")))
        bookmarks_toolbar.addAction(pythongeeks)
        facebook = QAction("Bing", self)
        facebook.setStatusTip("Go to Bing")
        facebook.triggered.connect(lambda: self.browser.setUrl(QUrl("https://www.bing.com")))
        bookmarks_toolbar.addAction(facebook)
        linkedin = QAction("Facebook", self)
        linkedin.setStatusTip("Go to FaceBook")
        linkedin.triggered.connect(lambda: self.browser.setUrl(QUrl("https://facebook.com")))
        bookmarks_toolbar.addAction(linkedin)
        instagram = QAction("Instagram", self)
        instagram.setStatusTip("Go to Instagram")
        instagram.triggered.connect(lambda: self.browser.setUrl(QUrl("https://www.instagram.com")))
        bookmarks_toolbar.addAction(instagram)
        twitter = QAction("YouTube", self)
        twitter.setStatusTip('Go to YouTube')
        twitter.triggered.connect(lambda: self.browser.setUrl(QUrl("https://youtube.com")))
        bookmarks_toolbar.addAction(twitter)
        self.show()



    def listToString(self, s):
 
        # initialize an empty string
        str1 = ""
 
        # traverse in the string
        for ele in s:
            str1 += ele
 
        # return string
        return str1    
    def go_to_home(self,):
        self.browser.setUrl(QUrl("http://CatWeb.rf.gd"))
    def open_url(self):
        url = self.url_bar.text()
        if "wget:" in url:
            url2 = url.split(':')
            s = url2[2]
            
            final = self.listToString(s)
            try:
                wget.download("https://" + final)
                print("WebCat Window: Webpage Download successful")
            except Exception as e:
                print("Cannot download: " + str(e))
        elif "." not in url:
            self.browser.setUrl(QUrl("https://www.google.com/search?PC=U523&q=" + url + "&pglt=43&FORM=ANNTA1&adlt=strict&toWww=1&redig=4097D7EF3E3F461785884D4DCA9B8564"))
            print("WebCat Window: Webpage successful")
            return
        elif "http://" not in url:
            url = self.url_bar.text()
            self.browser.setUrl(QUrl("http://" + url))
            print("WebCat Window: Webpage successful")
            return
        else:   
            url = self.url_bar.text()
            self.browser.setUrl(QUrl(url))
            print("WebCat Window: Webpage successful")
    # To update the URL bar contents when navigated from one page to another:
    def update_url(self, q):
        self.url_bar.setText(q.toString())
# To call constructor of the C++ class QApplication:
# Here, sys.argv is used to initialize the QT application
app = QApplication(sys.argv)
# To specify name of the browser:
QApplication.setApplicationName("WebCat Version 1.02")
# To create an object of MainWindow class defined above:
window = MainWindow()
print("WebCat Window: Successful")
# To run the main event loop and wait until exit() is called:
app.exec()
