import PokerDicesGUI
import sys
from PyQt5 import QtWidgets


if __name__ == "__main__":
    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PokerDicesGUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    """

    app = QtWidgets.QApplication(sys.argv)
    gui = PokerDicesGUI.PokerDicesGUI()
    sys.exit(app.exec_())




    


