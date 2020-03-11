class Services:
    service_payment = []

    def __init__(self, drug, room, duration, maternity_services):
        self.drug = drug
        self.room = room
        self.duration = duration
        self.maternity_services = maternity_services
    
    def get_room(self):
        if self.room == "Class 1":
            self.service_payment.append(self.duration * 450000)
            return self.duration * 450000
        elif self.room == "Class 2":
            self.service_payment.append(self.duration * 250000)
            return self.duration * 250000
        elif self.room == "Class 3":
            self.service_payment.append(self.duration * 150000)
            return self.duration * 150000
        elif self.room == "VIP":
            self.service_payment.append(self.duration * 600000)
            return self.duration * 600000
        elif self.room == "VVIP":
            self.service_payment.append(self.duration * 800000)
            return self.duration * 800000
        else:
            self.service_payment.append(0)
            return 0
    
    def get_maternity_services(self):
        if self.maternity_services == "normal":
            self.service_payment.append(4000000)
            return 4000000
        else:
            self.service_payment.append(8000000)
            return 8000000
    
    def medical_action(self):
        if self.maternity_services == "normal":
            self.service_payment.append(3000000 + 1500000)
            return 3000000 + 1500000
        else:
            self.service_payment.append(8000000)
            return 8000000
    
    def get_drug(self):
        self.service_payment.append(self.drug)
        return self.drug

    def get_service_payment(self):
        return sum(self.service_payment)