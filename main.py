import sys
from ui import View
from ctrl import Control
from PyQt5.QtWidgets import QApplication

def main():
    calc = QApplication(sys.argv)
    app= QApplication(sys.argv)
    view=View()              # ui.py에서 가져옴
    Control(view=view)       # ctrl.py에서 가져``
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
