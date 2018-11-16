from _06_view import Ui_Dialog 
from _06_model import Model
from PyQt5 import QtWidgets
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    model = Model()
    url = "https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181114"
    model.excute(url)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
