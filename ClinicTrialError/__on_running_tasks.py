from __patients import Patients
from __services import Services

class tasks:

    def fetch_patient():
        full_name = input("Full Name\t: ")
        guardian_name = input("Guardian Name\t: ")
        address = input("Address\t: ")
        phone = input("Phone Number\t: ")
        blood_type = input("Blood Type\t: ")
        Patients(full_name,guardian_name,address,phone,blood_type)

    def fetch_service():
        drug = input("Drug price\t: Rp ")
        room = input("Room\t: ")
        duration = input("Duration of stay\t: ")
        maternity_services = input("Maternity Service\t: ")
        Services(drug, room, duration, maternity_services)