# An agency represents a company that the recruitment firm is actively recruiting for
# The class contains a dictionary that holds every Position where the agency is actively seeking candidates
# All dictionary methods must pass a Position object to function

from company import Company as cp
from position import Position as ps
from recruiter import Recruiter as rc


class Agency(cp):

    __all_reqs = {}
    
    # Constructor
    def __init__(self, name, industry_sector):
        super().__init__(name, industry_sector)
    
    # Adds a new position(ps) to the req dictionary
    def add_req(self, ps):
        if ps.get_name() in self.__all_reqs:
            print("This position has already been added with this Agency")
        else:
            self.__all_reqs[ps.get_name()] = ps

    # Removes a position(ps) from the req disctionary
    def remove_req(self, ps):
        if ps.get_name() in self.__all_reqs:
            del self.__all_reqs[ps.get_name()]
        else:
            print("Req is currently not associated with this agency")

    def get_req(self, ps):
        return self.__all_reqs[ps]
    
    # Get the req dictionary
    def get_all_reqs(self):
        return self.__all_reqs
