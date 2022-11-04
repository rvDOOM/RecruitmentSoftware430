from PySide2 import QtWidgets
from GUI import candidate_view
from GUI import add_objects_view
from backend.candidate import Candidate
from backend.company import Company


class candidate_window(candidate_view.Ui_Candidates,
                       QtWidgets.QMainWindow):
    def __init__(self):
        super(candidate_window, self).__init__()
        self.setupUi(self)
        self.populate_list_data()
        self.get_info_button.clicked.connect(self.update_candidate_info)

    def populate_list_data(self):
        self.list_data.clear()
        item = [x for x in simulated_database]
        self.list_data.addItems(item)

    def update_candidate_info(self):
        self.work_history_table.setRowCount(0)
        selection = self.list_data.currentItem().text()
        object = simulated_database[selection]
        self.number_label.setText(str(object.get_phone_number()))
        self.address_label.setText(object.get_address())
        self.email_data.setText(object.get_email())
        print(len(object.get_all_prev_employment()))
        self.work_history_table.setRowCount(len(object[selection].get_all_prev_employment()))

        # row = 1
        # for entry in object.get_all_prev_employment():
        #     for col in range(2):
        #         self.work_history_table.setItem(row, col, QtWidgets.QTableWidgetItem())


class add_objects_window(add_objects_view.Ui_MainWindow,
                         QtWidgets.QMainWindow):
    def __init__(self):
        super(add_objects_window, self).__init__()
        self.setupUi(self)


simulated_database = {}

if __name__ == '__main__':
    cp = Candidate("Test", "Dummy", True, 718627839,
                   "144 Vaughan St,\nStaten Island, NY 10403",
                   "rv91@gmail.com")
    
    simulated_database[cp.get_full_name()] = cp

    cp2 = Candidate("Another", "One", True, 7186283738,
                    "342 Kirkland blvd,\nStaten Island, NY 10304",
                    "ao21@yahoo.com")

    simulated_database[cp2.get_full_name()] = cp2

    cp3 = Candidate("Rob", "Sanchez", True, 3465748375,
                    "546 Tar Rd,\nStaten Island, NY 10302",
                    "asf@gmail.com")

    simulated_database[cp3.get_full_name()] = cp3

    company1 = Company("Grant Associates", "Recruitment")
    
    company2 = Company("Company 2", "Somethinghere")

    company3 = Company("Company 3", "SOmethingElse")

    company4 = Company("Company 4", "whatever")

    company5 = Company("Company 5", "oadjadn")

    cp.add_previous_employment(company1, "2")
    cp.add_previous_employment(company2, "4")

    cp2.add_previous_employment(company3, "1")
    
    cp3.add_previous_employment(company3, "2")
    cp3.add_previous_employment(company5, "1")
    cp3.add_previous_employment(company1, "3")

    app = QtWidgets.QApplication()
    qt_app = candidate_window()
    qt_app.show()
    app.exec_()
