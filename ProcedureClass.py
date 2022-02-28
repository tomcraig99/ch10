class Procedure:
    

    def __init__(self, procName, date, pracName, pay, patID):
        self.__proc = procName
        self.__datePerf = date
        self.__practitioner = pracName
        self.__payment = pay
        self.__patient = patID

    def get_proc(self):
        return self.__proc

    def get_date(self):
        return self.__datePerf

    def get_practitioner(self):
        return self.__practitioner

    def get_pay(self):
        return self.__payment

    def get_patient(self):
        return self.__patient