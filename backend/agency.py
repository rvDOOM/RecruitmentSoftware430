from company import Company as cp
from position import Position as ps
from recruiter import Recruiter as rc


class Agency(cp):

    __all_reqs = {}

    def __init__(self, name, industry_sector):
        super().__init__(name, industry_sector)

    def add_req(self, ps):
        if ps.get_name() in self.__all_reqs:
            print("This position has already been added with this Agency")
        else:
            self.__all_reqs[ps.get_name()] = ps.get_num_of_openings()

    def remove_req(self, ps):
        if ps.get_name() in self.__all_reqs:
            del self.__all_reqs[ps.get_name()]
        else:
            print("Req is currently not associated with this agency")

    def get_all_reqs(self):
        return self.__all_reqs
