from __patients import Patients
from __services import Services
from __on_running_tasks import Tasks
from tabulate import tabulate

class Invoice:
    

    def __init__(self, person, payment):
        self.person = person
        self.payment = payment

    
    def invoice(self):
         

        print("\n\n\nBiodata Pasien:")
        print("\t- Nama Pasien: ", self.person.get_full_name())
        print("\t- Nama Wali: ", self.person.get_guardian_name())
        print("\t- Alamat: ", self.person.get_address())
        print("\t- No. Telepon: ", self.person.get_phone())
        print("\t- Gol. Darah: ", self.person.get_blood_type())
        print("Pembayaran:\n")
        
        print(
            tabulate(
                [
                    [self.payment.get_room(), 
                    self.payment.medical_action(), 
                    self.payment.get_maternity_services(), 
                    self.payment.get_drug(), 
                    self.payment.get_service_payment()]
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