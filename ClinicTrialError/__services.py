class Services:
    
    def __init__(self, drug, room, duration, maternity_services):
        self.drug = drug
        self.room = room
        self.duration = duration
        self.maternity_services = maternity_services
    
    def get_room(self):
        if self.room == "Class 1":
            return self.duration * 450000
        elif self.room == "Class 2":
            return self.duration * 250000
        elif self.room == "Class 3":
            return self.duration * 150000
        elif self.room == "VIP":
            return self.duration * 600000
        elif self.room == "VVIP":
            return self.duration * 800000
        else:
            return 0
    
    def get_maternity_servives(self):
        if self.maternity_services == "normal":
            return 4000000
        else:
            return 8000000
    
    def medical_action(self):
        if self.maternity_services == "normal":
            return 3000000 + 1500000
        else:
            return 8000000
    
    def get_drug(self):
        return self.drug