# This class holds the information of any given company
# The company isn't associated with the recruitment firm
# but it allows the recruitment firm to associate several companies
# with a candidate's previous work experience

class Company():

    # Contructor
    def __init__(self, name, industry_sector):
        self.__name = name
        self.__industry_sector = industry_sector

    # Setters
    def set_name(self, name):
        self.name = name

    def set_industry(self, industry_sector):
        self.industry_sector = industry_sector

    # Getters
    def get_name(self):
        return self.__name

    def get_industry(self):
        return self.__industry_sector
