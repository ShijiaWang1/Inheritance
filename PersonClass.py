class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def get_telephone(self):
        return self.__telephone


class Customer(Person):
    def __init__(self, name, address, telephone, mailList):
        self.__mailList = mailList
        Person.__init__(self, name, address, telephone, mailList)

    def set_mailList(self, mailList):
        self.__mailList = mailList

    def get_mailList(self):
        return self.__mailList

    def __str__(self):
        return (
            self.get_name(),
            self.get_address(),
            self.get_telephone(),
            self.mailList(),
        )
