from company import Company as cp


class Candidate():

    __previous_employment = {}

    __job_title = "Not Applicable"

    def __init__(self, first_name, last_name,
                 employed_status):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__employed_status = employed_status

    def get_full_name(self):
        return "{} {}".format(self.__first_name, self.__last_name)

    def set_current_job_title(self, job_title):
        self.__job_title = job_title

    def get_current_job_title(self):
        return self.__job_title

    def get_employment_status(self):
        return self.__employed_status

    def set_employment_status(self):
        if self.__employed_status is False:
            self.__employed_status = True
        else:
            self.__employed_status = False

    def add_previous_employment(self, cp, years_worked):
        if cp.get_name() in self.__previous_employment:
            print("Employment history for this company has already" +
                  "been recorded")
        else:
            self.__previous_employment[cp.name] = years_worked

    def remove_previous_employment(self, cp):
        if cp.get_name() in self.previous_employment:
            del self.__previous_employment[cp.name]
        else:
            print("Employment never recorded")

    def get_prev_employment_instance(self, cp):
        if cp.get_name() in self.__previous_employment:
            return self.__previous_employment[cp.name]
        else:
            print("Employment never recorded")

    def get_all_prev_employment(self):
        return self.__previous_employment
