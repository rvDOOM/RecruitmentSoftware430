from PySide2 import QtWidgets
from GUI import candidate_view
from GUI import add_objects_view


class candidate_window(candidate_view.Ui_Candidates,
                       QtWidgets.QMainWindow):
    def __init__(self):
        super(candidate_window, self).__init__()
        self.setupUi(self)


class add_objects_window(add_objects_view.Ui_MainWindow,
                         QtWidgets.QMainWindow):
    def __init__(self):
        super(add_objects_window, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = add_objects_window()
    qt_app.show()
    app.exec_()
