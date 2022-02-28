class Patient:
    

    def __init__(self, id, name, address, phone, veteranStatus):
        self.__iden = id
        self.__patientName = name
        self.__add = address
        self.__phoneNum = phone
        self.__veteran = veteranStatus

    def get_iden(self):
        return self.__iden

    def get_patient(self):
        return self.__patientName
    
    def get_add(self):
        return self.__add

    def get_phoneNum(self):
        return self.__phoneNum

    def get_veteran(self):
        return self.__veteran

 