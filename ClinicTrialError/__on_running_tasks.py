from __patients import Patients
from __services import Services

class Tasks:

    def fetch_patient():
        full_name = input("Full Name\t: ")
        guardian_name = input("Guardian Name\t: ")
        address = input("Address\t: ")
        phone = input("Phone Number\t: ")
        blood_type = input("Blood Type\t: ")
        return Patients(full_name,guardian_name,address,phone,blood_type)

    def fetch_service():
        drug = int(input("Drug price\t: Rp "))
        room = input("Room\t: ")
        duration = int(input("Duration of stay\t: "))
        maternity_services = input("Maternity Service\t: ")
        return Services(drug, room, duration, maternity_services)