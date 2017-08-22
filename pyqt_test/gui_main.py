import sys

from PyQt5.QtWidgets import QApplication, QTabWidget

from pyqt_test.gui_test import *
# from pyqt_test.result_test import *

import pandas as pd

if __name__ == '__main__':
    '''
    主函数
    '''
    df = pd.read_csv('stock_px.csv', index_col=0, parse_dates=True)
    # d = pd.DataFrame([1,2,3])
    # # w = pd.ExcelWriter('asd.xls')
    # d.to_excel('asd.xls')
    # df.to_excel('asd.xlsx')

    app = QApplication(sys.argv)
    mainWindow = QTabWidget()
    ui = Ui_Dialog()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())