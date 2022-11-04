# The candidate class holds all the information the recruitment firm has on a candidate
# Contains a dictionary that holds previous work experience
# where the key is the name of the company they worked for and the value is YOE
# All methods associated with the dictionary takes a Company object(cp)


from company import Company as cp


class Candidate():

    # Dictionary of work experience KEY = company name Value = YOE
    __previous_employment = {}

    __job_title = "Not Applicable"

    # Constructor
    def __init__(self, first_name, last_name, employed_status, phone_number, address, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__employed_status = employed_status
        self.__phone_number = phone_number
        self.__address = address
        self.__email = email
    
    # Getters

    # Get a candidate's full name returned as "first_name last_name"
    def get_full_name(self):
        return "{} {}".format(self.__first_name, self.__last_name)

    def get_current_job_title(self):
        return self.__job_title

    def get_employment_status(self):
        return self.__employed_status

    def get_phone_number(self):
        return self.__phone_number

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    # Setters
    def set_current_job_title(self, job_title):
        self.__job_title = job_title

    def set_employment_status(self):
        if self.__employed_status is False:
            self.__employed_status = True
        else:
            self.__employed_status = False

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_address(self, address):
        self.__address = address

    def set_email(self, email):
        self.__email = email

    # Adds an entry for candidate's previous employment
    def add_previous_employment(self, cp, years_worked):
        if cp.get_name() in self.__previous_employment:
            print("Employment history for this company has already" +
                  "been recorded")
        else:
            self.__previous_employment[cp.name] = years_worked

    # Removes an entry from previous employement
    def remove_previous_employment(self, cp):
        if cp.get_name() in self.previous_employment:
            del self.__previous_employment[cp.name]
        else:
            print("Employment never recorded")

    # Get a specific entry from previous employment
    def get_prev_employment_instance(self, cp):
        if cp.get_name() in self.__previous_employment:
            return self.__previous_employment[cp.name]
        else:
            print("Employment never recorded")

    # Get the dictionary object of previous employment
    def get_all_prev_employment(self):
        return self.__previous_employment
