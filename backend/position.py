from recruiter import Recruiter as rc


class Position():

    total_reqs_filled = 0

    def __init__(self, position_name, numOfOpenings, recruiter):
        self.__position_name = position_name
        self.__num_of_openings = numOfOpenings
        self.__recruiter = recruiter

    # Deducts past 0. NEED TO FIX
    def deduct_req_count(self, num_to_deduct):
        if self.__num_of_openings >= 0:
            self.__num_of_openings -= num_to_deduct
        else:
            print("Number submitted to deduct is greater than current" +
                  "amount of reqs. No action taken.")

    def add_req_count(self, num_to_add):
        self.__num_of_openings += num_to_add

    def change_recruiter(self, recruiter):
        self.__recruiter = recruiter

    def get_num_of_openings(self):
        return self.__num_of_openings

    def get_recruiter(self):
        return self.__recruiter

    def get_name(self):
        return self.__position_name
