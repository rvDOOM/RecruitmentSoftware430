class Recruiter:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_full_name(self):
        return '{} {}'.format(self.__first_name, self.__last_name)

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name
