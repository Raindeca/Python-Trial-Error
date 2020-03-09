from __patients import Patients
from __services import Services
from tabulate import tabulate

class Invoice:

    total = sum(Services.service_payment)
    
    person = Patients()

    def invoice():
        print("Biodata Pasien:")
        print("\t- Nama Pasien: ", person.get_full_name())
        print("\t- Nama Wali: ", person.get_guardian_name())
        print("\t- Alamat: ", person.get_address())
        print("\t= No. Telepon: ", person.get_phone())
        print("\t- Gol. Darah: ", person.get_blood_type())
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