class Services:
    service_payment = []

    def __init__(self, drug, room, duration, maternity_services):
        self.drug = drug
        self.room = room
        self.duration = duration
        self.maternity_services = maternity_services
    
    def get_room(self):
        if self.room == "Class 1":
            service_payment.append(self.duration * 450000)
            return self.duration * 450000
        elif self.room == "Class 2":
            service_payment.append(self.duration * 250000)
            return self.duration * 250000
        elif self.room == "Class 3":
            service_payment.append(self.duration * 150000)
            return self.duration * 150000
        elif self.room == "VIP":
            service_payment.append(self.duration * 600000)
            return self.duration * 600000
        elif self.room == "VVIP":
            service_payment.append(self.duration * 800000)
            return self.duration * 800000
        else:
            service_payment.append(0)
            return 0
    
    def get_maternity_servives(self):
        if self.maternity_services == "normal":
            service_payment.append(4000000)
            return 4000000
        else:
            service_payment.append(8000000)
            return 8000000
    
    def medical_action(self):
        if self.maternity_services == "normal":
            service_payment.append(3000000 + 1500000)
            return 3000000 + 1500000
        else:
            service_payment.append(8000000)
            return 8000000
    
    def get_drug(self):
        service_payment.append(self.drug)
        return self.drug