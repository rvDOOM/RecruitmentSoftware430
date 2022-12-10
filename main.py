from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow
from GUI.complete import Ui_MainWindow
import mysql.connector

recruitmentdb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='rootpw',
    database='recruitmentdb'
)

if recruitmentdb.is_connected():
    db_Info = recruitmentdb.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = recruitmentdb.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

mycursor = recruitmentdb.cursor()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.new_button.clicked.connect(self.switch_to_add_page)
        self.ui.company_button.clicked.connect(self.switch_to_company_page)
        self.ui.main_candidate_button.clicked.connect(self.switch_to_candidate_page)

    def switch_to_candidate_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Candidatepage)
        self.populate_list_data()
        self.populate_company_button2()
        self.ui.get_info_button.clicked.connect(self.update_candidate_info)
        self.ui.pushButton.clicked.connect(self.add_work_history)



    def populate_company_button2(self):
        self.ui.comboBox_2.clear()
        cursor.execute("SELECT name FROM Company")
        company_list = cursor.fetchall()
        company_res = [x[0] for x in company_list]
        print(company_res)
        self.ui.comboBox_2.addItems(company_res)



    def add_work_history(self):
        company_selected = self.ui.comboBox_2.currentText()
        yoe = self.ui.lineEdit_2.text()
        candidate_selection = self.ui.list_data.currentItem().text()
        first_name, last_name = candidate_selection.split(" ")
        add_work_history = \
            """INSERT INTO WorkHistory
            VALUES (%s, %s, %s, %s)"""
        wh_attributes = (first_name, last_name, company_selected, yoe)
        cursor.execute(add_work_history, wh_attributes)
        recruitmentdb.commit()


    def populate_list_data(self):
        # self.list_data.clear()
        # item = [x for x in simulated_database]
        # self.list_data.addItems(item)
        self.ui.list_data.clear()
        cursor.execute("SELECT firstName, lastName FROM Candidate")
        rows = cursor.fetchall()
        item = []
        for row in rows:
            firstName = row[0]
            lastName = row[1]
            item.append(firstName + " " + lastName)
        self.ui.list_data.addItems(item)


    def update_candidate_info(self):
        self.ui.work_history_table_3.setRowCount(0)
        selection = self.ui.list_data.currentItem().text()
        first_name, last_name = selection.split(" ")

        get_number = \
            """SELECT phoneNumber
            FROM Candidate
            WHERE firstName = %s && lastName = %s"""
        name = (first_name, last_name)
        cursor.execute(get_number, name)
        number = cursor.fetchone()
        self.ui.number_label_4.setText("".join(number))

        get_address = \
            """SELECT address
            FROM Candidate
            WHERE firstName = %s && lastName = %s"""
        cursor.execute(get_address, name)
        address = cursor.fetchone()
        self.ui.address_label_4.setText("".join(address))

        get_email = \
            """SELECT email
            FROM Candidate
            WHERE firstName = %s && lastName = %s"""
        cursor.execute(get_email, name)
        email = cursor.fetchone()
        self.ui.email_data_3.setText("".join(email))

        get_row_count = \
            """SELECT COUNT(*)
        FROM WorkHistory
        WHERE candidateFirstName = %s && candidateLastName = %s"""
        cursor.execute(get_row_count, name)
        row_count = cursor.fetchone()
        self.ui.work_history_table_3.setRowCount(row_count[0])

        get_all_entries = \
            """SELECT companyName, yoe 
        FROM WorkHistory 
        WHERE candidateFirstName = %s && candidateLastName = %s"""

        cursor.execute(get_all_entries, name)
        entries = cursor.fetchall()
        for row in range(row_count[0]):
            for col in range(2):
                company, yoe = entries[row]
                item_company = QtWidgets.QTableWidgetItem(company)
                item_experience = QtWidgets.QTableWidgetItem(str(yoe))
                self.ui.work_history_table_3.setItem(row, 0, item_experience)
                self.ui.work_history_table_3.setItem(row, 1, item_company)

        self.ui.interview_table2.setRowCount(0)
        get_interview_row_count = \
            """SELECT COUNT(*)
        FROM Interviews
        WHERE candidateFirstName = %s && candidateLastName = %s"""
        cursor.execute(get_interview_row_count, name)
        interview_row_count = cursor.fetchone()
        self.ui.interview_table2.setRowCount(interview_row_count[0])

        get_all_interview_entries = \
            """SELECT dateof, timeof, companyName, reqName
        FROM Interviews 
        WHERE candidateFirstName = %s && candidateLastName = %s"""

        cursor.execute(get_all_interview_entries, name)
        interview_entries = cursor.fetchall()
        for row in range(interview_row_count[0]):
            for col in range(4):
                date, time, company_name, req = interview_entries[row]
                item_company = QtWidgets.QTableWidgetItem(company_name)
                item_date = QtWidgets.QTableWidgetItem(str(date))
                item_time = QtWidgets.QTableWidgetItem(str(time))
                item_req = QtWidgets.QTableWidgetItem(req)
                self.ui.interview_table2.setItem(row, 0, item_date)
                self.ui.interview_table2.setItem(row, 1, item_time)
                self.ui.interview_table2.setItem(row, 2, item_company)
                self.ui.interview_table2.setItem(row, 3, item_req)


    def switch_to_company_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Companypage)
        self.populate_agency_button()
        self.ui.view_button.clicked.connect(self.get_company_info)

    def populate_agency_button(self):
        self.ui.sector_label.clear()
        self.ui.num_emp_label.clear()
        cursor.execute("SELECT name FROM Company")
        company_list = cursor.fetchall()
        list = [name[0] for name in company_list]
        self.ui.comboBox.addItems(list)

    def get_company_info(self):
        company_selected = self.ui.comboBox.currentText()
        company_tuple = [company_selected]
        get_employees =\
        """SELECT numOfEmployees
        FROM Company
        WHERE name = %s"""
        cursor.execute(get_employees, company_tuple)
        num_of_employees = cursor.fetchone()
        self.ui.num_emp_label.setText(str(num_of_employees[0]))

        get_sector =\
        """SELECT industrySector
        FROM Company
        WHERE name = %s"""
        cursor.execute(get_sector, company_tuple)
        sector = cursor.fetchone()
        self.ui.sector_label.setText("".join(sector))



        get_row_count = \
            """SELECT COUNT(*)
        FROM Reqs
        WHERE companyName = %s"""
        cursor.execute(get_row_count, company_tuple)
        row_count = cursor.fetchone()
        self.ui.open_reqs_table.setRowCount(row_count[0])


        get_req_info = \
            """SELECT name, numOf, recruiterFirstName, recruiterLastName
        FROM Reqs 
        WHERE companyName = %s"""

        cursor.execute(get_req_info, company_tuple)
        entries = cursor.fetchall()
        for row in range(row_count[0]):
                req_name, num, rec_first_name, rec_last_name = entries[row]
                item_req_name = QtWidgets.QTableWidgetItem(req_name)
                item_num = QtWidgets.QTableWidgetItem(str(num))
                item_recruiter = QtWidgets.QTableWidgetItem(rec_first_name + " " + rec_last_name)

                self.ui.open_reqs_table.setItem(row, 0, item_req_name)
                self.ui.open_reqs_table.setItem(row, 1, item_num)
                self.ui.open_reqs_table.setItem(row, 2, item_recruiter)

        self.populate_interviews(company_tuple)

    def populate_interviews(self,company_tuple):
        get_interview_row_count = \
            """SELECT COUNT(*)
        FROM Interviews
        WHERE companyName = %s"""
        cursor.execute(get_interview_row_count, company_tuple)
        interview_row_count = cursor.fetchone()
        self.ui.interview_table.setRowCount(interview_row_count[0])
        print(interview_row_count[0])
        get_interview_info = \
            """SELECT dateOf, timeOf, candidateFirstName, candidateLastName, reqName
        FROM Interviews 
        WHERE companyName = %s"""
        cursor.execute(get_interview_info, company_tuple)
        interview_entries = cursor.fetchall()
        print(interview_entries)
        for interview_row in range(interview_row_count[0]):
                date, time, can_first_name, can_last_name, req = interview_entries[interview_row]
                item_interview_date = QtWidgets.QTableWidgetItem(str(date))
                item_interview_time = QtWidgets.QTableWidgetItem(str(time))
                item_can_name = QtWidgets.QTableWidgetItem(can_first_name + " " + can_last_name)
                item_req_name = QtWidgets.QTableWidgetItem(req)
                self.ui.interview_table.setItem(interview_row, 0, item_interview_date)
                self.ui.interview_table.setItem(interview_row, 1, item_interview_time)
                self.ui.interview_table.setItem(interview_row, 2, item_can_name)
                self.ui.interview_table.setItem(interview_row, 3, item_req_name)

    def switch_to_add_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Addpage)
        self.populate_agency_list()
        self.populate_recruiter_button()
        self.populate_candidate_button()
        self.populate_company_button()
        self.ui.label_9.clear()
        self.ui.label_12.clear()
        self.ui.label_10.clear()
        self.ui.label_11.clear()
        self.ui.agency_button.clicked.connect(self.add_new_agency)
        self.ui.candidate_button.clicked.connect(self.add_new_candidate)
        self.ui.recruiter_button.clicked.connect(self.add_new_recruiter)
        self.ui.position_button.clicked.connect(self.add_new_req)
        self.ui.interview_button.clicked.connect(self.new_interview)
        self.ui.pushButton_2.clicked.connect(self.get_reqs)


    def clear_labels(self):
        self.ui.label_9.clear()
        self.ui.label_12.clear()
        self.ui.label_10.clear()
        self.ui.label_11.clear()
    def add_new_agency(self):
        self.clear_labels()
        agency_name = self.ui.agency_name_input.text()
        industry_sector = self.ui.industry_sector_input.text()
        num_of_employees = self.ui.lineEdit.text()
        add_agency =\
            """INSERT INTO Company
            VALUES (%s, %s, %s)"""
        agency_attributes = (agency_name, industry_sector, num_of_employees)
        cursor.execute(add_agency, agency_attributes)
        recruitmentdb.commit()
        self.populate_agency_list()

        self.ui.label_9.setText("New Agency Created")

    def add_new_candidate(self):
        self.clear_labels()
        first_name = self.ui.candidate_first_name_input.text()
        last_name = self.ui.candidate_last_name_input.text()
        address = self.ui.address_input.text()
        email = self.ui.email_input.text()
        phone = self.ui.number_input.text()

        add_candidate = \
            """INSERT INTO Candidate
            VALUES (%s, %s, %s, %s, %s)"""
        candidate_attributes = (first_name, last_name, phone, address, email)
        cursor.execute(add_candidate, candidate_attributes)
        recruitmentdb.commit()

        self.ui.label_10.setText("New Candidate Created")

    def add_new_recruiter(self):
        first_name = self.ui.recruiter_first_name_input.text()
        last_name = self.ui.recruiter_last_name_input.text()

        add_recruiter= \
            """INSERT INTO Recruiter
            VALUES (%s, %s)"""

        recruiter_attributes = (first_name, last_name)

        cursor.execute(add_recruiter, recruiter_attributes)
        recruitmentdb.commit()
        self.populate_recruiter_button()

        self.ui.label_12.setText("New Recruiter Created")


    def populate_agency_list(self):
        # self.agency_list.clear()
        # agency_item = [x for x in simulated_agency_list]
        # self.agency_list.addItems(agency_item)


        self.ui.agency_list.clear()
        cursor.execute("SELECT name FROM Company")
        rows = cursor.fetchall()
        company_list = [company[0] for company in rows]
        self.ui.agency_list.addItems(company_list)

    def add_new_req(self):
        self.clear_labels()
        agency_selected = self.ui.agency_list.currentItem().text()
        position_name = self.ui.position_name_input.text()
        num_of_openings = self.ui.num_openings_input.text()
        recruiter_selected = self.ui.recruiter_dropdown.currentText()
        pay = 10
        fulltime = 1
        recruiter_first_name, recruiter_last_name = recruiter_selected.split()

        add_req =\
        """INSERT INTO Reqs
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        req_attributes = (position_name, pay, num_of_openings, fulltime,
                          agency_selected, recruiter_first_name, recruiter_last_name)
        cursor.execute(add_req, req_attributes)
        recruitmentdb.commit()
        self.ui.label_11.setText("New Req Added!")


    def populate_recruiter_button(self):
        self.ui.recruiter_dropdown.clear()
        cursor.execute("SELECT firstName, lastName FROM Recruiter")
        recruiter_list = cursor.fetchall()
        res = [' '.join(tups) for tups in recruiter_list]
        self.ui.recruiter_dropdown.addItems(res)

    def populate_candidate_button(self):
        self.ui.candidate_box.clear()
        cursor.execute("SELECT firstName, lastName FROM Candidate")
        candidate_list = cursor.fetchall()
        cres = [' '.join(tups) for tups in candidate_list]
        self.ui.candidate_box.addItems(cres)

    def populate_company_button(self):
        self.ui.company_box.clear()
        cursor.execute("SELECT name FROM Company")
        company_list = cursor.fetchall()
        company_res = [x[0] for x in company_list]
        print(company_res)
        self.ui.company_box.addItems(company_res)

    def new_interview(self):
        candidate_selected = self.ui.candidate_box.currentText()
        position_name = self.ui.listWidget.currentItem().text()
        c_first_name, c_last_name = candidate_selected.split()
        company_selected = self.ui.company_box.currentText()
        date = self.ui.dateTimeEdit.date()
        time = self.ui.dateTimeEdit.time()
        date_final = date.toPython()
        time_final = time.toPython()
        # date_final = datetime.strptime(date, '%Y-%m-%d')
        # time_final = datetime.strptime(date, '%H:%M:%S')


        add_interview =\
        """INSERT INTO Interviews
        VALUES (%s, %s, %s, %s, %s, %s)"""

        interview_attributes = (c_first_name, c_last_name, position_name, company_selected, date_final, time_final)
        cursor.execute(add_interview, interview_attributes)
        recruitmentdb.commit()
    def get_reqs(self):
        self.ui.listWidget.clear()
        company_selected = self.ui.company_box.currentText()
        new_tuple = (company_selected,)
        print(new_tuple)
        cursor.execute("SELECT name FROM Reqs WHERE companyName = %s", new_tuple)
        new_rows = cursor.fetchall()
        print(new_rows)
        req_list = [''.join(i) for i in new_rows]
        print(req_list)
        cursor.execute("SELECT COUNT(*) FROM Reqs WHERE companyName = %s", new_tuple)
        iteration = cursor.fetchone()
        self.ui.listWidget.addItems(req_list)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MainWindow()
    qt_app.show()
    app.exec_()
