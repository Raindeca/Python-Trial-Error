from __patients import Patients
from __services import Services
from __on_running_tasks import Tasks
from tabulate import tabulate

class Invoice:
    

    def __init__(self, person, payment):
        self.person = person
        self.payment = payment

    total = sum(Services.service_payment)
    
    def invoice(self):
        
        # person = Tasks.fetch_patient()
        # payment = Tasks.fetch_service()
        # total = sum(Services.service_payment) 

        print("\n\n\nBiodata Pasien:")
        print("\t- Nama Pasien: ", Patients(self.person).get_full_name())
        print("\t- Nama Wali: ", Patients(self.person).get_guardian_name())
        print("\t- Alamat: ", Patients(self.person).get_address())
        print("\t- No. Telepon: ", Patients(self.person).get_phone())
        print("\t- Gol. Darah: ", Patients(self.person).get_blood_type())
        print("Pembayaran:\n")
        
        print(
            tabulate(
                [
                    [Services.get_room(), 
                    Services.medical_action(), 
                    Services.get_maternity_services(), 
                    Services.get_drug(), 
                    total]
                ],

                headers= [
                    "Biaya menginap (RP)",
                    "Penanganan (RP)",
                    "Layanan (Rp)",
                    "Obat (Rp)",
                    "TOTAL (Rp)"
                ],

                tablefmt="orgtbl"
            )
        )