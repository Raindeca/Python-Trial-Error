class Services:
    
    def __init__(self, rooms, durations, maternityServices):
        self.rooms = rooms
        self.durations = durations
        self.maternityServices = maternityServices
    
    def getRooms(self):
        if self.rooms == "Class 1":
            return self.durations * 450000
        elif self.rooms == "Class 2":
            return self.durations * 250000
        elif self.rooms == "Class 3":
            return self.durations * 150000
        elif self.rooms == "VIP":
            return self.durations * 600000
        elif self.rooms == "VVIP":
            return self.durations * 800000
        else:
            return 0
    
    def getMaternityServives:
        if self.maternityServices == "normal":
            return 4000000
        else:
            return 8000000
    
    def medicalAction:
        if self.maternityServices == "normal":
            return 3000000 + 1500000
        else:
            return 8000000
    