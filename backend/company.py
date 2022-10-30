class Company():
    def __init__(self, name, industry_sector):
        self.__name = name
        self.__industry_sector = industry_sector

    def set_name(self, name):
        self.name = name

    def set_industry(self, industry_sector):
        self.industry_sector = industry_sector

    def get_name(self):
        return self.__name

    def get_industry(self):
        return self.__industry_sector
