class Patients:
#    thisPatients = []

    def __init__(self, full_name, guardian_name, address, phone, blood_type):
        self.full_name = full_name
        self.guardian_name = guardian_name
        self.address = address
        self.phone = phone
        self.blood_type = blood_type

    def get_full_name(self):
        return self.full_name
    
    def get_guardian_name(self):
        return self.guardian_name

    def get_address(self):
        return self.address
    
    def get_phone(self):
        return self.phone

    def get_blood_type(self):
        return self.blood_type