# This class represents all positions the recruitment firm is actively recruiting on

from recruiter import Recruiter as rc


class Position():

    total_reqs_filled = 0

    # Constructor
    def __init__(self, position_name, numOfOpenings, recruiter):
        self.__position_name = position_name
        self.__num_of_openings = numOfOpenings
        self.__recruiter = recruiter

    # Deduct the req count by the requested amount
    def deduct_req_count(self, num_to_deduct):
        if num_to_deduct >= self.__num_of_openings:
            self.__num_of_openings -= num_to_deduct
        else:
            print("Number submitted to deduct is greater than current" +
                  "amount of reqs. No action taken.")

    # Increase the req count by specified amount
    def add_req_count(self, num_to_add):
        self.__num_of_openings += num_to_add

    def change_recruiter(self, recruiter):
        self.__recruiter = recruiter

    # Getters
    def get_num_of_openings(self):
        return self.__num_of_openings

    def get_recruiter(self):
        return self.__recruiter

    def get_name(self):
        return self.__position_name
