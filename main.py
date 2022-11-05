from PySide2 import QtWidgets
from GUI import candidate_view
from GUI import add_objects_view
from backend.company import Company
from backend.candidate import Candidate
from backend.recruiter import Recruiter
from backend.agency import Agency
from backend.position import Position


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
        new_row = len(object.get_all_prev_employment())

        self.work_history_table.setRowCount(new_row)
        prev_company = [key for key in object.get_all_prev_employment()]
        print(prev_company)
        for row in range(new_row):
            for col in range(2):
                item_company = QtWidgets.QTableWidgetItem(prev_company[row])
                item_experience = QtWidgets.QTableWidgetItem(object.get_all_prev_employment()[prev_company[row]])
                self.work_history_table.setItem(row, 0, item_experience)
                self.work_history_table.setItem(row, 1, item_company)


class add_objects_window(add_objects_view.Ui_MainWindow,
                         QtWidgets.QMainWindow):
    def __init__(self):
        super(add_objects_window, self).__init__()
        self.setupUi(self)
        self.populate_agency_list()
        self.populate_recruiter_button()
        self.agency_button.clicked.connect(self.add_new_agency)
        self.candidate_button.clicked.connect(self.add_new_candidate)
        self.recruiter_button.clicked.connect(self.add_new_recruiter)
        self.position_button.clicked.connect(self.add_new_req)

    def add_new_agency(self):
        agency_name = self.agency_name_input.text()
        industry_sector = self.industry_sector_input.text()
        new_company = Company(agency_name, industry_sector)
        self.event_label.setText("New Agency Created")
        print(new_company)

    def add_new_candidate(self):
        first_name = self.candidate_first_name_input.text()
        last_name = self.candidate_last_name_input.text()
        address = self.address_input.text()
        email = self.email_input.text()
        phone = self.number_input.text()
        new_candidate = Candidate(first_name, last_name, address, phone, email)
        self.event_label.setText("New Candidate Created")
        print(new_candidate)

    def add_new_recruiter(self):
        first_name = self.recruiter_first_name_input.text()
        last_name = self.recruiter_last_name_input.text()
        new_recruiter = Recruiter(first_name, last_name)
        self.event_label.setText("New Recruiter Created")
        print(new_recruiter)

    def populate_agency_list(self):
        self.agency_list.clear()
        agency_item = [x for x in simulated_agency_list]
        self.agency_list.addItems(agency_item)

    def add_new_req(self):
        agency_selected = self.agency_list.currentItem().text()
        agency_object = simulated_agency_list[agency_selected]
        position_name = self.position_name_input.text()
        num_of_openings = self.num_openings_input.text()
        recruiter_selected = self.recruiter_dropdown.currentText()
        recruiter_object = simulated_recruiter_list[recruiter_selected]
        new_req = Position(position_name, num_of_openings, recruiter_object)
        agency_object.add_req(new_req)
        print(agency_object.get_req(new_req).get_name())
        
    def populate_recruiter_button(self):
        recruiters = [x for x in simulated_recruiter_list]
        self.recruiter_dropdown.addItems(recruiters)


simulated_database = {}
simulated_agency_list = {}
simulated_recruiter_list = {}
simulated_position_list = {}

if __name__ == '__main__':
    cp = Candidate("Test", "Dummy", 718627839,
                   "144 Vaughan St,\nStaten Island, NY 10403",
                   "rv91@gmail.com")
    
    simulated_database[cp.get_full_name()] = cp

    cp2 = Candidate("Another", "One", 7186283738,
                    "342 Kirkland blvd,\nStaten Island, NY 10304",
                    "ao21@yahoo.com")

    simulated_database[cp2.get_full_name()] = cp2

    cp3 = Candidate("Rob", "Sanchez", 3465748375,
                    "546 Tar Rd,\nStaten Island, NY 10302",
                    "asf@gmail.com")

    simulated_database[cp3.get_full_name()] = cp3

    company1 = Company("Grant Associates", "Recruitment")
    
    company2 = Company("Company 2", "Somethinghere")

    company3 = Company("Company 3", "SomethingElse")

    company4 = Company("Company 4", "whatever")

    company5 = Company("Company 5", "oadjadn")

    cp.add_previous_employment(company1, "2")
    cp.add_previous_employment(company2, "4")

    cp2.add_previous_employment(company3, "1")
    
    cp3.add_previous_employment(company3, "2")
    cp3.add_previous_employment(company5, "1")
    cp3.add_previous_employment(company1, "3")


    a1 = Agency("A1", "S1")
    a2 = Agency("A2", "S2")
    a3 = Agency("A3", "S3")
    a4 = Agency("A4", "S4")
    
    r1 = Recruiter("First1", "Last1")
    r2 = Recruiter("First2", "Last2")
    r3 = Recruiter("First3", "Last3")

    simulated_recruiter_list[r1.get_full_name()] = r1
    simulated_recruiter_list[r2.get_full_name()] = r2
    simulated_recruiter_list[r3.get_full_name()] = r3

    p1 = Position("Retail Associate", 5, r1)
    p2 = Position("Engineer", 2, r2)
    p3 = Position("Curator", 3, r3)
    p4 = Position("Salesman", 1, r1)
    p5 = Position("Recruiter", 5, r2)
    p6 = Position("Designer", 3, r3)
    p7 = Position("Electrician", 6, r1)
    p8 = Position("Packagesk", 2, r2)
    p9 = Position("Driver", 3, r3)
    p10 = Position("Musician", 1, r1)

    simulated_position_list[p1.get_name()] = p1
    simulated_position_list[p2.get_name()] = p2
    simulated_position_list[p3.get_name()] = p3
    simulated_position_list[p4.get_name()] = p4
    simulated_position_list[p5.get_name()] = p5
    simulated_position_list[p6.get_name()] = p6
    simulated_position_list[p7.get_name()] = p7
    simulated_position_list[p8.get_name()] = p8
    simulated_position_list[p9.get_name()] = p9
    simulated_position_list[p10.get_name()] = p10

    a1.add_req(p1)
    a1.add_req(p2)
    a1.add_req(p3)
    a2.add_req(p4)
    a2.add_req(p5)
    a2.add_req(p6)
    a3.add_req(p7)
    a3.add_req(p8)
    a3.add_req(p9)
    a3.add_req(p10)

    simulated_agency_list[a1.get_name()] = a1
    simulated_agency_list[a2.get_name()] = a2
    simulated_agency_list[a3.get_name()] = a3
    simulated_agency_list[a4.get_name()] = a4

    print(simulated_agency_list)
    print(simulated_database)
    print(simulated_position_list)
    print(simulated_recruiter_list)

    app = QtWidgets.QApplication()
    qt_app = add_objects_window()
    qt_app.show()
    app.exec_()
