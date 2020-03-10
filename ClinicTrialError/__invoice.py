from __patients import Patients
from __services import Services
from __create_structure import Create_Structure
from tabulate import tabulate

class Invoice:
    

    def __init__(self, person, payment):
        self.person = Patients(Create_Structure.patient())
        self.payment = Services(Create_Structure.service())
    
    total = sum(Services.service_payment) 

    def invoice(self):
        print("Biodata Pasien:")
        print("\t- Nama Pasien: ", person.get_full_name(self))
        print("\t- Nama Wali: ", person.get_guardian_name(self))
        print("\t- Alamat: ", person.get_address(self))
        print("\t= No. Telepon: ", person.get_phone(self))
        print("\t- Gol. Darah: ", person.get_blood_type(self))
        print("Pembayaran:\n")
        
        print(
            tabulate(
                [
                    [payment.get_room(self), 
                    payment.medical_action(self), 
                    payment.get_maternity_services(self), 
                    payment.get_drug(self), 
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